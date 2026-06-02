# Z-Deck 0.2.7-public

Build date: 2026-06-01
Base version: `2.8.0.zdeck8`
PlatformIO environment: `t-deck-tft`
Hardware: LilyGO T-Deck / T-Deck Plus

This folder contains the Z-Deck public firmware image for the 0.2.7 release.

Changes from 0.2.6-public:

- Fixes SD setup detection so a card prepared with the Z-Deck `/zdeck` and `/itsz/history` layout is not treated as new every time it is reinserted.
- Keeps compatibility with cards prepared by the older legacy `/maps`, `/ringtones`, `/messages`, `/backups`, and `/logs` layout.
- Adds visible SD setup progress on the popup and Tools screen while checking, formatting, remounting, and creating folders.
- Keeps the 0.2.6 public stack: corrected boot progress bar, US LongFast default, classic UI, serial recovery, disabled USB mass storage, SD history/ringtones, popup controls, map/status/delivery improvements, and sound-off setup compatibility.

Files:

- `zdeck-factory.bin`: combined flash image.
- `zdeck-firmware.bin`: app partition image flashed at `0x10000` and backup slot `0x650000`.
- `zdeck-littlefs.bin`: LittleFS image.
- `bootloader.bin`, `boot_app0.bin`, `partitions.bin`: support images for full flashing.
- `zdeck-meshtastic-metadata.json`: Meshtastic metadata from the build with Z-Deck pack fields.
- `SHA256SUMS.json`: hashes for verification.

Source patches are stored in `source/patches/2026-06-01-zdeck8-public/`.
