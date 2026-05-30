# Known Issues

- This is beta firmware. Treat it as experimental.
- The firmware base reports `2.8.0.itsz1`; the public release label is `2.8.0.itsz1-beta.1`.
- The SD-card message journal stores message text locally in plaintext.
- SD-card behavior depends on the card mounting correctly at runtime.
- GPS and map behavior depends on sky view, valid GPS wiring, and available/cached map tiles.
- The browser flasher requires Chrome or Edge with Web Serial support.
- Private Meshtastic channels, PSKs, admin keys, channel URLs, and personal config are not included.
- A clean public-site flash should be tested on each hardware variant before treating it as broadly stable.
