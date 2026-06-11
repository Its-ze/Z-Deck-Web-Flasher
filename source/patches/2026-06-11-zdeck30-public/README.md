# Z-Deck 0.2.29-cyberdeck Source Patch Archive

This folder contains the public-safe patch stack used to build `2.8.0.zdeck30` / `0.2.29-cyberdeck` from Meshtastic firmware `2.8`.

The zdeck30 change fixes map recovery on the physical T-Deck: live GPS and located mesh nodes now take priority over stale saved map-home data, automatic centering keeps trying until live GPS is usable, and the map overlay shows current GPS coordinates when available.

No private channel URLs, PSKs, admin keys, Wi-Fi credentials, owner-specific settings, or saved chats are included.
