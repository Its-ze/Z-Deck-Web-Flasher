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
- `device-ui-map-pages.patch`
- `device-ui-map-switching-fix.patch`
- `device-ui-map-autocenter.patch`
- `device-ui-map-fullscreen.patch`
- `device-ui-screen-correction.patch`
- `device-ui-sd-message-journal.patch`
- `device-ui-sd-tools.patch`
- `device-ui-home-status.patch`
- `device-ui-usability.patch`
- `device-ui-polish.patch`
- `device-ui-delivery-status.patch`
- `device-ui-brand-version.patch`
- `device-ui-home-layout-fix.patch`
- `device-ui-zdeck-public-stack.patch`
- `device-ui-sidebar-layout.patch`
- `device-ui-sidebar-overlap-fix.patch`
- `device-ui-ota-controls.patch`
- `device-ui-wifi-scan.patch`

These patches document the custom changes layered on top of upstream Meshtastic firmware. The shipped binaries should be treated as GPLv3 firmware derived from Meshtastic plus these Z-Deck changes.

## Rebuild Notes

Use the upstream Meshtastic firmware tree, check out the `2.8` branch, apply the patch set, and build the `t-deck-tft` PlatformIO environment. The current full source patch also includes the Z-Deck app-only Wi-Fi updater service, active LVGL Settings OTA controls, SD settings backup/restore support, sidebar placement with a fixed gutter/header overlap fix, bounded battery-safe owner-name home header behavior, Wi-Fi scan/select, map-page defaults, and map tile progress status. The private workbench contains additional local helper scripts, but this public repo includes the source patches needed to review the custom firmware changes.
