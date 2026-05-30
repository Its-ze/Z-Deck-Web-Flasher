# Source And Attribution

Z-Deck Firmware Pack is based on Meshtastic firmware.

- Upstream project: https://github.com/meshtastic/firmware
- Upstream branch used for this beta patch set: `2.8`
- Target environment: `t-deck-tft`
- License: GNU GPL v3.0, included in [LICENSE](LICENSE)

## Included Source Patches

The public beta includes the Z-Deck source patch set under [source/patches](source/patches):

- `zdeck-full-source.patch`
- `device-ui-map.patch`
- `device-ui-map-internet.patch`
- `device-ui-screen-correction.patch`
- `device-ui-sd-message-journal.patch`
- `patch-manifest.json`

These patches document the custom changes layered on top of upstream Meshtastic firmware. The shipped binaries should be treated as GPLv3 firmware derived from Meshtastic plus these Z-Deck changes.

## Rebuild Notes

Use the upstream Meshtastic firmware tree, check out the `2.8` branch, apply the patch set, and build the `t-deck-tft` PlatformIO environment. The private workbench contains additional local helper scripts, but this public repo includes the source patches needed to review the custom firmware changes.
