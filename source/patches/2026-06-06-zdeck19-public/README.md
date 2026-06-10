# Z-Deck 0.2.18-public source patch archive

Release: Z-Deck 0.2.18-public
Firmware identity: 2.8.0.zdeck19
Build export: 20260606-zdeck19-t-deck-tft

This archive contains the public source patch stack used to build the packaged Z-Deck firmware.

Apply `zdeck-full-source.patch` to upstream Meshtastic firmware `2.8`, then provide the `device-ui-*.patch` files under the firmware tree's `itsz/` directory before building `env:t-deck-tft`.

Highlights in this release:

- Fixes Z-Deck map page switching so page selection no longer changes the Meshtastic tile style.
- Keeps SD/offline tile loading on the real `zdeck-mesh` tile directory and filters non-tile page folders from the map style dropdown.
- Makes the physical T-Deck map workflow easier: pressing Map again cycles views, and the on-screen menu has larger Next View / Remember controls.
- Moves the map status/readiness text to a compact bottom-left overlay instead of a center-blocking loading panel.
- Keeps the visible `Z-Deck Updates` entry directly in the Home Action menu and the nested `System > Z-Deck Updates` entry.
- Keeps app-only Wi-Fi updates, SD settings backup/restore, fresh T-Deck GPS startup defaults, home RX overlap fixes, newest-first chats, node-name fallback cleanup, clearer send status, and public LongFast defaults.
- Ships no private channel data, PSKs, channel URLs, private keys, or admin keys.

Public package folder:

`firmware/zdeck-2.8.0-zdeck19-public`
