# Z-Deck 0.2.12-public

Public T-Deck firmware package for the Z-Deck web flasher.

Base version: 2.8.0.zdeck13
Pack label: 0.2.12-public
Target: t-deck-tft
Build export: 20260602-zdeck13-t-deck-tft

This folder contains the Z-Deck public firmware image for the 0.2.12 release.

## Changes

- Fixes the T-Deck home screen signal row so the short RX status keeps a full row slot and no longer pushes the next front-page icon into the same line.
- Keeps the public default channel fallback that shows LongFast instead of unset when the channel name is empty.
- Keeps the app-only System > Updates menu for Wi-Fi update checks and applies.
- Applies app-only OTA updates with Arduino Update, leaving NVS config, Meshtastic channels, keys, owner settings, and SD-card chat history in place.
- Keeps the Modern Field UI, SD setup detection/progress fixes, boot progress fix, public LongFast defaults, and disabled USB SD mass storage from 0.2.11.

## Files

- bootloader.bin
- partitions.bin
- boot_app0.bin
- zdeck-firmware.bin
- zdeck-factory.bin
- zdeck-littlefs.bin
- zdeck-meshtastic-metadata.json
- SHA256SUMS.json

Source patches are stored in source/patches/2026-06-02-zdeck13-public/.
