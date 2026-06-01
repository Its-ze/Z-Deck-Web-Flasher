# Z-Deck 0.2.6-public

Build date: 2026-06-01
Base version: `2.8.0.zdeck7`
PlatformIO environment: `t-deck-tft`
Hardware: LilyGO T-Deck / T-Deck Plus

This folder contains the Z-Deck public firmware image for the 0.2.6 release.

Changes from 0.2.5-public:

- Fixes the boot progress bar layout so it renders as a compact foreground bar and does not overlap the boot labels.
- Uses non-animated boot progress updates so early boot status changes are visible reliably.
- Rebuilds from a clean public patch stack and removes a stale LittleFS map fallback include that blocked clean public rebuilds.
- Keeps the 0.2.5 public stack: US LongFast default, classic UI, serial recovery, disabled USB mass storage, SD tools/history/ringtones, popup controls, map/status/delivery improvements, and sound-off setup compatibility.

Files:

- `zdeck-factory.bin`: combined flash image.
- `zdeck-firmware.bin`: app partition image flashed at `0x10000` and backup slot `0x650000`.
- `zdeck-littlefs.bin`: LittleFS image.
- `bootloader.bin`, `boot_app0.bin`, `partitions.bin`: support images for full flashing.
- `zdeck-meshtastic-metadata.json`: Meshtastic metadata from the build with Z-Deck pack fields.
- `SHA256SUMS.json`: hashes for verification.

Source patches are stored in `source/patches/2026-06-01-zdeck7-public/`.