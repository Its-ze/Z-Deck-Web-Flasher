# Z-Deck 0.2.14-public

Public T-Deck firmware package for the Z-Deck web flasher.

Base version: 2.8.0.zdeck15
Pack label: 0.2.14-public
Target: t-deck-tft
Build export: 20260605-zdeck15-t-deck-tft

This folder contains the Z-Deck public firmware image for the 0.2.14 release.

## Changes

- Fixes the physical T-Deck home screen row-wrap regression by reserving a full row slot for the LoRa RX status label, preventing the next icon from overlapping that area.
- Keeps the LoRa RX text compact with clipped status text, smaller label font, and a short idle/readout line inside the reserved row.
- Keeps selectable map/position pages for Mesh map, Live compass, DF/Radar, and Distance alert, with the selected page saved as the default map style.
- Keeps SD/offline map folder preparation, newest-first chat pickers, improved node-name fallbacks, and clearer send status from the previous public build.
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

Source patches are stored in source/patches/2026-06-05-zdeck15-public/.
