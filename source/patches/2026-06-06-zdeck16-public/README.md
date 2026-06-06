# Z-Deck 0.2.15-public source patch archive

Release: Z-Deck 0.2.15-public
Firmware identity: 2.8.0.zdeck16
Build export: 20260606-zdeck16-t-deck-tft
Patch base: meshtastic/firmware origin/2.8

This archive contains the public, non-secret patch stack used to build the bundled T-Deck firmware.

No private Meshtastic channels, PSKs, channel URLs, admin keys, private keys, owner-specific settings, or private setup data are included.

Highlights:

- Adds SD settings backup and restore under System > Updates.
- Apply Update writes and verifies `/zdeck/backups/preferences.proto` before downloading firmware.
- The backup file contains Meshtastic config, module config, channels/PSKs, owner data, and security keys; treat the SD card as private.
- Keeps saved map page defaults for Mesh map, Live compass, DF/Radar, and Distance alert.
- Keeps SD/offline map folder prep for `/maps/zdeck-*` and map status text that does not stay stuck on loading.
- Keeps newest-first chat pickers, stable node-name fallbacks, clearer broadcast/direct send status, and the home RX overlap fix.

`zdeck-full-source.patch` is the combined firmware patch. The `device-ui-*.patch` files show the layered device-ui changes.
