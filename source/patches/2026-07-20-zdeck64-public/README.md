# Z-Deck zdeck64 source patches

Reproducible source patches for firmware `2.8.0.zdeck64` / pack `0.2.63-cyberdeck`.

- `device-ui-blackberry-shell.patch` contains the Device UI launcher, startup handoff, and high-contrast icon treatment.
- `zdeck-full-source.patch` is the complete firmware delta against pinned Meshtastic firmware commit `35b0590408faddfa933edec3dafd915e714f05b1`.

The clean WSL build applies `zdeck-full-source.patch` and builds `t-deck-tft` firmware plus LittleFS. Public source contains no private channels, PSKs, private keys, Wi-Fi credentials, or admin credentials.
