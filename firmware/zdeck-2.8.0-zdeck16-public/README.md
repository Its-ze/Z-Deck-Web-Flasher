# Z-Deck 0.2.15-public

Base version: 2.8.0.zdeck16
Pack label: 0.2.15-public
Target: t-deck-tft
Build export: 20260606-zdeck16-t-deck-tft
Generated from: F:\Dropbox\Dev Ops\T-Deck\firmware\builds\20260606-134431-t-deck-tft

This folder contains the Z-Deck public firmware image for the 0.2.15 release.

Included files:

- bootloader.bin
- partitions.bin
- boot_app0.bin
- zdeck-firmware.bin
- zdeck-factory.bin
- zdeck-littlefs.bin
- zdeck-meshtastic-metadata.json
- SHA256SUMS.json

Release highlights:

- Adds SD settings backup and restore under System > Updates.
- Apply Update writes and verifies `/zdeck/backups/preferences.proto` before downloading firmware.
- Keeps app-only Wi-Fi updates so Meshtastic config, channels, keys, owner settings, and SD files are preserved unless a future manifest declares another update mode.
- Keeps the home RX overlap fix, saved map pages, SD/offline map folders, newest-first chat pickers, stable node-name fallbacks, clearer send status, Modern Field UI, public LongFast defaults, and disabled USB SD mass storage.

Privacy warning:

- `/zdeck/backups/preferences.proto` contains Meshtastic config, module config, channels/PSKs, owner data, and security keys. Treat the SD card as private.
- No private channel data, PSKs, channel URLs, private keys, or admin keys are bundled in this public firmware folder.

Source patches are stored in source/patches/2026-06-06-zdeck16-public/.
