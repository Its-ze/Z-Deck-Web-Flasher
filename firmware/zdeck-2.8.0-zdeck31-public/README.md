# Z-Deck 0.2.30-cyberdeck Firmware Package

Public-safe LilyGO T-Deck/T-Deck Plus firmware package.

- Firmware version: `2.8.0.zdeck31`
- Pack version: `0.2.30-cyberdeck`
- Hardware: `T_DECK` / `t-deck-tft`
- Build: `20260611-zdeck31-ota-ui-progress-t-deck-tft`
- Update mode: `app-only` for Wi-Fi OTA after an initial USB install

## Files

- `bootloader.bin` at `0x0`
- `partitions.bin` at `0x8000`
- `boot_app0.bin` at `0xe000`
- `zdeck-firmware.bin` at `0x10000` and `0x650000`
- `zdeck-littlefs.bin` at `0xc90000`

## Hotfix

This build fixes the on-device Z-Deck OTA and SD backup controls so CHECK, APPLY, BACKUP SD, and RESTORE SD release the pressed button and repaint the status readout before long Wi-Fi, flash, or SD work starts. OTA progress also pumps the screen while the firmware image downloads and writes.

The app-only OTA path preserves Meshtastic settings, owner identity, channels, keys, SD files, chats, map defaults, and sidebar placement. APPLY still writes a private settings backup to `/zdeck/backups/preferences.proto` before downloading firmware.
