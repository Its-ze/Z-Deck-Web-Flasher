# Z-Deck 0.2.5-public

Build date: 2026-06-01
Base version: `2.8.0.zdeck6`
PlatformIO environment: `t-deck-tft`
Hardware: LilyGO T-Deck / T-Deck Plus

This folder contains the normal Z-Deck public firmware image for the 0.2.5 release.

Changes from 0.2.4-public:

- Forces the T-Deck LoRa region default to `US` so LongFast does not fall back to an unset region after setup.
- Keeps the previous Z-Deck public stack: classic UI, LongFast defaults, USB serial recovery, disabled USB mass storage, SD tools/history/ringtones, popup controls, boot progress, map/status/delivery work, and sound-off setup compatibility.

Files:

- `zdeck-factory.bin`: combined flash image.
- `zdeck-firmware.bin`: app partition image flashed at `0x10000` and backup slot `0x650000`.
- `zdeck-littlefs.bin`: LittleFS image.
- `bootloader.bin`, `boot_app0.bin`, `partitions.bin`: support images for full flashing.
- `zdeck-meshtastic-metadata.json`: Meshtastic metadata from the build with Z-Deck pack fields.
- `SHA256SUMS.json`: hashes for verification.

Source patches are stored in `source/patches/2026-06-01-zdeck6-public/`.
