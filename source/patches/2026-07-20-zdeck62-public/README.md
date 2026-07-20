# Z-Deck zdeck62 source patches

Reproducible source patches for firmware `2.8.0.zdeck62` / pack `0.2.61-cyberdeck`.

- `device-ui-blackberry-shell.patch` is the Device UI delta for the 4x2 paged launcher and battery-status fix.
- `zdeck-full-source.patch` is the complete firmware delta against pinned Meshtastic firmware commit `35b0590408faddfa933edec3dafd915e714f05b1`.

The clean WSL build applies `zdeck-full-source.patch` and builds `t-deck-tft` firmware plus LittleFS. Public source contains no private channels, PSKs, private keys, Wi-Fi credentials, or admin credentials.
