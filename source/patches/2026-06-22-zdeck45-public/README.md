# Z-Deck 0.2.44-cyberdeck public source archive

Firmware: 2.8.0.zdeck45
Build source: 20260622-zdeck45-sd-backup-ready-state-t-deck-tft

This public-safe archive fixes the on-device BACKUP SD/RESTORE SD crash path by deferring SD maintenance outside the UI button handler. It also adds the USB ackup-queue diagnostic for the same deferred path and fixes backup completion state so diagnostics return READY instead of staying busy.

No private channels, PSKs, private keys, admin keys, Wi-Fi passwords, or admin URLs are bundled.