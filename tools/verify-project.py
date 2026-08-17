#!/usr/bin/env python3
"""Verify the canonical Z-Deck source, release, and Pages contract."""

from __future__ import annotations

import hashlib
import json
import pathlib
import sys


def load(path: pathlib.Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def main() -> int:
    root = pathlib.Path(__file__).resolve().parent.parent
    failures: list[str] = []

    def check(condition: bool, message: str) -> None:
        print(f"{'OK:  ' if condition else 'FAIL:'} {message}")
        if not condition:
            failures.append(message)

    project = load(root / "project.json")
    ota = load(root / "update-ota.json")["latest"]
    legacy = load(root / "update.json")["latest"]
    patch_manifest = load(root / "source/patches/patch-manifest.json")
    release = project["release"]

    for field in ("packVersion", "firmwareVersion"):
        check(ota[field] == release[field], f"OTA {field} matches project.json")
        check(legacy[field] == release[field], f"migration {field} matches project.json")

    payload_path = root / ota["firmware"]["path"]
    check(payload_path.is_file(), "current OTA payload exists")
    if payload_path.is_file():
        payload = payload_path.read_bytes()
        check(len(payload) == ota["firmware"]["size"], "current OTA size matches")
        check(hashlib.sha256(payload).hexdigest() == ota["firmware"]["sha256"], "current OTA SHA256 matches")
        check(hashlib.md5(payload).hexdigest() == ota["firmware"]["md5"], "current OTA MD5 matches")

    expected_dirs = {
        pathlib.Path(release["artifactFolder"]).name,
        pathlib.Path(project["supportArtifacts"]["migration"]).name,
        pathlib.Path(project["supportArtifacts"]["meshCore"]).name,
    }
    actual_dirs = {path.name for path in (root / "firmware").iterdir() if path.is_dir()}
    check(actual_dirs == expected_dirs, "firmware tree contains only current, migration, and MeshCore artifacts")
    for firmware_dir in sorted((root / "firmware").iterdir()):
        if not firmware_dir.is_dir():
            continue
        checksum_path = firmware_dir / "SHA256SUMS.json"
        check(checksum_path.is_file(), f"{firmware_dir.name} has a checksum manifest")
        if not checksum_path.is_file():
            continue
        for entry in load(checksum_path):
            artifact = firmware_dir / entry["name"]
            valid = artifact.is_file()
            if valid:
                data = artifact.read_bytes()
                valid = len(data) == int(entry["length"]) and hashlib.sha256(data).hexdigest() == entry["sha256"]
            check(valid, f"checksum matches: {firmware_dir.name}/{entry['name']}")

    patches_dir = root / "source/patches"
    expected_patches = set(patch_manifest["patchFiles"])
    actual_patches = {path.name for path in patches_dir.glob("*.patch")}
    check(actual_patches == expected_patches, "patch tree contains only three canonical patches")
    archive_dirs = [path.name for path in patches_dir.iterdir() if path.is_dir()]
    check(not archive_dirs, "dated patch archives are removed from the active tree")

    full_patch = (patches_dir / "zdeck-full-source.patch").read_text(encoding="utf-8", errors="replace")
    embedded_ui_patches = [line for line in full_patch.splitlines() if line.startswith("diff --git a/itsz/device-ui-")]
    check(embedded_ui_patches == ["diff --git a/itsz/device-ui-zdeck.patch b/itsz/device-ui-zdeck.patch"],
          "full source patch embeds one consolidated Device UI patch")
    check("ZDeckUpdatePolicy.cpp" in full_patch, "full source patch includes OTA integrity policy")
    check("apply_legacy_itsz_device_ui_patch_chain" not in full_patch, "legacy patch-chain code is absent")

    readme = (root / "README.md").read_text(encoding="utf-8")
    source_doc = (root / "SOURCE.md").read_text(encoding="utf-8")
    check("4x4" not in readme, "README describes the current six-button home")
    check(project["firmware"]["commit"] in source_doc, "SOURCE.md records the pinned firmware commit")
    check(project["deviceUi"]["commit"] in source_doc, "SOURCE.md records the pinned Device UI commit")

    if failures:
        print(f"\n{len(failures)} project verification check(s) failed.")
        return 1
    print("\nZ-Deck project contract passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
