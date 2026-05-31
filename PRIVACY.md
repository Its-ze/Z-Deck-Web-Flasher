# Privacy

This public repo does not include private Meshtastic channels, PSKs, complete channel URLs, admin keys, private keys, saved chats, or personal node configuration.

## SD Message Journal

Z-Deck adds a custom SD-card message journal. When the SD card is mounted, sent and received text messages can be appended to:

```text
/itsz/history/messages.jsonl
```

Entries include message direction, sender, destination, channel number, time, and text.

The journal is plaintext local history. Anyone with access to the SD card may be able to read it. Remove or encrypt the SD card if the message history is sensitive.

## USB SD Access

When the T-Deck is plugged into a computer and the SD card is mounted, Z-Deck can expose the card as USB mass storage named `TDECK SD CARD`. Treat this the same as removing the card: files, maps, logs, ringtone assets, and message history on the SD card may be visible to the connected computer.
