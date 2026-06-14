# Z-Deck 0.2.36-cyberdeck Firmware Package

Public-safe LilyGO T-Deck/T-Deck Plus firmware package.

- Firmware version: `2.8.0.zdeck37`
- Pack version: `0.2.36-cyberdeck`
- Hardware: `T_DECK` / `t-deck-tft`
- Build: `20260614-zdeck37-ota-test-t-deck-tft`
- Update mode: `app-only` for Wi-Fi OTA after an initial USB install

## Files

- `bootloader.bin` at `0x0`
- `partitions.bin` at `0x8000`
- `boot_app0.bin` at `0xe000`
- `zdeck-firmware.bin` at `0x10000` and `0x650000`
- `zdeck-littlefs.bin` at `0xc90000`

## Production Readiness Update

This build fixes duplicate found-device entries by deduping repeated NodeDB records before the node list, message destination picker, and favorite-node pages render them.

It keeps the selectable on-device themes, GPS/MAP coordinate label, real compass/radar/alert position pages, compact map options overlay, GPS/map recovery, visible Settings OTA, Wi-Fi scan/select, SD backup/restore, newest-first chats, stable node names, clearer send status, hop counters, Modern Field UI, battery/header fixes, sidebar gutter fixes, home RX overlap fixes, diagnostics, and app-only OTA preservation.

The app-only OTA path preserves Meshtastic settings, owner identity, channels, keys, SD files, chats, map defaults, and sidebar placement. APPLY writes a private settings backup to `/zdeck/backups/preferences.proto` before downloading firmware.
