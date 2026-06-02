# Z-Deck 0.2.7-public Source Patch Backup

Built artifact: `firmware/zdeck-2.8.0-zdeck8-public/`
Firmware identity: `2.8.0.zdeck8`
Pack label: `0.2.7-public`
Build folder: `20260601-zdeck8-t-deck-tft`
Upstream base: Meshtastic firmware `2.8` branch at commit `35b059040`

This archive preserves the public patch set used for the 0.2.7 public T-Deck build.

Changes from 0.2.6-public:

- SD setup detection accepts cards prepared with the current Z-Deck `/zdeck` and `/itsz/history` layout.
- Older legacy SD folder layouts remain accepted so existing prepared cards do not need to be reworked.
- The SD setup popup and Tools reset/format flow now show progress while checking, formatting, remounting, and creating folders.
- The prior 0.2.6 public stack is preserved, including the corrected boot progress bar, US LongFast default, classic UI, serial recovery, disabled USB mass storage, SD history/ringtones, popup controls, map/status/delivery improvements, and sound-off setup compatibility.

Patch files:

- `zdeck-full-source.patch`
- `meshtastic-firmware-src.patch`
- `device-ui-map.patch`
- `device-ui-map-internet.patch`
- `device-ui-screen-correction.patch`
- `device-ui-sd-message-journal.patch`
- `device-ui-sd-tools.patch`
- `device-ui-sd-card-notices-ringtones.patch`
- `device-ui-usability.patch`
- `device-ui-polish.patch`
- `device-ui-delivery-status.patch`
- `device-ui-brand-version.patch`
- `device-ui-zdeck-public-stack.patch`
