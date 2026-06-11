# Z-Deck 0.2.29-cyberdeck Firmware Package

Public-safe LilyGO T-Deck/T-Deck Plus firmware package for Z-Deck.

- Firmware version: `2.8.0.zdeck30`
- Pack version: `0.2.29-cyberdeck`
- Target: `t-deck-tft` / ESP32-S3 / 16 MB flash
- Build: `20260611-zdeck30-map-gps-recovery-t-deck-tft`

## Included Files

- `bootloader.bin`
- `partitions.bin`
- `boot_app0.bin`
- `zdeck-firmware.bin`
- `zdeck-factory.bin`
- `zdeck-littlefs.bin`
- `zdeck-meshtastic-metadata.json`
- `SHA256SUMS.json`

## Notes

This build improves the physical T-Deck map page so a stale saved map home no longer blocks recovery to the live GPS or located mesh-node area. The map overlay now shows the current GPS coordinates when available, and automatic centering keeps trying until live GPS is usable.

It keeps the visible on-device OTA controls, Wi-Fi scan/select setup, app-only Wi-Fi updates, SD settings backup/restore, SD chat journal, newest-first chats, stable node names, send status, hop counters, public-safe labels, and disabled USB SD mass storage.

No private channel URLs, private PSKs, admin keys, or owner-specific settings are bundled.
