# Known Issues

- This is beta firmware. Treat it as experimental.
- The current firmware and pack versions are authoritative in `update.json`; the flasher reads those values at runtime.
- The SD-card message journal stores message text locally in plaintext.
- The SD settings backup at `/zdeck/backups/preferences.proto` stores Meshtastic config, channels/PSKs, owner data, and security keys locally in plaintext.
- SD-card behavior depends on the card mounting correctly at runtime.
- USB SD mass storage is disabled because the CDC serial + MSC composite path was unstable on Windows during API sessions.
- The on-device updater requires Wi-Fi to be configured and connected before checking or applying updates; the active control is visible under `Settings > Z-Deck OTA`, and the Wi-Fi popup now has Scan and network-select controls for visible networks.
- If the right sidebar, battery icon, top bar, OTA controls, map overlay, compass pages, duplicate-device list, theme list, or SD backup/restore path still looks wrong after an update, compare the on-device version with `update.json`; an older app slot can still boot after an incomplete flash.
- Avoid editing the same SD-card files from the host computer and the T-Deck UI at the same time.
- GPS, map, and compass behavior still depends on sky view, valid GPS wiring, positioned peer nodes, and available/cached map tiles. The current build keeps GPS active on supported fresh T-Deck installs, separates map page selection from tile style, reports missing tiles, labels coordinate sources, prioritizes live GPS and positioned nodes, and renders dedicated compass/radar/alert pages.
- The browser flasher requires Chrome or Edge with Web Serial support.
- Private Meshtastic channels, PSKs, admin keys, channel URLs, and personal config are not included.
- A clean public-site flash should be tested on each hardware variant before treating it as broadly stable.
