# T-Deck SD Popups Build Patch

Created: 2026-06-01
Target: LilyGO T-Deck / T-Deck Plus, PlatformIO environment `t-deck-tft`
Built artifact: `firmware/zdeck-2.8.0-sdpopups-20260601/`

This backup captures the local working firmware used for the SD-card setup and popup-control build.

Included patches:

- `meshtastic-firmware-src.patch`: tracked Meshtastic firmware source changes in `src/`.
- `meshtastic-device-ui.patch`: local PlatformIO `meshtastic-device-ui` dependency changes against upstream device-ui `4bf593a82100b911ff816dddf7158ffdee2114cd`.

Notes:

- Sound/buzzer was kept off during testing.
- Build succeeded for `t-deck-tft` on 2026-06-01.
- Flash verified on COM6 with app image `firmware-t-deck-tft-2.8.0.f9fea56.bin`.
- The T-Deck remained in ESP bootloader mode after flashing until physically released/reset.
- Build logs, serial test logs, and downloaded map tiles were intentionally left out of this backup.
