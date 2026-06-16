# Known Issues

- This is beta firmware. Treat it as experimental.
- The firmware base reports `2.8.0.zdeck38`; the public-safe release label is `0.2.37-cyberdeck`.
- The SD-card message journal stores message text locally in plaintext.
- The SD settings backup at `/zdeck/backups/preferences.proto` stores Meshtastic config, channels/PSKs, owner data, and security keys locally in plaintext.
- SD-card behavior depends on the card mounting correctly at runtime.
- USB SD mass storage is disabled in `0.2.37-cyberdeck` because the CDC serial + MSC composite path was unstable on Windows during API sessions.
- The on-device updater requires Wi-Fi to be configured and connected before checking or applying updates; the active control is visible under `Settings > Z-Deck OTA`, and the Wi-Fi popup now has Scan and network-select controls for visible networks.
- If the right sidebar, battery icon, top bar, OTA controls, map GPS/MAP overlay, compass pages, map options menu, duplicate found-device list, theme list, or SD backup/restore path still look wrong after an update, confirm the device is actually on `2.8.0.zdeck38`; the SD backup decode hotfix, fixed gutter, bounded header lane, Settings OTA block, map GPS recovery, explicit GPS/MAP coordinate labels, real compass pages, compact map menu, duplicate device filtering, OTA/backup button repaint fix, and Amber Terminal/Slate Signal/Arctic High themes are not present in older zdeck24-zdeck37 builds.
- Avoid editing the same SD-card files from the host computer and the T-Deck UI at the same time.
- GPS, map, and compass behavior depends on sky view, valid GPS wiring, positioned peer nodes, and available/cached map tiles. Z-Deck 0.2.37 keeps the GPS/map recovery behavior and disables the inherited fresh T-Deck power-saving default so supported GPS receivers stay active, keeps map page switching separate from SD tile style loading, persists the default map page, reports missing tiles, labels coordinates as `GPS` or `MAP` depending on what the map is showing, recovers from stale saved map-home data by prioritizing live GPS and positioned mesh nodes, and renders non-map position pages as compass/radar/alert panels.
- The browser flasher requires Chrome or Edge with Web Serial support.
- Private Meshtastic channels, PSKs, admin keys, channel URLs, and personal config are not included.
- A clean public-site flash should be tested on each hardware variant before treating it as broadly stable.
