# Z-Deck 0.2.67

Public LILYGO T-Deck/T-Deck Plus build using the unmodified upstream Meshtastic Device UI pinned in `project.json`.

- `zdeck-firmware.bin`: app-only A/B OTA payload.
- `zdeck-littlefs.bin`: public filesystem image used by the standard USB installer.
- `zdeck-factory.bin`: merged recovery image; it can overwrite more flash than an app-only update.
- `zdeck-meshtastic-metadata.json`: finalized build and partition metadata.

The package contains no private channels, keys, Wi-Fi credentials, owner settings, or admin configuration.
