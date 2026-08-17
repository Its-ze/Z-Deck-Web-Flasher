# Z-Deck 0.2.66

Public T-Deck/T-Deck Plus firmware for the `t-deck-tft` environment.

- `zdeck-firmware.bin`: app-only A/B OTA payload.
- `zdeck-littlefs.bin`: public filesystem image for a standard USB install.
- `zdeck-factory.bin`: merged recovery image; using it can overwrite more flash than an app-only update.
- `zdeck-meshtastic-metadata.json`: generated build and partition metadata.

Normal OTA updates preserve NVS, LittleFS, SD data, channels, keys, chats, and owner settings. Do not erase flash during a routine update.
