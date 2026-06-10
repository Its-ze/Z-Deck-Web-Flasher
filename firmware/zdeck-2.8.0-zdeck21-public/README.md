# Z-Deck 0.2.20-public

Base version: 2.8.0.zdeck21
Pack label: 0.2.20-public
Build export: 20260607-zdeck21-t-deck-tft

This folder contains the Z-Deck public firmware image for the 0.2.20 release.

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

- Adds on-device WiFi scan/select in the WiFi settings popup.
- Scan lists nearby SSIDs with RSSI and open/locked status.
- Selecting a network fills the SSID field; secured networks then focus the password field.
- Open networks can be saved with an empty password.
- Keeps the zdeck20 map Center and late GPS/node auto-center recovery.

Source patches are stored in source/patches/2026-06-07-zdeck21-public/.