# Z-Deck 0.2.35-cyberdeck Firmware Package

Public-safe LilyGO T-Deck/T-Deck Plus firmware package.

- Firmware version: `2.8.0.zdeck36`
- Pack version: `0.2.35-cyberdeck`
- Hardware: `T_DECK` / `t-deck-tft`
- Build: `20260613-zdeck36-production-themes-t-deck-tft`
- Update mode: `app-only` for Wi-Fi OTA after an initial USB install

## Files

- `bootloader.bin` at `0x0`
- `partitions.bin` at `0x8000`
- `boot_app0.bin` at `0xe000`
- `zdeck-firmware.bin` at `0x10000` and `0x650000`
- `zdeck-littlefs.bin` at `0xc90000`

## Production Readiness Update

This build adds three more selectable on-device screen themes: `Amber Terminal`, `Slate Signal`, and `Arctic High`. The themes use stable persisted IDs so existing saved theme selections continue to resolve correctly.

It keeps the GPS/MAP coordinate label, real compass/radar/alert position pages, compact map options overlay, GPS/map recovery, visible Settings OTA, Wi-Fi scan/select, SD backup/restore, newest-first chats, stable node names, clearer send status, hop counters, Modern Field UI, battery/header fixes, sidebar gutter fixes, home RX overlap fixes, diagnostics, and app-only OTA preservation.

The app-only OTA path preserves Meshtastic settings, owner identity, channels, keys, SD files, chats, map defaults, and sidebar placement. APPLY writes a private settings backup to `/zdeck/backups/preferences.proto` before downloading firmware.
