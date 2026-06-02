# Z-Deck 0.2.11-public

Public T-Deck firmware package for the Z-Deck web flasher.

Base version: 2.8.0.zdeck12
Pack label: 0.2.11-public
Target: t-deck-tft
Build export: 20260602-073938-t-deck-tft

This folder contains the Z-Deck public firmware image for the 0.2.11 release.

## Changes

- Fixes the physical T-Deck home screen layout so the RX status stays inside the signal/status block and does not overlap the front-page icons.
- Keeps the public default channel fallback that shows LongFast instead of unset when the channel name is empty.
- Keeps the app-only System > Updates menu for Wi-Fi update checks and applies.
- Applies app-only OTA updates with Arduino Update, leaving NVS config, Meshtastic channels, keys, owner settings, and SD-card chat history in place.
- Keeps the Modern Field UI, SD setup detection/progress fixes, boot progress fix, public LongFast defaults, and disabled USB SD mass storage from 0.2.10.

## Files

- bootloader.bin
- partitions.bin
- boot_app0.bin
- zdeck-firmware.bin
- zdeck-factory.bin
- zdeck-littlefs.bin
- zdeck-meshtastic-metadata.json
- SHA256SUMS.json

Source patches are stored in source/patches/2026-06-02-zdeck12-public/.
