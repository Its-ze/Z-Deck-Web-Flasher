# Z-Deck Web Flasher

Public GitHub Pages flasher for the ITSZ Z-Deck Firmware Pack.

This repo intentionally contains only the browser flashing site and non-secret firmware artifacts. It does not include private Meshtastic channels, PSKs, channel URLs, admin keys, or the full firmware workbench.

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

- Version: `2.8.0.itsz1`
- Target: `t-deck-tft`
- Chip: `ESP32-S3`
- Layout: bootloader, partitions, boot_app0, OTA app slots, LittleFS

