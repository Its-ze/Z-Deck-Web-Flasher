# Z-Deck 0.2.27-cyberdeck Firmware Package

Public-safe LilyGO T-Deck/T-Deck Plus firmware package for Z-Deck.

- Firmware version: `2.8.0.zdeck28`
- Pack version: `0.2.27-cyberdeck`
- Target: `t-deck-tft` / ESP32-S3 / 16 MB flash
- Build: `20260610-zdeck28-header-battery-safe-t-deck-tft`

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

This build fixes the physical T-Deck header so the battery icon and percent remain visible. The screen title is clipped into the safe lane between the battery/USB block and the right-side status icons, and a real battery keeps showing `100%` instead of collapsing into USB-only status when the charge value reports 101.

It keeps the fixed sidebar gutter, safe top-panel placement, map UI, Wi-Fi scan/select setup, app-only Wi-Fi OTA updates, SD settings backup/restore, SD chat journal, newest-first chats, stable node names, send status, hop counters, public-safe labels, and disabled USB SD mass storage.

No private channel URLs, private PSKs, admin keys, or owner-specific settings are bundled.
