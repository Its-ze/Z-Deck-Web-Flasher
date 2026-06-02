# Z-Deck 0.2.8-public

Build date: 2026-06-01
Base version: `2.8.0.zdeck9`
PlatformIO environment: `t-deck-tft`
Hardware: LilyGO T-Deck / T-Deck Plus

This folder contains the Z-Deck public firmware image for the 0.2.8 release.

Changes from 0.2.7-public:

- Adds the Modern Field dark theme for the on-device T-Deck UI.
- Updates the generated home/status layout with compact modern icon chips, a darker surface palette, and clearer active/inactive status colors.
- Restyles the Tools health panel, SD prepare/reset panel, SD setup popup, nav rail, and boot progress bar to match the new theme.
- Keeps the 0.2.7 SD setup fixes: prepared cards are not treated as new on every insert, and setup/reset operations show visible progress readouts.
- Keeps the public safety defaults: LongFast only, US region default, serial recovery, disabled USB mass storage, SD history/ringtones, popup controls, map/status/delivery improvements, and no private channel material.

Files:

- `zdeck-factory.bin`: combined flash image.
- `zdeck-firmware.bin`: app partition image flashed at `0x10000` and backup slot `0x650000`.
- `zdeck-littlefs.bin`: LittleFS image.
- `bootloader.bin`, `boot_app0.bin`, `partitions.bin`: support images for full flashing.
- `zdeck-meshtastic-metadata.json`: Meshtastic metadata from the build with Z-Deck pack fields.
- `SHA256SUMS.json`: hashes for verification.

Source patches are stored in `source/patches/2026-06-01-zdeck9-public/`.
