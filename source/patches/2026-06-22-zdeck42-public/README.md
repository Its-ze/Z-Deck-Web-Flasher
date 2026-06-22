# Z-Deck 0.2.41 Public Source Patch Archive

This archive contains the public-safe source patch stack used for Z-Deck `0.2.41-cyberdeck` / firmware `2.8.0.zdeck42`.

The zdeck42 change adds USB Wi-Fi diagnostics for OTA troubleshooting:

- `wifi-status` reports whether Wi-Fi is enabled, configured, connected, and its status code.
- `wifi-scan` reports scan counts and whether the saved network was seen, without printing SSIDs or passwords.
- `wifi-start` starts Wi-Fi using credentials already saved on the device, without printing or changing them.

This archive does not include private channels, PSKs, admin keys, Wi-Fi passwords, or user settings.
