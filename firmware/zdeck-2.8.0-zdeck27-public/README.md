# Z-Deck 0.2.26-cyberdeck Firmware Package

Public-safe LilyGO T-Deck/T-Deck Plus firmware package for Z-Deck.

- Firmware version: `2.8.0.zdeck27`
- Pack version: `0.2.26-cyberdeck`
- Target: `t-deck-tft` / ESP32-S3 / 16 MB flash
- Build: `20260610-zdeck27-owner-home-title-cyberdeck-t-deck-tft`

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

This build fixes the T-Deck home header that made every CyberDeck build look like the same device by showing the configured Meshtastic owner name, clipped to stay clear of the top status area. It keeps the zdeck26 fixed sidebar gutter, safe top-panel placement, map UI, Wi-Fi scan/select setup, app-only Wi-Fi OTA updates, SD settings backup/restore, SD chat journal, newest-first chats, stable node names, send status, hop counters, public-safe labels, and disabled USB SD mass storage.

No private channel URLs, private PSKs, admin keys, or owner-specific settings are bundled.
