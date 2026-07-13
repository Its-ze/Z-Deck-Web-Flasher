#!/usr/bin/env python3
"""Verify the dedicated-partition Z-Deck + MeshCore installer."""

from __future__ import annotations

import json
import pathlib
import sys

EXPECTED_OFFSETS = {0x0, 0x8000, 0xE000, 0x10000, 0x510000, 0xA10000}
ZDECK_OFFSETS = {0x10000, 0x510000}
MESHCORE_OFFSET = 0xA10000
STORAGE_START = 0xC90000
ZDECK_SLOT_SIZE = 0x500000
MESHCORE_SLOT_SIZE = 0x280000


def load_json(path: pathlib.Path):
    with path.open(encoding="utf-8-sig") as handle:
        return json.load(handle)


def main() -> int:
    root = pathlib.Path(__file__).resolve().parents[1]
    manifest = load_json(root / "manifest-dual.json")
    ota = load_json(root / "update-ota.json")
    failures: list[str] = []
    builds = manifest.get("builds", [])
    parts = builds[0].get("parts", []) if len(builds) == 1 and builds[0].get("chipFamily") == "ESP32-S3" else []
    if not parts:
        failures.append("dual manifest must contain one ESP32-S3 build")
    by_offset = {int(part.get("offset", -1)): str(part.get("path", "")) for part in parts}
    if set(by_offset) != EXPECTED_OFFSETS:
        failures.append(f"unexpected flash offsets: {sorted(hex(value) for value in by_offset)}")
    if any(offset >= STORAGE_START for offset in by_offset):
        failures.append("dual manifest must not write NVS, LittleFS, or later storage partitions")

    zdeck_path = str(ota.get("latest", {}).get("firmware", {}).get("path", ""))
    if any(by_offset.get(offset) != zdeck_path for offset in ZDECK_OFFSETS):
        failures.append("both Z-Deck A/B slots must use the OTA payload")
    if "meshcore" not in by_offset.get(MESHCORE_OFFSET, "").lower():
        failures.append("dedicated MeshCore partition is missing")

    for offset, relative in sorted(by_offset.items()):
        path = root / relative
        if not path.is_file():
            failures.append(f"missing part at {hex(offset)}: {relative}")
            continue
        size = path.stat().st_size
        if offset in ZDECK_OFFSETS and size > ZDECK_SLOT_SIZE:
            failures.append(f"Z-Deck at {hex(offset)} exceeds its slot")
        if offset == MESHCORE_OFFSET and size > MESHCORE_SLOT_SIZE:
            failures.append("MeshCore exceeds its dedicated partition")
        if offset in ZDECK_OFFSETS | {MESHCORE_OFFSET, 0x0} and path.read_bytes()[:1] != b"\xe9":
            failures.append(f"part at {hex(offset)} is not an ESP32 image")
        print(f"OK:   {hex(offset)} {relative} ({size} bytes)")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print("\nDual release checks passed; MeshCore is outside OTA A/B and storage is untouched.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
