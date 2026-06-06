# Z-Deck Web Flasher

Public GitHub Pages flasher for **Z-Deck Firmware Pack 0.2.15 PUBLIC**.

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

- Release label: `Z-Deck 0.2.15-public`
- Firmware base version: `2.8.0.zdeck16`
- Target: `t-deck-tft`
- LoRa region: `US` compiled default for public LongFast reliability
- Chip: `ESP32-S3`
- Layout: bootloader, partitions, boot_app0, OTA app slots, LittleFS
- Build skin: Modern Field dark theme and compact on-device status layout with a full-row front-page LoRa RX slot to prevent icon overlap.
- Map/position pages: Mesh map, Live compass, DF/Radar, and Distance alert can be selected from the map menu and saved as the default map style.
- Offline maps: SD preparation creates `/maps/zdeck-mesh`, `/maps/zdeck-compass`, `/maps/zdeck-radar`, and `/maps/zdeck-alert`; the map panel reports SD/offline readiness instead of staying stuck on loading.
- Chats: group and direct chat pickers sort newest active thread first, and missing node names fall back to stable `Node xxxx` labels instead of `?? ??`.
- Message UI: received packets show measured hop count as `H#`; unknown route data shows `H?`; outbound limits use `TTL#`.
- Audio: T-Deck I2S ringtone playback uses full tone sequences instead of stopping on the first note.
- SD card: Tools includes a two-press `Prepare / Reset SD` action that shows setup progress, formats the card, builds Z-Deck folders, writes a README, labels supported FAT cards as `TDECKSDCARD`, stores local message history, discovers ringtones from the SD card, and recognizes the same prepared card on later inserts.
- Settings backup: `System > Updates` includes `Backup Settings` and `Restore Settings`. Backups are written to `/zdeck/backups/preferences.proto` and include Meshtastic config, module config, channels/PSKs, owner data, and security keys. Treat the SD card as private.
- Updates: after this build is installed once by USB, use `System > Updates > Check for Updates` on the T-Deck over Wi-Fi, then `Apply Update`. The hosted updater is app-only and writes/verifies the SD settings backup before downloading firmware. App-only updates preserve Meshtastic config, channels, keys, owner settings, and SD chat history unless a future manifest explicitly declares a different update mode.
- USB storage: disabled by default in `0.2.15-public` so Web Serial and Meshtastic API sessions stay stable; SD prep/journal/ringtone/backup features still use the card internally.
- On-device notices: USB connected and SD inserted/setup prompts can be disabled in settings.

## Documentation

- [Compatibility](COMPATIBILITY.md)
- [Recovery and rollback](RECOVERY.md)
- [Known issues](KNOWN_ISSUES.md)
- [Privacy and SD message journal](PRIVACY.md)
- [Release notes](CHANGELOG.md)
- [Source and attribution](SOURCE.md)
