# zdeck55 Public Release

Current Z-Deck release with strict GPS quality filtering, nonblocking OTA/SD actions, dual-slot A/B updates, and a dedicated MeshCore partition that normal OTA cannot overwrite.

- Firmware: `2.8.0.zdeck55`
- Pack: `0.2.54-cyberdeck`
- GPS gate: fresh 3D fix, at least 5 satellites, HDOP at or below 2.5
- OTA A: `0x10000`, 5 MB
- OTA B: `0x510000`, 5 MB
- Dedicated MeshCore: `0xa10000`, 2.5 MB
- NVS and LittleFS offsets remain unchanged

App-only OTA writes only the inactive Z-Deck A/B slot. Manual SD backup and restore remain separate queued controls.
