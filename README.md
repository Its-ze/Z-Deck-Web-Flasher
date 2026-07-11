# Z-Deck Web Flasher

Public browser installer and OTA release source for the LILYGO T-Deck/T-Deck Plus `t-deck-tft` build.

- Live flasher: https://its-ze.github.io/Z-Deck-Web-Flasher/
- Wiki: https://its-ze.github.io/Z-Deck-Web-Flasher/wiki/
- Release metadata: [`update.json`](update.json)
- Production checks: [`PRODUCTION_READINESS_LOG.md`](PRODUCTION_READINESS_LOG.md)

This repository contains public firmware only. It must not contain private Meshtastic channels, PSKs, channel URLs, owner-specific settings, Wi-Fi credentials, admin keys, or private setup exports.

## Install Modes

### Standard Z-Deck

Use `manifest.json` for a first install or a dedicated Z-Deck device. It writes:

- Bootloader and the shared 16 MB partition table.
- Z-Deck to app 0 and app 1.
- The public LittleFS image.

Configure private settings locally after the public flash.

### Z-Deck + MeshCore

Use `manifest-dual.json` to install the dual-system layout:

- Z-Deck in app 0 at `0x10000`.
- MeshCore in app 1 at `0x650000`.
- No write to NVS or LittleFS.

The dual installer preserves existing Z-Deck configuration, channels, keys, chats, and SD files because it does not write their storage partitions.

Switch from Z-Deck in `Settings > Z-Deck OTA` by pressing `SWITCH TO MESHCORE` twice. Return from MeshCore on its `Z-Deck` page by pressing and releasing Enter. Both systems validate the destination image before changing the ESP32 boot partition.

## Browser Flash

1. Open the live flasher in current Chrome or Edge.
2. Select the standard or dual-system layout.
3. Connect the T-Deck over USB and choose its serial port.
4. Keep USB connected until ESP Web Tools completes verification.
5. Release BOOT/trackball and tap RESET for a normal boot.

Bootloader entry when the port does not appear:

1. Hold the center trackball / BOOT control.
2. Tap RESET and release RESET.
3. Release BOOT after the serial port appears.

Do not erase the device for a normal firmware upgrade. Erasing also removes local configuration and keys.

## OTA Updates

After the initial USB install, connect Wi-Fi from the T-Deck and open `Settings > Z-Deck OTA`:

- `CHECK` reads the hosted `update.json`.
- `APPLY` downloads and verifies the app-only payload.
- `STATUS` shows the current updater state.
- `BACKUP SD` writes `/zdeck/backups/preferences.proto`.
- `RESTORE SD` requires a second confirmation press.

App-only OTA updates do not write NVS, LittleFS, or SD. The updater requests an SD settings backup before installing. Treat that backup as sensitive because it can contain channels, PSKs, owner data, and security keys.

## Current Feature Areas

- Mesh map, live compass, DF/radar, and distance warning position pages.
- GPS startup defaults, live fix status, map recentering, and coordinate source labels.
- Newest-first direct/group chats, stable node names, delivery state, and hop count.
- Wi-Fi scan/select and visible OTA progress/status.
- Guarded SD preparation, settings backup/restore, and local chat journal.
- Right-side navigation option, battery safe zone, compact status lanes, and selectable themes.
- On-device diagnostics and redacted USB debug commands.
- Separate VoidLink T-Dongle USB network adapter flasher and pairing UI.

## Verification

Run the public release checks from this directory:

```powershell
python tools\verify-ota-release.py
python tools\verify-dual-release.py
```

Add `--live` to `verify-ota-release.py` only after publishing when you need to compare local and GitHub Pages bytes.

## Documentation

- [Compatibility](COMPATIBILITY.md)
- [Recovery and rollback](RECOVERY.md)
- [Known issues](KNOWN_ISSUES.md)
- [Privacy](PRIVACY.md)
- [Source and attribution](SOURCE.md)
- [Changelog](CHANGELOG.md)
