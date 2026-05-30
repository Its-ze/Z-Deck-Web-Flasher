# Privacy

This public repo does not include private Meshtastic channels, PSKs, complete channel URLs, admin keys, private keys, saved chats, or personal node configuration.

## SD Message Journal

Z-Deck adds a custom SD-card message journal. When the SD card is mounted, sent and received text messages can be appended to:

```text
/itsz/history/messages.jsonl
```

Entries include message direction, sender, destination, channel number, time, and text.

The journal is plaintext local history. Anyone with access to the SD card may be able to read it. Remove or encrypt the SD card if the message history is sensitive.
