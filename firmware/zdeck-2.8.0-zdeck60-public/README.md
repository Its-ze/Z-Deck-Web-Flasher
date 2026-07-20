# zdeck60 Public Release

Z-Deck release with a dedicated Bluetooth control/status page and corrected Bluetooth-enabled normal boot. Z-Deck remains active unless the user explicitly confirms a two-press MeshCore switch.

- Firmware: `2.8.0.zdeck60`
- Pack: `0.2.59-cyberdeck`
- Apps: 26 across two 4x4 launcher pages
- Bluetooth: status, enable/disable, pairing, and app-return controls
- Boot: enabled Bluetooth no longer enters USB programming mode
- Mesh Networks: `ADVICE ONLY`, `STAY ZD`, map, channels, and guarded `MESHCORE >`
- No automatic firmware or protocol switching
- OTA A: `0x10000`, 5 MB
- OTA B: `0x510000`, 5 MB
- Dedicated MeshCore: `0xa10000`, 2.5 MB
- NVS and LittleFS offsets remain unchanged

All Z-Deck maps, chats, settings, GPS, OTA, SD, and diagnostics remain available without switching firmware.
