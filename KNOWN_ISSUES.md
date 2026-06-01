# Known Issues

- This is beta firmware. Treat it as experimental.
- The firmware base reports `2.8.0.zdeck4`; the public release label is `0.2.3-public`.
- The SD-card message journal stores message text locally in plaintext.
- SD-card behavior depends on the card mounting correctly at runtime.
- USB SD mass storage is disabled in `0.2.3-public` because the CDC serial + MSC composite path was unstable on Windows during API sessions.
- Avoid editing the same SD-card files from the host computer and the T-Deck UI at the same time.
- GPS and map behavior depends on sky view, valid GPS wiring, and available/cached map tiles.
- The browser flasher requires Chrome or Edge with Web Serial support.
- Private Meshtastic channels, PSKs, admin keys, channel URLs, and personal config are not included.
- A clean public-site flash should be tested on each hardware variant before treating it as broadly stable.

