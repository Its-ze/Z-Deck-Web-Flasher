# Compatibility

## Tested / Targeted

- LILYGO T-Deck / T-Deck Plus class devices
- ESP32-S3
- Meshtastic PlatformIO environment: `t-deck-tft`
- 16MB flash layout
- Browser flashing from Chrome or Edge through Web Serial

## Expected But Not Fully Certified

- T-Deck variants close to the upstream Meshtastic `t-deck-tft` target
- SD-card use for map tiles and the Z-Deck message journal

## Not Supported By This Build

- Non-T-Deck ESP32 boards
- Devices that use a different display, partition table, or GPS wiring
- Firmware that needs a different Meshtastic PlatformIO target

If your board is not a T-Deck/T-Deck Plus, do not flash this build.
