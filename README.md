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

Switching is optional and never automatic. In this stock-UI release, switch from Z-Deck with the guarded USB serial command `itsz zdeck switch meshcore`. MeshCore remains active until you explicitly press and release Enter on its `Z-DECK` page. Z-Deck records its current A/B slot before leaving, so a manual return reaches the correct slot.

Run the dual-system browser installer once before using the switch command. App-only OTA deliberately cannot create or replace the dedicated MeshCore partition.

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

Z-Deck 0.2.67 uses the unmodified upstream Meshtastic Device UI, so the retired `Settings > Z-Deck OTA` custom panel is intentionally absent. The preserved updater backend can be diagnosed and triggered over the Z-Deck USB serial console:

- `itsz zdeck status` shows updater, storage, and runtime state.
- `itsz zdeck wifi scan` checks visible Wi-Fi networks without printing saved credentials.
- `itsz zdeck ota check` reads the hosted `update-ota.json`.
- `itsz zdeck ota apply` downloads and verifies the app-only payload.
- `itsz zdeck backup-queue` writes `/zdeck/backups/preferences.proto` without blocking the UI.
- `itsz zdeck restore confirm` restores the SD backup and reboots.

App-only A/B OTA does not write NVS, LittleFS, SD, or the dedicated MeshCore partition. Manual SD backup remains available but is not a mandatory OTA preflight. Treat backup files as sensitive because they can contain channels, PSKs, owner data, and security keys.

Devices on zdeck53 or earlier use the dual USB installer once to migrate the partition table safely. The legacy `update.json` intentionally refuses OTA because the old inactive app slot may contain MeshCore. `manifest-ota-test.json` installs zdeck54 without writing storage, providing a repeatable zdeck54-to-zdeck57 OTA test baseline.

## Current Feature Areas

- Unmodified upstream Meshtastic Device UI at pinned commit `4bf593a82100b911ff816dddf7158ffdee2114cd`.
- Standard Meshtastic home, messages, contacts/nodes, map, and settings behavior for the T-Deck.
- Strict GPS 3D-fix, satellite, HDOP, age, and coordinate validation behind the standard UI.
- A/B OTA backend with size, MD5, and SHA-256 verification plus USB status and control commands.
- Guarded SD settings backup/restore and local chat journal.
- Redacted USB diagnostics and manual dual-system switching.
- Separate VoidLink T-Dongle USB network adapter flasher and pairing UI.

## Verification

Run the public release checks from this directory:

```powershell
python tools\verify-ota-release.py
python tools\verify-dual-release.py
python tools\verify-project.py
```

Add `--live` to `verify-ota-release.py` only after publishing when you need to compare local and GitHub Pages bytes.

## Documentation

- [Compatibility](COMPATIBILITY.md)
- [Recovery and rollback](RECOVERY.md)
- [Known issues](KNOWN_ISSUES.md)
- [Privacy](PRIVACY.md)
- [Source and attribution](SOURCE.md)
- [Changelog](CHANGELOG.md)
