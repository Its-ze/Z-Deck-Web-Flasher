# Z-Deck 0.2.18-public

Base version: 2.8.0.zdeck19
Pack label: 0.2.18-public
Target: t-deck-tft
Build export: 20260606-zdeck19-t-deck-tft
Generated from: F:\Dropbox\Dev Ops\T-Deck\firmware\builds\20260606-193551-t-deck-tft

This folder contains the Z-Deck public firmware image for the 0.2.18 release.

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

- Fixes map page switching so Mesh map, Live compass, DF/Radar, and Distance alert no longer overwrite the real map tile style.
- Makes map switching easier: pressing the Map tab while already on the map cycles the Z-Deck page, and the map menu uses larger Next View / Remember controls.
- Keeps SD tile loading pinned to `/maps/zdeck-mesh` by default and filters non-tile Z-Deck page folders out of the tile-style dropdown.
- Moves the map readiness/status readout to a compact bottom-left overlay so it does not block the map.
- Keeps the visible Z-Deck Updates entry directly in the Home Action menu and the nested System > Z-Deck Updates entry.
- Keeps app-only Wi-Fi updates and SD settings backup verification before Apply Update.
- Keeps the fresh T-Deck GPS startup fix, home RX overlap fix, newest-first chat pickers, stable node-name fallbacks, clearer send status, Modern Field UI, public LongFast defaults, and disabled USB SD mass storage.

Privacy warning:

- `/zdeck/backups/preferences.proto` contains Meshtastic config, module config, channels/PSKs, owner data, and security keys. Treat the SD card as private.
- No private channel data, PSKs, channel URLs, private keys, or admin keys are bundled in this public firmware folder.

Source patches are stored in source/patches/2026-06-06-zdeck19-public/.
