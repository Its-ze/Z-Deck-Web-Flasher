# Known Issues

- This is beta firmware. Treat it as experimental.
- The firmware base reports `2.8.0.zdeck25`; the public-safe release label is `0.2.24-cyberdeck`.
- The SD-card message journal stores message text locally in plaintext.
- The SD settings backup at `/zdeck/backups/preferences.proto` stores Meshtastic config, channels/PSKs, owner data, and security keys locally in plaintext.
- SD-card behavior depends on the card mounting correctly at runtime.
- USB SD mass storage is disabled in `0.2.24-cyberdeck` because the CDC serial + MSC composite path was unstable on Windows during API sessions.
- The on-device updater requires Wi-Fi to be configured and connected before checking or applying updates; the Wi-Fi popup now has Scan and network-select controls for visible networks.
- Avoid editing the same SD-card files from the host computer and the T-Deck UI at the same time.
- GPS and map behavior depends on sky view, valid GPS wiring, and available/cached map tiles. Z-Deck 0.2.24 disables the inherited fresh T-Deck power-saving default so supported GPS receivers stay active, keeps map page switching separate from SD tile style loading, persists the default map page, reports missing tiles, and recenters once when late GPS or node coordinates arrive.
- The browser flasher requires Chrome or Edge with Web Serial support.
- Private Meshtastic channels, PSKs, admin keys, channel URLs, and personal config are not included.
- A clean public-site flash should be tested on each hardware variant before treating it as broadly stable.
