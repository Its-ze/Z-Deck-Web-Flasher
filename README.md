# Z-Deck Web Flasher

Public GitHub Pages flasher for **Z-Deck Firmware Pack 0.2.4 PUBLIC**.

This repo intentionally contains only the browser flashing site, non-secret firmware artifacts, and source patches needed to understand/rebuild the shipped public build. It does not include private Meshtastic channels, PSKs, channel URLs, admin keys, or private setup data.

Live flasher:

https://its-ze.github.io/Z-Deck-Web-Flasher/

Hosted wiki:

https://its-ze.github.io/Z-Deck-Web-Flasher/wiki/

## Release Status

This is **beta / experimental firmware**, not a stable production Meshtastic release.

Use it if you are comfortable recovering an ESP32-S3 T-Deck through bootloader mode. Keep a known-good Meshtastic release nearby in case you need to roll back.

## Use

Open the GitHub Pages site in Chrome or Edge, connect the T-Deck over USB, put it in ESP32-S3 bootloader mode, then choose **Connect and flash**.

Bootloader mode:

1. Plug in the T-Deck over USB.
2. Hold the center trackball / BOOT control.
3. Tap RESET, then release RESET.
4. Release BOOT after the serial port appears.

## Custom Firmware

The page defaults to `manifest.json`. The advanced field can point to another HTTPS ESP Web Tools manifest if you want to flash a different hosted build.

For arbitrary local firmware files, use the Windows installer from the firmware pack:

```powershell
.\Install-ZDeck.ps1 -FirmwareDir .\firmware\your-build
```

## Included Build

- Release label: `Z-Deck 0.2.4-public`
- Firmware base version: `2.8.0.zdeck5`
- Target: `t-deck-tft`
- Chip: `ESP32-S3`
- Layout: bootloader, partitions, boot_app0, OTA app slots, LittleFS
- Message UI: received packets show measured hop count as `H#`; unknown route data shows `H?`; outbound limits use `TTL#`.
- Audio: T-Deck I2S ringtone playback uses full tone sequences instead of stopping on the first note.
- SD card: Tools includes a two-press `Prepare / Reset SD` action that formats the card, builds Z-Deck folders, writes a README, labels supported FAT cards as `TDECKSDCARD`, stores local message history, and discovers ringtones from the SD card.
- USB storage: disabled by default in `0.2.4-public` so Web Serial and Meshtastic API sessions stay stable; SD prep/journal/ringtone features still use the card internally.
- On-device notices: USB connected and SD inserted/setup prompts can be disabled in settings.

## Documentation

- [Compatibility](COMPATIBILITY.md)
- [Recovery and rollback](RECOVERY.md)
- [Known issues](KNOWN_ISSUES.md)
- [Privacy and SD message journal](PRIVACY.md)
- [Release notes](CHANGELOG.md)
- [Source and attribution](SOURCE.md)
