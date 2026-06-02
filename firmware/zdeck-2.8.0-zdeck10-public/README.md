# Z-Deck 0.2.9-public

Public T-Deck firmware package for the Z-Deck web flasher.

Base version: `2.8.0.zdeck10`
Pack label: `0.2.9-public`
Target: `t-deck-tft`
Build export: `20260601-221536-t-deck-tft`

This folder contains the Z-Deck public firmware image for the 0.2.9 release.

## Changes

- Adds an on-device `System > Updates` menu with `Check for Updates`, `Apply Update`, and `Update Status`.
- Checks the hosted `update.json` manifest over Wi-Fi and downloads the app firmware directly on the T-Deck.
- Applies app-only OTA updates with Arduino `Update`, leaving NVS config, Meshtastic channels, keys, owner settings, and SD-card chat history in place.
- Rejects hosted updates that do not declare `updateMode: app-only`.
- Keeps the Modern Field UI, SD setup detection/progress fixes, boot progress fix, public LongFast defaults, and disabled USB SD mass storage from 0.2.8.

## Files

- `bootloader.bin`
- `partitions.bin`
- `boot_app0.bin`
- `zdeck-firmware.bin`
- `zdeck-factory.bin`
- `zdeck-littlefs.bin`
- `zdeck-meshtastic-metadata.json`
- `SHA256SUMS.json`

Source patches are stored in `source/patches/2026-06-02-zdeck10-public/`.
