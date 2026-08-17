# Source And Attribution

Z-Deck is GPLv3 firmware derived from Meshtastic for the LILYGO T-Deck/T-Deck Plus.

- Firmware upstream: https://github.com/meshtastic/firmware
- Pinned firmware commit: `35b0590408faddfa933edec3dafd915e714f05b1`
- Device UI upstream: https://github.com/meshtastic/device-ui
- Pinned Device UI commit: `4bf593a82100b911ff816dddf7158ffdee2114cd`
- Target environment: `t-deck-tft`
- Canonical build metadata: [`project.json`](project.json)
- License: GNU GPL v3.0, included in [LICENSE](LICENSE)

The optional dual-system package also contains a MeshCore companion-radio image from https://github.com/meshcore-dev/MeshCore under its MIT license. Its local return-page change is published separately.

## Canonical Patches

Only three source patches are maintained:

- `zdeck-full-source.patch`: complete Z-Deck delta from the pinned Meshtastic commit.
- `device-ui-zdeck.patch`: complete UI delta from the pinned Device UI commit; embedded by the full patch for builds.
- `meshcore-zdeck-return.patch`: optional MeshCore return-page change.

Historical patch chains and old binary folders remain available through Git history. They are not part of the current Pages tree or build contract.

## Rebuild

From WSL or Linux:

```bash
./tools/build-zdeck-wsl.sh
```

The script fetches the exact upstream commit from `project.json`, applies the full patch, runs all Z-Deck policy tests, builds the app and LittleFS, regenerates Meshtastic metadata, and refreshes app/filesystem hashes. It does not read or write a connected device.

Before publishing, run:

```bash
python3 tools/verify-project.py
python3 tools/verify-ota-release.py
python3 tools/verify-dual-release.py
```
