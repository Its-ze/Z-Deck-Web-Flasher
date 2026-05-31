# Changelog

## Z-Deck 0.2.1-public - 2026-05-31

Boot label hotfix public refresh.

- Rebuilt bundled firmware from 20260531-174556-t-deck-tft.
- Fixed the T-Deck boot/version label so it stays compact and does not overlap the boot screen graphic.
- Defaults remain LongFast only. No private channel data, PSKs, channel URLs, private keys, or admin keys are bundled.

## Z-Deck 0.2.0-public - 2026-05-30

Initial public beta flasher release.

- 2026-05-31 refresh: rebuilt bundled firmware from `20260531-150230-t-deck-tft`.
- Fixed T-Deck I2S ringtone playback so full RTTTL-style tone sequences play instead of stopping after the first note.
- Added USB SD-card mass storage for the T-Deck SD card with USB product name `TDECK SD CARD`.
- Added a Tools tab `Prepare / Reset SD` action with a two-press warning, Z-Deck folder setup, README creation, and FAT volume label `TDECKSDCARD` where supported.
- Added public GitHub Pages Web Serial flasher.
- Bundled non-secret T-Deck `t-deck-tft` firmware artifacts.
- Added Z-Deck Classic / Z-Deck beta release labeling.
- Added source patches for the custom firmware changes.
- Added compatibility, recovery, privacy, known-issues, and source attribution docs.
- Added advanced custom manifest URL support on the flasher page.

Firmware customization highlights:

- Z-Deck Classic low-color UI skin.
- GPS/compass refresh changes.
- Dynamic/safe map behavior and map cache menu work.
- Explicit on-device mesh idle, map GPS/WiFi/tile source, and message sent/heard/ACK/failed status labels.
- Follow-up map waiting card and compact TX/RX status chips so blank maps and message state are less ambiguous.
- Per-message hop indicators: received packets show measured `H#`, unknown routes show `H?`, and outgoing limits show `TTL#` instead of pretending the send limit is a measured hop count.
- Tools screen-correction sequence.
- Forced physical USB serial API access for recovery.
- SD-card message journal at `/itsz/history/messages.jsonl`.

