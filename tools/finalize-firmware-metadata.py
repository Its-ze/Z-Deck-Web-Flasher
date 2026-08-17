#!/usr/bin/env python3
"""Refresh and verify app/LittleFS hashes in generated Meshtastic metadata."""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("build_dir", type=pathlib.Path)
    args = parser.parse_args()
    build_dir = args.build_dir.resolve()
    manifests = sorted(build_dir.glob("*.mt.json"))
    if len(manifests) != 1:
        print(f"ERROR: expected one *.mt.json in {build_dir}, found {len(manifests)}")
        return 1

    manifest_path = manifests[0]
    manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
    files = manifest.get("files")
    if not isinstance(files, list):
        print("ERROR: firmware metadata has no files list")
        return 1

    refreshed: set[str] = set()
    for entry in files:
        part_name = entry.get("part_name")
        if part_name not in {"app0", "spiffs"}:
            continue
        artifact = build_dir / str(entry.get("name", ""))
        if not artifact.is_file():
            print(f"ERROR: metadata artifact is missing: {artifact.name}")
            return 1
        data = artifact.read_bytes()
        entry["bytes"] = len(data)
        entry["md5"] = hashlib.md5(data).hexdigest()
        refreshed.add(part_name)

    if refreshed != {"app0", "spiffs"}:
        print(f"ERROR: expected app0 and spiffs metadata, refreshed {sorted(refreshed)}")
        return 1

    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"OK: refreshed app0 and spiffs metadata in {manifest_path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
