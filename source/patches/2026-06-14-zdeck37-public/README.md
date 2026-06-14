# Z-Deck 0.2.36-cyberdeck Source Patch Archive

This folder contains the public-safe patch stack used to build `2.8.0.zdeck37` / `0.2.36-cyberdeck` from Meshtastic firmware `2.8`.

The zdeck37 change fixes duplicate found-device entries by deduping repeated NodeDB records in the node list, message destination picker, and favorite-node pages. It does not bundle private channels, PSKs, admin keys, Wi-Fi passwords, or user settings.

The full source patch is included as `zdeck-full-source.patch` and `meshtastic-firmware-src.patch` for traceability.
