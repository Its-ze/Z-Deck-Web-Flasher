#!/usr/bin/env python3
"""Verify the Z-Deck migration and A/B OTA release contracts."""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import sys
import urllib.request
from typing import Any

REQUIRED_PRESERVES = {
    "meshtastic_config", "channels", "keys", "owner_settings",
    "sd_chat_journal", "sd_settings_backup",
}
APP_SLOT_OFFSETS = {0x10000, 0x510000}
MESHCORE_OFFSET = 0xA10000
LITTLEFS_OFFSET = 0xC90000
APP_SLOT_SIZE = 0x500000


def load_json(path: pathlib.Path) -> Any:
    with path.open(encoding="utf-8-sig") as handle:
        return json.load(handle)


def fetch(url: str) -> bytes:
    with urllib.request.urlopen(url, timeout=120) as response:
        if response.status != 200:
            raise RuntimeError(f"{url} returned HTTP {response.status}")
        return response.read()


def digest(data: bytes) -> tuple[str, str]:
    return hashlib.sha256(data).hexdigest(), hashlib.md5(data).hexdigest()


def check(condition: bool, message: str, failures: list[str]) -> None:
    print(f"{'OK:  ' if condition else 'FAIL:'} {message}")
    if not condition:
        failures.append(message)


def parts_by_offset(manifest: dict[str, Any]) -> dict[int, str]:
    parts = manifest.get("builds", [{}])[0].get("parts", [])
    return {int(part["offset"]): str(part["path"]) for part in parts}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".")
    parser.add_argument("--live", action="store_true")
    args = parser.parse_args()
    root = pathlib.Path(args.root).resolve()
    failures: list[str] = []

    legacy = load_json(root / "update.json")
    ota = load_json(root / "update-ota.json")
    standard = load_json(root / "manifest.json")
    dual = load_json(root / "manifest-dual.json")
    test_manifest = load_json(root / "manifest-ota-test.json")
    legacy_latest = legacy.get("latest", {})
    latest = ota.get("latest", {})
    firmware = latest.get("firmware", {})

    check(legacy_latest.get("updateMode") == "usb-migration", "legacy update.json blocks unsafe OTA and requires USB migration", failures)
    check(legacy_latest.get("migrationManifest") == "manifest-dual.json", "legacy manifest points to the preservation-safe dual installer", failures)
    check(latest.get("updateMode") == "app-only", "update-ota.json is app-only", failures)
    check(latest.get("preUpdateBackup", {}).get("enabled") is False, "OTA does not require the crash-prone SD preflight backup", failures)
    check(REQUIRED_PRESERVES <= set(latest.get("preserves", [])), "OTA preservation list covers settings, channels, keys, and SD data", failures)

    firmware_path = str(firmware.get("path", ""))
    payload = root / firmware_path
    check(payload.is_file(), f"OTA payload exists: {firmware_path}", failures)
    if payload.is_file():
        data = payload.read_bytes()
        sha256, md5 = digest(data)
        check(len(data) == int(firmware.get("size", 0)), "OTA payload size matches metadata", failures)
        check(sha256 == str(firmware.get("sha256", "")).lower(), "OTA payload SHA256 matches metadata", failures)
        check(md5 == str(firmware.get("md5", "")).lower(), "OTA payload MD5 matches metadata", failures)
        check(len(data) <= APP_SLOT_SIZE, "OTA payload fits a 5 MB app slot", failures)

    metadata = load_json(payload.parent / "zdeck-meshtastic-metadata.json") if payload.is_file() else {}
    check(metadata.get("version") == latest.get("firmwareVersion"), "firmware metadata version matches OTA manifest", failures)
    check(metadata.get("zDeckPackVersion") == latest.get("packVersion"), "pack version matches OTA manifest", failures)

    standard_parts = parts_by_offset(standard)
    dual_parts = parts_by_offset(dual)
    test_parts = parts_by_offset(test_manifest)
    check(all(standard_parts.get(offset) == firmware_path for offset in APP_SLOT_OFFSETS), "standard installer writes zdeck55 to both A/B slots", failures)
    check(standard_parts.get(LITTLEFS_OFFSET, "").endswith("zdeck-littlefs.bin"), "standard installer writes LittleFS separately", failures)
    check(all(dual_parts.get(offset) == firmware_path for offset in APP_SLOT_OFFSETS), "dual installer writes zdeck55 to both A/B slots", failures)
    check("meshcore" in dual_parts.get(MESHCORE_OFFSET, "").lower(), "dual installer writes MeshCore only to its dedicated partition", failures)
    check(LITTLEFS_OFFSET not in dual_parts, "dual installer preserves LittleFS", failures)
    check(all("zdeck54-migration" in test_parts.get(offset, "") for offset in APP_SLOT_OFFSETS), "OTA test installer provides a zdeck54 A/B baseline", failures)
    check("meshcore" in test_parts.get(MESHCORE_OFFSET, "").lower(), "OTA test installer preserves the dedicated MeshCore layout", failures)

    if args.live and payload.is_file():
        live_legacy = json.loads(fetch("https://its-ze.github.io/Z-Deck-Web-Flasher/update.json").decode("utf-8-sig"))
        live_ota = json.loads(fetch("https://its-ze.github.io/Z-Deck-Web-Flasher/update-ota.json").decode("utf-8-sig"))
        check(live_legacy.get("latest", {}).get("updateMode") == "usb-migration", "live legacy manifest requires USB migration", failures)
        check(live_ota.get("latest", {}).get("firmware", {}).get("sha256") == firmware.get("sha256"), "live OTA manifest matches local SHA256", failures)
        live_data = fetch(str(firmware.get("url", "")))
        check(digest(live_data)[0] == firmware.get("sha256"), "live OTA payload matches SHA256", failures)

    if failures:
        print(f"\n{len(failures)} OTA release check(s) failed.")
        return 1
    print("\nOTA migration and A/B release checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
