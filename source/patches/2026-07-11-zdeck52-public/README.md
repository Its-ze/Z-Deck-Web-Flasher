# Z-Deck 0.2.51-cyberdeck Public Source Patch Archive

Public-safe source patch archive for firmware `2.8.0.zdeck52` / pack `0.2.51-cyberdeck`.

This release adds a fast validated handoff between Z-Deck/Meshtastic in app 0 and MeshCore in app 1. Z-Deck exposes `MESH >` on Home and `MESHCORE >` in Settings. MeshCore exposes a Z-Deck page and validates that app 0's firmware version contains `zdeck` before selecting it. Each handoff changes the boot partition and performs a short reboot; it does not reflash or erase NVS, LittleFS, or SD storage.

No private channel URLs, PSKs, admin keys, Wi-Fi passwords, owner-specific settings, raw backups, or user device configurations are bundled.
