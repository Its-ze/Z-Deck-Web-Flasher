#!/usr/bin/env python3
"""Write SHA256SUMS.json for one packaged firmware directory."""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("firmware_dir", type=pathlib.Path)
    args = parser.parse_args()
    root = args.firmware_dir.resolve()
    entries = []
    for path in sorted(root.iterdir()):
        if not path.is_file() or path.name == "SHA256SUMS.json":
            continue
        data = path.read_bytes()
        entries.append({"name": path.name, "length": len(data), "sha256": hashlib.sha256(data).hexdigest()})
    (root / "SHA256SUMS.json").write_text(json.dumps(entries, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(entries)} checksums for {root.name}")


if __name__ == "__main__":
    main()
