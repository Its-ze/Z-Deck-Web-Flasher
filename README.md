# Z-Deck Web Flasher

Public GitHub Pages flasher for **Z-Deck Firmware Pack Beta 1**.

This repo intentionally contains only the browser flashing site, non-secret firmware artifacts, and source patches needed to understand/rebuild the shipped beta. It does not include private Meshtastic channels, PSKs, channel URLs, admin keys, or private setup data.

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

For local private builds or arbitrary local firmware files, use the private pack's Windows installer:

```powershell
.\Install-ZDeck.ps1 -FirmwareDir .\firmware\your-build
```

## Included Build

- Release label: `Z-Deck 2.8.0.itsz1-beta.1`
- Firmware base version: `2.8.0.itsz1`
- Target: `t-deck-tft`
- Chip: `ESP32-S3`
- Layout: bootloader, partitions, boot_app0, OTA app slots, LittleFS

## Documentation

- [Compatibility](COMPATIBILITY.md)
- [Recovery and rollback](RECOVERY.md)
- [Known issues](KNOWN_ISSUES.md)
- [Privacy and SD message journal](PRIVACY.md)
- [Release notes](CHANGELOG.md)
- [Source and attribution](SOURCE.md)
