# Z-Deck 0.2.17-public source patch archive

Release: Z-Deck 0.2.17-public
Firmware identity: 2.8.0.zdeck18
Build export: 20260606-zdeck18-t-deck-tft

This archive contains the public source patch stack used to build the packaged Z-Deck firmware.

Apply `zdeck-full-source.patch` to upstream Meshtastic firmware `2.8`, then provide the `device-ui-*.patch` files under the firmware tree's `itsz/` directory before building `env:t-deck-tft`.

Highlights in this release:

- Adds a visible `Z-Deck Updates` entry directly to the Home Action menu.
- Keeps app-only Wi-Fi updates from `System > Z-Deck Updates`.
- Keeps `Check for Updates`, `Apply Update`, `Backup Settings`, `Restore Settings`, and `Update Status`.
- Fixes fresh T-Deck GPS startup by disabling the inherited T-Deck power-saving default while keeping GPS enabled on RX44/TX43.
- Keeps SD settings backup and restore at `/zdeck/backups/preferences.proto`.
- Keeps saved map pages, SD/offline map folders, newest-first chat pickers, node-name fallback cleanup, clearer send status, and home RX overlap fixes.
- Keeps public LongFast defaults and ships no private channel data, PSKs, channel URLs, private keys, or admin keys.

Public package folder:

`firmware/zdeck-2.8.0-zdeck18-public`
