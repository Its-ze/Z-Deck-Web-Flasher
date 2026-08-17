# Known Issues

- This is beta firmware. Treat it as experimental.
- The current firmware and pack versions are authoritative in `update.json`; the flasher reads those values at runtime.
- The SD-card message journal stores message text locally in plaintext.
- The SD settings backup at `/zdeck/backups/preferences.proto` stores Meshtastic config, channels/PSKs, owner data, and security keys locally in plaintext.
- SD-card behavior depends on the card mounting correctly at runtime.
- USB SD mass storage is disabled because the CDC serial + MSC composite path was unstable on Windows during API sessions.
- Z-Deck 0.2.67 intentionally uses the unmodified upstream Meshtastic Device UI. Custom Z-Deck launcher, map/compass, OTA, SD maintenance, theme, sidebar, diagnostics, and dual-switch screens are not present.
- Z-Deck OTA and SD maintenance remain available through the USB serial commands documented in `README.md`; OTA requires configured and connected Wi-Fi.
- If the screen still shows the retired custom Z-Deck launcher after an update, compare the on-device version with `update.json`; an older app slot may still be booting after an incomplete flash.
- Avoid editing the same SD-card files from the host computer and the T-Deck UI at the same time.
- GPS and map behavior still depends on sky view, valid GPS wiring, positioned peer nodes, and the capabilities of the upstream Meshtastic Device UI. Z-Deck retains strict live-fix validation but no longer replaces the upstream map or compass screens.
- The browser flasher requires Chrome or Edge with Web Serial support.
- Private Meshtastic channels, PSKs, admin keys, channel URLs, and personal config are not included.
- A clean public-site flash should be tested on each hardware variant before treating it as broadly stable.
