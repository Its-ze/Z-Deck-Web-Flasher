# Z-Deck 0.2.19-public

Base version: 2.8.0.zdeck20
Pack label: 0.2.19-public
Target: t-deck-tft
Build export: 20260607-zdeck20-t-deck-tft
Generated from: F:\Dropbox\Dev Ops\T-Deck\firmware\builds\20260607-110130-t-deck-tft

This folder contains the Z-Deck public firmware image for the 0.2.19 release.

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

- Adds a `CENTER` control to the physical T-Deck map menu.
- Automatically recenters the map when the first GPS fix or positioned mesh node arrives after the map was opened.
- Keeps manual pan, zoom, and home actions from being overridden by later auto-centering.
- Keeps the zdeck19 map page/tile-style separation, stable SD tile loading, and compact map status overlay.
- Keeps Home Action and System Z-Deck Updates, app-only Wi-Fi updates, SD settings backup verification, fresh GPS startup defaults, newest-first chats, clearer send status, and disabled USB SD mass storage.

Privacy warning:

- `/zdeck/backups/preferences.proto` contains Meshtastic config, module config, channels/PSKs, owner data, and security keys. Treat the SD card as private.
- No private channel data, PSKs, channel URLs, private keys, or admin keys are bundled in this public firmware folder.

Source patches are stored in source/patches/2026-06-07-zdeck20-public/.
