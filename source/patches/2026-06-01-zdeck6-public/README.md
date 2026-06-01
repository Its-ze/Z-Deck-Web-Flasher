# Z-Deck 0.2.5-public Source Patch Backup

Built artifact: `firmware/zdeck-2.8.0-zdeck6-public/`
Firmware identity: `2.8.0.zdeck6`
Pack label: `0.2.5-public`
Build folder: `20260601-zdeck6-t-deck-tft`

This archive keeps the full source delta plus the device UI patch stack used for the normal Z-Deck public release.

Important change in this release:

- `USERPREFS_CONFIG_LORA_REGION` is compiled as `meshtastic_Config_LoRaConfig_RegionCode_US` for the T-Deck build so LongFast does not remain in an unset radio region after setup.

No private channel data, PSKs, channel URLs, private keys, admin keys, or saved chats are bundled.
