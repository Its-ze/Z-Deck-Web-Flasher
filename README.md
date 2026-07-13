# Z-Deck Web Flasher

Public browser installer and OTA release source for the LILYGO T-Deck/T-Deck Plus `t-deck-tft` build.

- Live flasher: https://its-ze.github.io/Z-Deck-Web-Flasher/
- Wiki: https://its-ze.github.io/Z-Deck-Web-Flasher/wiki/
- Legacy migration metadata: [`update.json`](update.json)
- A/B OTA metadata: [`update-ota.json`](update-ota.json)
- Production checks: [`PRODUCTION_READINESS_LOG.md`](PRODUCTION_READINESS_LOG.md)

This repository contains public firmware only. It must not contain private Meshtastic channels, PSKs, channel URLs, owner-specific settings, Wi-Fi credentials, admin keys, or private setup exports.

## Install Modes

### Standard Z-Deck

Use `manifest.json` for a first install or a dedicated Z-Deck device. It writes:

- Bootloader and the shared 16 MB partition table.
- Z-Deck to OTA A at `0x10000` and OTA B at `0x510000`.
- The public LittleFS image.

Configure private settings locally after the public flash.

### Z-Deck + MeshCore

Use `manifest-dual.json` to install the dual-system layout:

- Z-Deck in OTA A and OTA B.
- MeshCore in its dedicated partition at `0xa10000`.
- No write to NVS or LittleFS.

The dual installer preserves existing Z-Deck configuration, channels, keys, chats, and SD files because it does not write their storage partitions.

Switch from Z-Deck in `Settings > Z-Deck OTA` by pressing `SWITCH TO MESHCORE` twice. Return from MeshCore on its `Z-Deck` page by pressing and releasing Enter. Z-Deck records its current A/B slot before leaving, so MeshCore returns to the correct slot.

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

- `CHECK` reads the hosted `update-ota.json` after the one-time USB migration.
- `APPLY` downloads and verifies the app-only payload.
- `STATUS` shows the current updater state.
- `BACKUP SD` writes `/zdeck/backups/preferences.proto`.
- `RESTORE SD` requires a second confirmation press.

Check, Apply, Backup, and Restore are queued actions so network or SD work does not block the UI callback. App-only A/B OTA does not write NVS, LittleFS, SD, or the dedicated MeshCore partition. Manual SD backup remains available but is not a mandatory OTA preflight because that old coupled path could reset the device. Treat backup files as sensitive because they can contain channels, PSKs, owner data, and security keys.

Devices on zdeck53 or earlier use the dual USB installer once to migrate the partition table safely. The legacy `update.json` intentionally refuses OTA because the old inactive app slot may contain MeshCore. `manifest-ota-test.json` installs zdeck54 without writing storage, providing a repeatable zdeck54-to-zdeck55 OTA test baseline.

## Current Feature Areas

- Mesh map, live compass, DF/radar, and distance warning position pages.
- Strict GPS 3D-fix, satellite, HDOP, age, and coordinate validation; map recentering keeps the last accepted fix.
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
