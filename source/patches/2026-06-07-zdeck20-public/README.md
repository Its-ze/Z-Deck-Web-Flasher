# Z-Deck 0.2.19-public source patch archive

Release: Z-Deck 0.2.19-public
Firmware identity: 2.8.0.zdeck20
Build export: 20260607-zdeck20-t-deck-tft

This archive contains the public source patch stack used to build the packaged Z-Deck firmware.

Apply `zdeck-full-source.patch` to upstream Meshtastic firmware `2.8`, then provide the `device-ui-*.patch` files under the firmware tree's `itsz/` directory before building `env:t-deck-tft`.

Highlights in this release:

- Adds `device-ui-map-autocenter.patch` for the physical T-Deck map.
- Adds a `CENTER` map menu control that centers on GPS, saved map area, or positioned mesh nodes.
- Automatically recenters once when GPS or mesh node coordinates arrive after the map was opened on the default world view.
- Keeps manual pan/zoom/home actions authoritative so later fixes do not pull the map away.
- Keeps zdeck19 page switching separate from the real SD tile style.
- Ships no private channel data, PSKs, channel URLs, private keys, or admin keys.

Public package folder:

`firmware/zdeck-2.8.0-zdeck20-public`
