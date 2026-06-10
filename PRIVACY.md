# Privacy

This public repo does not include private Meshtastic channels, PSKs, complete channel URLs, admin keys, private keys, saved chats, or personal node configuration.

## SD Message Journal

Z-Deck adds a custom SD-card message journal. When the SD card is mounted, sent and received text messages can be appended to:

```text
/itsz/history/messages.jsonl
```

Entries include message direction, sender, destination, channel number, time, and text.

The journal is plaintext local history. Anyone with access to the SD card may be able to read it. Remove or encrypt the SD card if the message history is sensitive.

## SD Settings Backup

In `0.2.27-cyberdeck`, Z-Deck can back up and restore Meshtastic preferences from:

```text
/zdeck/backups/preferences.proto
```

The backup file includes Meshtastic config, module config, channels/PSKs, owner data, and security keys. It is local plaintext storage on the SD card. Do not publish it, upload it to public issues, or share it with anyone you do not want to have access to your mesh settings.

## USB SD Access

In `0.2.27-cyberdeck`, Z-Deck does not expose the SD card as USB mass storage by default. Treat the SD card as plaintext local storage: files, maps, logs, ringtone assets, settings backups, and message history may be visible if the card is removed or mounted by another build.

## On-Device Updates

The Wi-Fi updater uses the hosted `update.json` manifest and applies only app firmware updates marked `app-only`. In `0.2.27-cyberdeck`, Apply Update writes and verifies the SD settings backup before downloading firmware. The update mode does not erase NVS config, Meshtastic channels, keys, owner settings, sidebar placement, map page default, owner home title behavior, or SD-card files. A future update that intentionally changes config or data must declare a different update mode before the device will accept it. The Wi-Fi scan/dropdown setup stores only the selected network credentials in the device's normal Meshtastic configuration path.
