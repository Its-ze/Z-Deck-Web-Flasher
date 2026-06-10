# Z-Deck 0.2.23-cyberdeck

Base version: 2.8.0.zdeck24
Pack label: 0.2.23-cyberdeck
Build export: 20260609-zdeck24-sidebar-right-cyberdeck-t-deck-tft

This folder contains the public-safe Z-Deck firmware image for the zdeck24 T-Deck release.

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

- Adds a System setting for sidebar placement with right-side default.
- Persists sidebar placement in the device UI filesystem at `/zdeck_sidebar.cfg`.
- Keeps on-device Wi-Fi scan/select, app-only Wi-Fi OTA updates, SD settings backup/restore, SD chat history, map page switching, newest-first chats, stable node names, send status, and hop counter work.
- Public package contains no private channels, PSKs, channel URLs, private keys, Wi-Fi credentials, or admin keys.

Source patches are stored in source/patches/2026-06-09-zdeck24-public/.

