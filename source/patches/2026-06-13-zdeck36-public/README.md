# Z-Deck 0.2.35-cyberdeck Source Patch Archive

This folder contains the public-safe patch stack used to build `2.8.0.zdeck36` / `0.2.35-cyberdeck` from Meshtastic firmware `2.8`.

The zdeck36 change adds three more selectable on-device screen themes: `Amber Terminal`, `Slate Signal`, and `Arctic High`. Existing theme IDs remain stable and saved configs continue to resolve safely.

It keeps the zdeck32-zdeck35 UI and state work: GPS/MAP coordinate labels, real compass/radar/alert position pages, compact map controls, visible Settings OTA with progress repainting, SD backup/restore, Wi-Fi scan/select, persistent map defaults, diagnostics, chat ordering, send status, hop counters, battery/header/sidebar fixes, and app-only OTA preservation.

No private channel data, PSKs, channel URLs, Wi-Fi credentials, admin keys, owner-specific settings, or saved chats are bundled in this public source archive.
