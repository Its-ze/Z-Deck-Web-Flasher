#!/usr/bin/env python3
"""Verify the public Z-Deck OTA release metadata and payload.

This checks the app-only update contract used by Settings > Z-Deck OTA:
- update.json must describe an app-only firmware update.
- The OTA payload must be the app firmware image, not LittleFS or factory image.
- Local payload size, SHA256, and MD5 must match update.json.
- Web flasher manifest app slots must point at the same app firmware path.
- Optional --live downloads the hosted update.json and firmware URL and verifies
  the hosted bytes too.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import sys
import urllib.request
from typing import Any


REQUIRED_PRESERVES = {
    "meshtastic_config",
    "channels",
    "keys",
    "owner_settings",
    "sd_chat_journal",
    "sd_settings_backup",
}

APP_SLOT_OFFSETS = {0x10000, 0x650000}
LITTLEFS_OFFSET = 0xC90000


def load_json(path: pathlib.Path) -> Any:
    with path.open(encoding="utf-8-sig") as handle:
        return json.load(handle)


def fetch_json(url: str) -> Any:
    with urllib.request.urlopen(url, timeout=30) as response:
        if response.status != 200:
            raise RuntimeError(f"{url} returned HTTP {response.status}")
        return json.loads(response.read().decode("utf-8-sig"))


def fetch_bytes(url: str) -> bytes:
    with urllib.request.urlopen(url, timeout=120) as response:
        if response.status != 200:
            raise RuntimeError(f"{url} returned HTTP {response.status}")
        return response.read()


def digest(data: bytes) -> tuple[str, str]:
    return hashlib.sha256(data).hexdigest(), hashlib.md5(data).hexdigest()


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)
    print(f"FAIL: {message}")


def ok(message: str) -> None:
    print(f"OK:   {message}")


def validate(root: pathlib.Path, update_json: dict[str, Any], manifest_json: dict[str, Any], live: bool) -> int:
    failures: list[str] = []

    latest = update_json.get("latest")
    if not isinstance(latest, dict):
        fail("update.json missing latest object", failures)
        return 1

    firmware = latest.get("firmware")
    if not isinstance(firmware, dict):
        fail("update.json latest.firmware must be an object", failures)
        return 1

    pack_version = str(latest.get("packVersion", ""))
    firmware_version = str(latest.get("firmwareVersion", ""))
    update_mode = str(latest.get("updateMode", ""))
    firmware_path = str(firmware.get("path", ""))
    firmware_url = str(firmware.get("url", ""))
    expected_size = int(firmware.get("size") or 0)
    expected_sha256 = str(firmware.get("sha256", "")).lower()
    expected_md5 = str(firmware.get("md5", "")).lower()

    if pack_version:
        ok(f"packVersion is {pack_version}")
    else:
        fail("latest.packVersion is missing", failures)

    if firmware_version:
        ok(f"firmwareVersion is {firmware_version}")
    else:
        fail("latest.firmwareVersion is missing", failures)

    if update_mode == "app-only":
        ok("updateMode is app-only")
    else:
        fail(f"updateMode must be app-only, got {update_mode!r}", failures)

    if firmware_path and "littlefs" not in firmware_path.lower() and "factory" not in firmware_path.lower():
        ok(f"OTA path is app firmware: {firmware_path}")
    else:
        fail(f"OTA path must be app firmware, got {firmware_path!r}", failures)

    if firmware_url.startswith("https://"):
        ok("firmware URL is HTTPS")
    else:
        fail(f"firmware URL must be HTTPS, got {firmware_url!r}", failures)

    preserves = set(latest.get("preserves") or [])
    missing_preserves = REQUIRED_PRESERVES - preserves
    if not missing_preserves:
        ok("preserves list includes required config/data protections")
    else:
        fail(f"preserves list missing: {', '.join(sorted(missing_preserves))}", failures)

    pre_backup = latest.get("preUpdateBackup") or {}
    if pre_backup.get("enabled") is True and pre_backup.get("location") == "sd":
        ok("preUpdateBackup requires SD backup")
    else:
        fail("preUpdateBackup must be enabled with location sd", failures)
    if pre_backup.get("path") == "/zdeck/backups/preferences.proto":
        ok("preUpdateBackup path is /zdeck/backups/preferences.proto")
    else:
        fail(f"unexpected preUpdateBackup path: {pre_backup.get('path')!r}", failures)

    local_firmware = (root / firmware_path).resolve()
    if not local_firmware.exists():
        fail(f"local firmware payload missing: {firmware_path}", failures)
        return 1

    data = local_firmware.read_bytes()
    actual_sha256, actual_md5 = digest(data)
    if len(data) == expected_size:
        ok(f"local firmware size matches: {expected_size}")
    else:
        fail(f"local firmware size mismatch: expected {expected_size}, got {len(data)}", failures)
    if actual_sha256 == expected_sha256:
        ok("local firmware SHA256 matches update.json")
    else:
        fail(f"local firmware SHA256 mismatch: {actual_sha256}", failures)
    if actual_md5 == expected_md5:
        ok("local firmware MD5 matches update.json")
    else:
        fail(f"local firmware MD5 mismatch: {actual_md5}", failures)

    metadata_path = local_firmware.parent / "zdeck-meshtastic-metadata.json"
    if metadata_path.exists():
        metadata = load_json(metadata_path)
        if metadata.get("version") == firmware_version:
            ok("metadata firmware version matches update.json")
        else:
            fail("metadata firmware version does not match update.json", failures)
        if metadata.get("zDeckPackVersion") == pack_version:
            ok("metadata pack version matches update.json")
        else:
            fail("metadata pack version does not match update.json", failures)
    else:
        fail(f"metadata missing beside firmware: {metadata_path}", failures)

    parts = manifest_json.get("builds", [{}])[0].get("parts", [])
    app_parts = {
        int(part.get("offset", -1)): part.get("path")
        for part in parts
        if isinstance(part, dict) and int(part.get("offset", -1)) in APP_SLOT_OFFSETS
    }
    if set(app_parts) == APP_SLOT_OFFSETS and all(path == firmware_path for path in app_parts.values()):
        ok("Web flasher manifest app slots match OTA firmware path")
    else:
        fail(f"manifest app slots do not match OTA path: {app_parts}", failures)

    littlefs_parts = [
        part.get("path")
        for part in parts
        if isinstance(part, dict) and int(part.get("offset", -1)) == LITTLEFS_OFFSET
    ]
    if littlefs_parts and firmware_path not in littlefs_parts:
        ok("OTA firmware path is separate from LittleFS first-install part")
    else:
        fail("OTA firmware path must not be the LittleFS part", failures)

    if live:
        live_update = fetch_json("https://its-ze.github.io/Z-Deck-Web-Flasher/update.json")
        if live_update.get("latest", {}).get("firmware", {}).get("sha256", "").lower() == expected_sha256:
            ok("live update.json SHA256 matches local update.json")
        else:
            fail("live update.json SHA256 differs from local update.json", failures)

        live_data = fetch_bytes(firmware_url)
        live_sha256, live_md5 = digest(live_data)
        if len(live_data) == expected_size:
            ok("live firmware size matches update.json")
        else:
            fail(f"live firmware size mismatch: expected {expected_size}, got {len(live_data)}", failures)
        if live_sha256 == expected_sha256:
            ok("live firmware SHA256 matches update.json")
        else:
            fail(f"live firmware SHA256 mismatch: {live_sha256}", failures)
        if live_md5 == expected_md5:
            ok("live firmware MD5 matches update.json")
        else:
            fail(f"live firmware MD5 mismatch: {live_md5}", failures)

    if pack_version and firmware_version:
        ok(f"installed {pack_version}/{firmware_version} should report current/no update against this manifest")

    if failures:
        print(f"\n{len(failures)} OTA release check(s) failed.")
        return 1

    print("\nOTA release checks passed.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify Z-Deck app-only OTA release metadata.")
    parser.add_argument("--root", default=".", help="repository root")
    parser.add_argument("--live", action="store_true", help="also verify live GitHub Pages update.json and firmware bytes")
    args = parser.parse_args()

    root = pathlib.Path(args.root).resolve()
    update_json = load_json(root / "update.json")
    manifest_json = load_json(root / "manifest.json")
    return validate(root, update_json, manifest_json, args.live)


if __name__ == "__main__":
    sys.exit(main())
