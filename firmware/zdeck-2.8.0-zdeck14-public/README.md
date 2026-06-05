# Z-Deck 0.2.13-public

Public T-Deck firmware package for the Z-Deck web flasher.

Base version: 2.8.0.zdeck14
Pack label: 0.2.13-public
Target: t-deck-tft
Build export: 20260605-zdeck14-t-deck-tft

This folder contains the Z-Deck public firmware image for the 0.2.13 release.

## Changes

- Fixes the T-Deck home screen receive status so the LoRa RX label stays in a fixed clipped slot and no longer overlaps neighboring front-page icons.
- Adds selectable map/position pages for Mesh map, Live compass, DF/Radar, and Distance alert, with the selected page saved as the default map style.
- Keeps the map screen useful without Wi-Fi by showing SD/offline-ready status instead of a permanent loading message and by preparing `/maps/zdeck-*` folders on SD cards.
- Orders group and direct chat thread pickers by newest activity first.
- Improves node display names by avoiding `??` and `?? ??` placeholders when long/short names are missing.
- Clarifies channel broadcast send status as sent with TTL instead of incorrectly showing no ACK, while keeping direct-message ACK/no-response status.
- Keeps app-only Wi-Fi updates, Modern Field UI, SD setup progress/readouts, public LongFast defaults, and disabled USB SD mass storage from prior public builds.

## Files

- bootloader.bin
- partitions.bin
- boot_app0.bin
- zdeck-firmware.bin
- zdeck-factory.bin
- zdeck-littlefs.bin
- zdeck-meshtastic-metadata.json
- SHA256SUMS.json

Source patches are stored in source/patches/2026-06-05-zdeck14-public/.
