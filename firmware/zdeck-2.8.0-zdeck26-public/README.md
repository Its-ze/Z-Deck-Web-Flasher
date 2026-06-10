# Z-Deck 0.2.25-cyberdeck Firmware Package

Public-safe LilyGO T-Deck/T-Deck Plus firmware package for Z-Deck.

- Firmware version: `2.8.0.zdeck26`
- Pack version: `0.2.25-cyberdeck`
- Target: `t-deck-tft` / ESP32-S3 / 16 MB flash
- Build: `20260610-zdeck26-sidebar-gutter-cyberdeck-t-deck-tft`

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

This build fixes the T-Deck right-side sidebar/header overlap by reserving a fixed sidebar gutter, moving top panels into the content area, and including setup/search/neighbors/LoRa TX headers in sidebar placement. It keeps the zdeck25 map UI, Wi-Fi scan/select setup, app-only Wi-Fi OTA updates, SD settings backup/restore, SD chat journal, newest-first chats, stable node names, send status, hop counters, public-safe labels, and disabled USB SD mass storage.

No private channel URLs, private PSKs, admin keys, or owner-specific settings are bundled.
