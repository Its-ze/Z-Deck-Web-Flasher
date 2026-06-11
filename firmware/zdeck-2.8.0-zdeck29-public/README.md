# Z-Deck 0.2.28-cyberdeck Firmware Package

Public-safe LilyGO T-Deck/T-Deck Plus firmware package for Z-Deck.

- Firmware version: `2.8.0.zdeck29`
- Pack version: `0.2.28-cyberdeck`
- Target: `t-deck-tft` / ESP32-S3 / 16 MB flash
- Build: `20260610-zdeck29-ota-controls-t-deck-tft`

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

This build exposes OTA on the physical T-Deck Settings screen. Scroll to the `Z-Deck OTA` block to use `CHECK`, `APPLY`, `STATUS`, `BACKUP SD`, and guarded `RESTORE SD` controls with a live status readout.

It keeps the battery-safe header, fixed sidebar gutter, safe top-panel placement, map UI, Wi-Fi scan/select setup, app-only Wi-Fi OTA updates, SD settings backup/restore, SD chat journal, newest-first chats, stable node names, send status, hop counters, public-safe labels, and disabled USB SD mass storage.

No private channel URLs, private PSKs, admin keys, or owner-specific settings are bundled.
