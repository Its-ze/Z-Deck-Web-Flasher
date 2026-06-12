# Z-Deck 0.2.31-cyberdeck Firmware Package

Public-safe LilyGO T-Deck/T-Deck Plus firmware package.

- Firmware version: `2.8.0.zdeck32`
- Pack version: `0.2.31-cyberdeck`
- Hardware: `T_DECK` / `t-deck-tft`
- Build: `20260611-zdeck32-compass-map-menu-t-deck-tft`
- Update mode: `app-only` for Wi-Fi OTA after an initial USB install

## Files

- `bootloader.bin` at `0x0`
- `partitions.bin` at `0x8000`
- `boot_app0.bin` at `0xe000`
- `zdeck-firmware.bin` at `0x10000` and `0x650000`
- `zdeck-littlefs.bin` at `0xc90000`

## Hotfix

This build gives the non-map position pages a real on-device compass/radar/alert panel instead of leaving the map view stuck underneath them. The compass view draws a heading ring, cardinal labels, own-position status, and nearest positioned mesh-node bearing/range when that data is available.

The map options overlay is shorter and tighter so Center, page switching, Wi-Fi/cache status, and GPS text fit on the T-Deck screen without covering the map controls.

The app-only OTA path preserves Meshtastic settings, owner identity, channels, keys, SD files, chats, map defaults, and sidebar placement. APPLY still writes a private settings backup to `/zdeck/backups/preferences.proto` before downloading firmware.
