# Z-Deck 0.2.37-cyberdeck Source Patch Archive

This folder contains the public-safe patch stack used to build `2.8.0.zdeck38` / `0.2.37-cyberdeck` from Meshtastic firmware `2.8`.

The zdeck38 change fixes SD settings backup/restore by decoding `/zdeck/backups/preferences.proto` with the actual SD file size and by rejecting empty or oversized backup files. It does not bundle private channels, PSKs, admin keys, Wi-Fi passwords, or user settings.

The full source patch is included as `zdeck-full-source.patch` and `meshtastic-firmware-src.patch` for traceability.