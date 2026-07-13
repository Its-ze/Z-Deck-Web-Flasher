# zdeck56 Public Release

Current Z-Deck release with an integrated 4x4 launcher, Z-Deck dashboard, Mesh Networks hub, cached MeshCore validation, strict GPS quality filtering, and nonblocking OTA/SD actions.

- Firmware: `2.8.0.zdeck56`
- Pack: `0.2.55-cyberdeck`
- Dashboard: live network, nearby-node, RX-age, GPS, battery, SD, and MeshCore readiness status
- Mesh Networks: area recommendation and guarded switch to the dedicated MeshCore partition
- OTA A: `0x10000`, 5 MB
- OTA B: `0x510000`, 5 MB
- Dedicated MeshCore: `0xa10000`, 2.5 MB
- NVS and LittleFS offsets remain unchanged

App-only OTA writes only the inactive Z-Deck A/B slot. Use the dual-system USB installer once when the device reports `USB INSTALL NEEDED` or `No MeshCore loaded`.
