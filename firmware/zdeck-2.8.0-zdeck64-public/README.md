# zdeck64 Public Release

Z-Deck physical-screen launcher contrast release.

- Firmware: `2.8.0.zdeck64`
- Pack: `0.2.63-cyberdeck`
- App icons: larger solid badges with dark high-contrast glyphs
- Tiles: opaque surfaces and visible borders for cleaner grouping
- Palette: restrained grouped accents rather than per-app rainbow colors
- Startup: retains the verified splash-to-launcher recovery
- Restore status: remains bounded to 15 seconds
- OTA A: `0x10000`, 5 MB
- OTA B: `0x510000`, 5 MB
- Dedicated MeshCore: `0xa10000`, 2.5 MB

The app-only OTA payload does not write NVS, LittleFS, SD, channels, keys, chats, owner settings, or UI preferences.
