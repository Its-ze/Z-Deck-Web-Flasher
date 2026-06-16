# Z-Deck 0.2.37-cyberdeck Firmware Package

Public-safe LilyGO T-Deck/T-Deck Plus firmware package.

- Firmware version: `2.8.0.zdeck38`
- Pack version: `0.2.37-cyberdeck`
- Hardware: `T_DECK` / `t-deck-tft`
- Build: `20260616-zdeck38-sd-backup-restore-hotfix-t-deck-tft`
- Update mode: `app-only` for Wi-Fi OTA after an initial USB install

## Files

- `bootloader.bin` at `0x0`
- `partitions.bin` at `0x8000`
- `boot_app0.bin` at `0xe000`
- `zdeck-firmware.bin` at `0x10000` and `0x650000`
- `zdeck-littlefs.bin` at `0xc90000`

## Production Readiness Update

This build fixes SD settings backup and restore by decoding `/zdeck/backups/preferences.proto` using the actual SD file size instead of the maximum protobuf size. That also fixes the post-write verification step that made `BACKUP SD` report failure after creating a valid file.

It keeps the duplicate found-device cleanup, selectable on-device themes, GPS/MAP coordinate label, real compass/radar/alert position pages, compact map options overlay, GPS/map recovery, visible Settings OTA, Wi-Fi scan/select, newest-first chats, stable node names, clearer send status, hop counters, Modern Field UI, battery/header fixes, sidebar gutter fixes, home RX overlap fixes, diagnostics, and app-only OTA preservation.

The app-only OTA path preserves Meshtastic settings, owner identity, channels, keys, SD files, chats, map defaults, and sidebar placement. APPLY writes a private settings backup to `/zdeck/backups/preferences.proto` before downloading firmware.