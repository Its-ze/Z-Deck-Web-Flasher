# zdeck62 Public Release

Z-Deck battery-status correctness release for the MeshOS-inspired launcher.

- Firmware: `2.8.0.zdeck62`
- Pack: `0.2.61-cyberdeck`
- Launcher: three pages of 4x2 applications plus the persistent dock
- Battery header: shows a bounded `BAT n%` value after valid telemetry
- Startup battery state: shows `BAT --` instead of a false `0%`
- Dashboard and always-on display use the same validated battery state
- OTA A: `0x10000`, 5 MB
- OTA B: `0x510000`, 5 MB
- Dedicated MeshCore: `0xa10000`, 2.5 MB
- NVS and LittleFS offsets remain unchanged

The app-only OTA payload does not write NVS, LittleFS, SD, channels, keys, chats, owner settings, or UI preferences.
