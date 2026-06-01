# Z-Deck 0.2.4-public

Build date: 2026-06-01
Base version: `2.8.0.zdeck5`
PlatformIO environment: `t-deck-tft`
Hardware: LilyGO T-Deck / T-Deck Plus

This folder contains the normal Z-Deck public firmware image for the 0.2.4 release.

Files:

- `zdeck-factory.bin`: combined flash image.
- `zdeck-firmware.bin`: app partition image flashed at `0x10000` and backup slot `0x650000`.
- `zdeck-littlefs.bin`: LittleFS image.
- `bootloader.bin`, `boot_app0.bin`, `partitions.bin`: support images for full flashing.
- `zdeck-meshtastic-metadata.json`: Meshtastic metadata from the build with Z-Deck pack fields.
- `SHA256SUMS.json`: hashes for verification.

Source patches are stored in `source/patches/2026-06-01-zdeck5-public/`.
