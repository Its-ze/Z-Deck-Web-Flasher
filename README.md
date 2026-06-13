# Z-Deck Web Flasher

Public GitHub Pages flasher for **Z-Deck Firmware Pack 0.2.34-cyberdeck**.

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

If the flash verifies but the device keeps showing the ESP32-S3 programming/ROM-loader port, use the page's Recovery assistant. Choose **Normal boot**, release BOOT/trackball/GPIO0 completely, then tap RESET or unplug/replug normally before trying Meshtastic API or private setup.

## Custom Firmware

The page defaults to `manifest.json`. The advanced field can point to another HTTPS ESP Web Tools manifest if you want to flash a different hosted build.

For arbitrary local firmware files, use the Windows installer from the firmware pack:

```powershell
.\Install-ZDeck.ps1 -FirmwareDir .\firmware\your-build
```

## Included Build

- Release label: `Z-Deck 0.2.34-cyberdeck`
- Firmware base version: `2.8.0.zdeck35`
- Target: `t-deck-tft`
- LoRa region: `US` compiled default for public LongFast reliability
- Chip: `ESP32-S3`
- Layout: bootloader, partitions, boot_app0, OTA app slots, LittleFS
- Sidebar: System setting controls left/right placement, defaults to right-side placement, persists at `/zdeck_sidebar.cfg`, and uses a fixed gutter so the right rail does not cover top/header panels.
- Home identity: the home header shows the configured Meshtastic owner name instead of a hard-coded CyberDeck title.
- Header safety: the owner title is clipped into the lane between the battery/percent block and the right-side status icons, and full batteries show clamped percent instead of USB-only status.
- Build skin: Modern Field dark theme and compact on-device status layout with a full-row front-page LoRa RX slot to prevent icon overlap.
- Map/position pages: Mesh map, Live compass, DF/Radar, and Distance alert are switched with the Map tab or the compact map menu without changing the real SD tile style. The default page persists across restarts. The map page includes Center, which moves to live GPS, positioned mesh nodes, then saved map area. The coordinate readout now says `GPS` when it is showing the live centered GPS fix and `MAP` when it is showing the manually scrolled map center. Compass/Radar/Alert pages render a real ring, heading/status text, and nearest positioned mesh-node bearing/range when data is available instead of showing a stuck map underneath.
- Wi-Fi setup: the T-Deck Wi-Fi popup can scan nearby networks, show RSSI and open/locked status, and fill the selected SSID. Open networks can save with a blank password, while manual SSID/password entry still works.
- GPS defaults: fresh T-Deck installs keep GPS enabled on RX44/TX43 and disable the inherited T-Deck power-saving default so the receiver stays active.
- Offline maps: SD preparation creates Z-Deck map folders, while the real tile loader stays on `/maps/zdeck-mesh` by default and filters non-tile page folders from the tile-style dropdown. The on-device map reports drawing, ready, missing-tile, and cached-tile status instead of staying stuck on a loading message. If GPS or peer locations arrive after opening the map, the view recenters and stale saved map-home data no longer prevents recovery to the live GPS or located mesh-node area.
- Chats: group and direct chat pickers sort newest active thread first, and missing node names fall back to stable `Node xxxx` labels instead of `?? ??`.
- Message UI: received packets show measured hop count as `H#`; unknown route data shows `H?`; outbound limits use `TTL#`.
- Audio: T-Deck I2S ringtone playback uses full tone sequences instead of stopping on the first note.
- SD card: Tools includes a two-press `Prepare / Reset SD` action that shows setup progress, formats the card, builds Z-Deck folders, writes a README, labels supported FAT cards as `TDECKSDCARD`, stores local message history, discovers ringtones from the SD card, and recognizes the same prepared card on later inserts.
- Settings backup: the active T-Deck Settings screen has a visible `Z-Deck OTA` block with `BACKUP SD` and guarded `RESTORE SD` controls. Backups are written to `/zdeck/backups/preferences.proto` and include Meshtastic config, module config, channels/PSKs, owner data, and security keys. Treat the SD card as private.
- Updates: after this build is installed once by USB, use the Wi-Fi settings popup to scan/select your network, then open `Settings > Z-Deck OTA` and use `CHECK`, `APPLY`, or `STATUS`. The hosted updater is app-only and writes/verifies the SD settings backup before downloading firmware. App-only updates preserve Meshtastic config, channels, keys, owner settings, sidebar placement, map page default, and SD chat history unless a future manifest explicitly declares a different update mode.
- OTA and backup controls: CHECK, APPLY, BACKUP SD, and RESTORE SD release the pressed button and repaint the status readout before long Wi-Fi, flash, or SD work starts. OTA progress also pumps the screen during download/write.
- USB storage: disabled by default so Web Serial and Meshtastic API sessions stay stable; SD prep/journal/ringtone/backup features still use the card internally.
- On-device notices: USB connected and SD inserted/setup prompts can be disabled in settings.

## Documentation

- [Compatibility](COMPATIBILITY.md)
- [Recovery and rollback](RECOVERY.md)
- [Known issues](KNOWN_ISSUES.md)
- [Privacy and SD message journal](PRIVACY.md)
- [Release notes](CHANGELOG.md)
- [Source and attribution](SOURCE.md)
