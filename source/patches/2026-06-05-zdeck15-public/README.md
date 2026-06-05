# Z-Deck 0.2.14-public source patch archive

Release: Z-Deck 0.2.14-public
Firmware identity: 2.8.0.zdeck15
Build export: 20260605-zdeck15-t-deck-tft
Patch base: meshtastic/firmware origin/2.8

This archive contains the public, non-secret patch stack used to build the bundled T-Deck firmware.

No private Meshtastic channels, PSKs, channel URLs, admin keys, private keys, owner-specific settings, or private setup data are included.

Highlights:

- Restored full-row space for the home LoRa RX status label so LVGL flex row wrapping cannot place the next home icon into the same row.
- Kept the LoRa RX readout compact by clipping the status line inside the reserved row with a smaller font.
- Kept saved map page defaults for Mesh map, Live compass, DF/Radar, and Distance alert.
- Kept SD/offline map folder prep for `/maps/zdeck-*` and map status text that does not stay stuck on loading.
- Kept newest-first chat pickers, stable node-name fallbacks, and clearer broadcast/direct send status.

`zdeck-full-source.patch` is the combined firmware patch. The `device-ui-*.patch` files show the layered device-ui changes.
