# Z-Deck Web Flasher

Public GitHub Pages flasher for **Z-Deck Firmware Pack 0.2.1 PUBLIC**.

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

- Release label: `Z-Deck 0.2.1-public`
- Firmware base version: `2.8.0.zdeck2`
- Target: `t-deck-tft`
- Chip: `ESP32-S3`
- Layout: bootloader, partitions, boot_app0, OTA app slots, LittleFS
- Message UI: received packets show measured hop count as `H#`; unknown route data shows `H?`; outbound limits use `TTL#`.
- Audio: T-Deck I2S ringtone playback uses full tone sequences instead of stopping on the first note.
- SD card: Tools includes a two-press `Prepare / Reset SD` action that formats the card, builds Z-Deck folders, writes a README, and labels supported FAT cards as `TDECKSDCARD`.
- USB storage: when an SD card is mounted, the T-Deck exposes it to the computer as `TDECK SD CARD` USB mass storage.

## Documentation

- [Compatibility](COMPATIBILITY.md)
- [Recovery and rollback](RECOVERY.md)
- [Known issues](KNOWN_ISSUES.md)
- [Privacy and SD message journal](PRIVACY.md)
- [Release notes](CHANGELOG.md)
- [Source and attribution](SOURCE.md)

