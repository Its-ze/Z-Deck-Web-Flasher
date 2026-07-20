# zdeck63 Public Release

Z-Deck startup recovery and launcher readability release.

- Firmware: `2.8.0.zdeck63`
- Pack: `0.2.62-cyberdeck`
- Startup: explicitly leaves the boot splash and loads the 4x2 launcher
- Restore status: clears after 15 seconds even if SD restore cannot finish
- Launcher: grouped colors, stronger tile contrast, and outlined icon badges
- OTA A: `0x10000`, 5 MB
- OTA B: `0x510000`, 5 MB
- Dedicated MeshCore: `0xa10000`, 2.5 MB
- NVS and LittleFS offsets remain unchanged

The app-only OTA payload does not write NVS, LittleFS, SD, channels, keys, chats, owner settings, or UI preferences.
