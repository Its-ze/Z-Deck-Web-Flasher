# Z-Deck 0.2.24-cyberdeck

Base version: 2.8.0.zdeck25
Pack label: 0.2.24-cyberdeck
Build export: 20260610-zdeck25-map-ui-cyberdeck-t-deck-tft

This folder contains the public-safe Z-Deck firmware image for the zdeck25 T-Deck release.

## Files

- bootloader.bin
- partitions.bin
- boot_app0.bin
- zdeck-firmware.bin
- zdeck-factory.bin
- zdeck-littlefs.bin
- zdeck-meshtastic-metadata.json
- SHA256SUMS.json

## Highlights

- Makes the map view more usable on the physical 320 x 240 T-Deck screen with a tighter menu and status overlay.
- Adds persistent default selection for Mesh map, Live compass, DF/Radar, and Distance alert pages.
- Tracks tile slots, loaded tiles, and missing tiles so the map reports actual progress instead of staying ambiguous.
- Keeps the real SD tile style on the mesh tile set while page switching changes only the UI overlay mode.
- Keeps sidebar placement, on-device Wi-Fi scan/select, app-only Wi-Fi OTA updates, SD settings backup/restore, SD chat history, newest-first chats, stable node names, send status, hop counters, Modern Field UI, home RX overlap fixes, and disabled USB SD mass storage.
- Public package contains no private channels, PSKs, channel URLs, private keys, Wi-Fi credentials, or admin keys.

Source patches are stored in source/patches/2026-06-10-zdeck25-public/.
