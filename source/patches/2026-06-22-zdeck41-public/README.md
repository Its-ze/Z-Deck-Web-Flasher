# Z-Deck 0.2.40-cyberdeck Source Patch Archive

This folder contains the public-safe patch stack used to build `2.8.0.zdeck41` / `0.2.40-cyberdeck` from Meshtastic firmware `2.8`.

The zdeck41 change adds verified USB serial debug commands for Z-Deck status, SD backup, OTA check, and OTA apply, plus a host helper that filters output to Z-Deck diagnostics by default. It also keeps the SD backup/restore guardrails from zdeck38 and does not bundle private channels, PSKs, admin keys, Wi-Fi passwords, or user settings.

The full source patch is included as `zdeck-full-source.patch` and `meshtastic-firmware-src.patch` for traceability.
