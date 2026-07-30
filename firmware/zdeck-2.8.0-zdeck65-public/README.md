# zdeck65 Public Release

Z-Deck sketch-based home screen release.

- Firmware: `2.8.0.zdeck65`
- Pack: `0.2.64-cyberdeck`
- Header: compact Z-Deck brand, live clock, and validated battery state
- Home: six large controls for Alerts, Map, Messages, Contacts, Tools, and Settings
- Status: one-line mesh, GPS, SD, and unread-message summary
- Navigation: direct routes with no launcher paging or bottom dock
- OTA A: `0x10000`, 5 MB
- OTA B: `0x510000`, 5 MB
- Dedicated MeshCore: `0xa10000`, 2.5 MB

The app-only OTA payload does not write NVS, LittleFS, SD, channels, keys, chats, owner settings, or UI preferences.
