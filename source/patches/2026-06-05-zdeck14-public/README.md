# Z-Deck 0.2.13-public source patch archive

Release: Z-Deck 0.2.13-public
Firmware identity: 2.8.0.zdeck14
Build export: 20260605-zdeck14-t-deck-tft
Patch base: meshtastic/firmware origin/2.8

This archive contains the public, non-secret patch stack used to build the bundled T-Deck firmware.

No private Meshtastic channels, PSKs, channel URLs, admin keys, private keys, owner-specific settings, or private setup data are included.

Highlights:

- Fixed clipped home LoRa RX status to prevent front-page icon overlap.
- Added saved map page defaults for Mesh map, Live compass, DF/Radar, and Distance alert.
- Added SD/offline map folder prep for `/maps/zdeck-*` and map status text that does not stay stuck on loading.
- Ordered chat thread pickers by latest activity first.
- Improved node name fallbacks so placeholders like `?? ??` are not shown as names.
- Clarified broadcast send status as sent with TTL while keeping direct-message ACK/no-response status.

`zdeck-full-source.patch` is the combined firmware patch. The `device-ui-*.patch` files show the layered device-ui changes.
