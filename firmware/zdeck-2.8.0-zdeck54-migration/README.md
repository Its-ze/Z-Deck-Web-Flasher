# zdeck54 OTA Migration Baseline

This build introduces the dual-slot Z-Deck OTA partition table while preserving the established NVS and LittleFS offsets. Use `manifest-ota-test.json` to install it without writing NVS, LittleFS, or SD, then test the update to zdeck55 from `Settings > Z-Deck OTA`.

- Firmware: `2.8.0.zdeck54`
- Pack: `0.2.53-cyberdeck`
- OTA A: `0x10000`, 5 MB
- OTA B: `0x510000`, 5 MB
- Dedicated MeshCore: `0xa10000`, 2.5 MB
- LittleFS: `0xc90000`, unchanged

Do not publish private configuration or backup files with this package.
