# Z-Deck 0.2.6-public Source Patch Backup

Built artifact: `firmware/zdeck-2.8.0-zdeck7-public/`
Firmware identity: `2.8.0.zdeck7`
Pack label: `0.2.6-public`
Build folder: `20260601-zdeck7-t-deck-tft`

This archive keeps the full source delta plus the device UI patch stack used for the normal Z-Deck public release.

Important changes in this release:

- `USERPREFS_CONFIG_LORA_REGION` is compiled as `meshtastic_Config_LoRaConfig_RegionCode_US` for the T-Deck build so LongFast does not remain in an unset radio region after setup.
- The boot progress bar uses the corrected compact foreground layout and non-animated updates.
- The public patch stack rebuilds cleanly without the stale `LittleFSService` fallback include.

No private channel data, PSKs, channel URLs, private keys, admin keys, or saved chats are bundled.