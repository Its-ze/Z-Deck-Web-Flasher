# Z-Deck 0.2.12-public Source Patch Backup

Built artifact: firmware/zdeck-2.8.0-zdeck13-public/
Firmware identity: 2.8.0.zdeck13
Pack label: 0.2.12-public
Build folder: 20260602-zdeck13-t-deck-tft

This archive preserves the public patch set used for the 0.2.12 public T-Deck build.

Apply zdeck-full-source.patch to upstream Meshtastic firmware 2.8, then provide the device-ui-*.patch files under the firmware tree's itsz/ directory before building env:t-deck-tft.

The source patch stack contains only public/non-secret material. It does not include private channels, PSKs, channel URLs, admin keys, saved chats, or personal node configuration.

Included:

- zdeck-full-source.patch
- meshtastic-firmware-src.patch
- device-ui-map.patch
- device-ui-map-internet.patch
- device-ui-screen-correction.patch
- device-ui-sd-message-journal.patch
- device-ui-sd-tools.patch
- device-ui-home-status.patch
- device-ui-usability.patch
- device-ui-polish.patch
- device-ui-delivery-status.patch
- device-ui-brand-version.patch
- device-ui-zdeck-public-stack.patch
