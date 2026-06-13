# Z-Deck 0.2.34-cyberdeck Source Patch Archive

This folder contains the public-safe patch stack used to build `2.8.0.zdeck35` / `0.2.34-cyberdeck` from Meshtastic firmware `2.8`.

The zdeck35 change updates the map coordinate readout so it says `GPS` when the displayed coordinate is the live centered GPS fix and `MAP` when the coordinate is the manually scrolled map center. This is intended to make apparent map/GPS offsets diagnosable on the device.

It keeps the zdeck32-zdeck34 UI and state work: real compass/radar/alert position pages, compact map controls, visible Settings OTA with progress repainting, SD backup/restore, Wi-Fi scan/select, persistent map defaults, diagnostics, chat ordering, send status, hop counters, battery/header/sidebar fixes, and app-only OTA preservation.
