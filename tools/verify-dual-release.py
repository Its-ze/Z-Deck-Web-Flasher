#!/usr/bin/env python3
"""Verify the public Z-Deck + MeshCore ESP Web Tools manifest."""

from __future__ import annotations

import json
import pathlib
import sys
from typing import Any


EXPECTED_OFFSETS = {0x0, 0x8000, 0xE000, 0x10000, 0x650000}
APP_OFFSETS = {0x10000, 0x650000}
STORAGE_START = 0xC90000
SLOT_SIZE = 0x640000


def load_json(path: pathlib.Path) -> Any:
    with path.open(encoding="utf-8-sig") as handle:
        return json.load(handle)


def main() -> int:
    root = pathlib.Path(__file__).resolve().parents[1]
    manifest = load_json(root / "manifest-dual.json")
    update = load_json(root / "update.json")
    failures: list[str] = []

    builds = manifest.get("builds") or []
    if len(builds) != 1 or builds[0].get("chipFamily") != "ESP32-S3":
        failures.append("dual manifest must contain one ESP32-S3 build")
        parts: list[dict[str, Any]] = []
    else:
        parts = builds[0].get("parts") or []

    by_offset = {int(part.get("offset", -1)): str(part.get("path", "")) for part in parts}
    if set(by_offset) != EXPECTED_OFFSETS:
        failures.append(f"unexpected flash offsets: {sorted(hex(value) for value in by_offset)}")

    if any(offset >= STORAGE_START for offset in by_offset):
        failures.append("dual manifest must not write NVS, LittleFS, or later storage partitions")

    zdeck_path = by_offset.get(0x10000, "")
    ota_path = str(update.get("latest", {}).get("firmware", {}).get("path", ""))
    if zdeck_path != ota_path:
        failures.append("dual app0 must use the same Z-Deck image as update.json")

    if by_offset.get(0x650000) == zdeck_path:
        failures.append("dual app1 must be a distinct MeshCore image")

    for offset, relative_path in sorted(by_offset.items()):
        path = root / relative_path
        if not path.is_file():
            failures.append(f"missing part at {hex(offset)}: {relative_path}")
            continue
        size = path.stat().st_size
        if offset in APP_OFFSETS and size > SLOT_SIZE:
            failures.append(f"app at {hex(offset)} exceeds the {SLOT_SIZE}-byte slot")
        if offset in APP_OFFSETS | {0x0} and path.read_bytes()[:1] != b"\xe9":
            failures.append(f"part at {hex(offset)} is not an ESP32 image")
        print(f"OK:   {hex(offset)} {relative_path} ({size} bytes)")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        print(f"\n{len(failures)} dual release check(s) failed.")
        return 1

    print("\nDual release checks passed; no storage partition is written.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
