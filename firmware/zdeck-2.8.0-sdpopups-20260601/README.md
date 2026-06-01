# Z-Deck SD Popups Build

Build date: 2026-06-01
Base version: `2.8.0.f9fea56`
PlatformIO environment: `t-deck-tft`
Hardware: LilyGO T-Deck / T-Deck Plus

This folder contains the firmware image that was built and flashed during the SD-card setup / popup-control session.

Files:

- `zdeck-factory.bin`: combined flash image.
- `zdeck-firmware.bin`: app partition image flashed at `0x10000`.
- `zdeck-littlefs.bin`: LittleFS image.
- `bootloader.bin`, `boot_app0.bin`, `partitions.bin`: support images for full flashing.
- `zdeck-meshtastic-metadata.json`: PlatformIO Meshtastic metadata from the build.
- `SHA256SUMS.json`: hashes for verification.

Source patches are stored in `source/patches/2026-06-01-tdeck-sd-popups/`.
