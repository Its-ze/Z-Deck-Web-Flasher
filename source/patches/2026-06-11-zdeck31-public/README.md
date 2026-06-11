# Z-Deck 0.2.30-cyberdeck Source Patch Archive

This folder contains the public-safe patch stack used to build `2.8.0.zdeck31` / `0.2.30-cyberdeck` from Meshtastic firmware `2.8`.

The zdeck31 change fixes the OTA/backup control behavior on the physical T-Deck: CHECK, APPLY, BACKUP SD, and RESTORE SD now release their pressed state and repaint status before blocking Wi-Fi, flash, or SD work starts. OTA progress also pumps the screen while downloading and writing the app image.
