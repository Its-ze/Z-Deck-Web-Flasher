# Z-Deck 0.2.10-public Source Patch Backup

Built artifact: `firmware/zdeck-2.8.0-zdeck11-public/`
Firmware identity: `2.8.0.zdeck11`
Pack label: `0.2.10-public`
Build folder: `20260601-233903-t-deck-tft`

This archive preserves the public patch set used for the 0.2.10 public T-Deck build.

Apply `zdeck-full-source.patch` to upstream Meshtastic firmware `2.8`, then provide the `device-ui-*.patch` files under the firmware tree's `itsz/` directory before building `env:t-deck-tft`.

The source patch stack contains only public/non-secret material. It does not include private channels, PSKs, channel URLs, admin keys, saved chats, or personal node configuration.

Included:

- `zdeck-full-source.patch`
- `meshtastic-firmware-src.patch`
- `device-ui-map.patch`
- `device-ui-map-internet.patch`
- `device-ui-screen-correction.patch`
- `device-ui-sd-message-journal.patch`
- `device-ui-sd-tools.patch`
- `device-ui-home-status.patch`
- `device-ui-usability.patch`
- `device-ui-polish.patch`
- `device-ui-delivery-status.patch`
- `device-ui-brand-version.patch`
- `device-ui-zdeck-public-stack.patch`