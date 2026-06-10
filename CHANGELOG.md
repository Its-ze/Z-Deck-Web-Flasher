# Changelog

## Web flasher recovery assistant - 2026-06-10

Programming-mode recovery helper for post-flash support.

- Added a visible Recovery assistant to the public flasher page.
- Added Normal boot, Enter bootloader, and Verify app mode flows for devices that flash successfully but keep presenting the ESP32-S3 ROM loader.
- Updates the status ticker when a recovery mode is selected.
- No firmware payload, private channel data, PSKs, channel URLs, private keys, Wi-Fi credentials, admin keys, or private setup data changed.

## Z-Deck 0.2.23-cyberdeck - 2026-06-09

Sidebar placement and zdeck24 public-safe release package.

- Rebuilt bundled firmware from `20260609-zdeck24-sidebar-right-cyberdeck-t-deck-tft`.
- Bumped runtime identity to `2.8.0.zdeck24` and pack label to `0.2.23-cyberdeck`.
- Added a System setting for sidebar placement, defaulted to the right side for one-handed T-Deck use.
- Persisted sidebar placement in the device UI filesystem at `/zdeck_sidebar.cfg`.
- Kept Wi-Fi scan/select, app-only Wi-Fi updates, SD settings backup/restore, SD chat history, map page switching, newest-first chats, stable node names, clearer send status, hop counters, Modern Field UI, home RX overlap fixes, and disabled USB SD mass storage.
- No private channel data, PSKs, channel URLs, private keys, Wi-Fi credentials, or admin keys are bundled.

## Z-Deck 0.2.20-public - 2026-06-07

On-device Wi-Fi scan and select setup for the public build.

- Rebuilt bundled firmware from `20260607-zdeck21-t-deck-tft`.
- Bumped runtime identity to `2.8.0.zdeck21` and pack label to `0.2.20-public`.
- Added a Scan button to the T-Deck Wi-Fi popup so the device can search nearby networks instead of requiring manual SSID typing.
- Added a network dropdown that shows SSID, signal strength, and open/locked status, then fills the selected SSID into the Wi-Fi settings form.
- Open networks can now save with a blank password; locked networks still focus the password field after selection.
- Manual SSID/password entry remains available for hidden networks or unusual setups.
- Kept zdeck20 map Center and late GPS/node auto-center recovery, zdeck19 page/tile-style separation, compact map status, app-only Wi-Fi updates, SD settings backup/restore, fresh GPS startup defaults, home RX overlap fixes, newest-first chats, stable node names, clearer send status, Modern Field UI, public LongFast defaults, and disabled USB SD mass storage.
- No private channel data, PSKs, channel URLs, private keys, or admin keys are bundled.

## Z-Deck 0.2.19-public - 2026-06-07

Physical T-Deck map usability fix for the public build.

- Rebuilt bundled firmware from `20260607-zdeck20-t-deck-tft`.
- Bumped runtime identity to `2.8.0.zdeck20` and pack label to `0.2.19-public`.
- Added a `CENTER` control to the map menu; it centers on GPS first, saved map area second, and positioned mesh nodes third.
- Fixed the case where the map was opened before GPS or peer coordinates were ready and stayed on the default world view.
- Added one-shot auto-recenter when the first GPS fix or positioned mesh node arrives after opening the map.
- Manual pan, zoom, and Home now disable pending auto-center so the map does not pull away after you move it.
- Kept zdeck19 map page/tile-style separation, compact map status, app-only Wi-Fi updates, SD settings backup/restore, fresh GPS startup defaults, home RX overlap fixes, newest-first chats, stable node names, clearer send status, Modern Field UI, public LongFast defaults, and disabled USB SD mass storage.
- No private channel data, PSKs, channel URLs, private keys, or admin keys are bundled.

## Z-Deck 0.2.18-public - 2026-06-06

Physical T-Deck map/menu fix for the public build.

- Rebuilt bundled firmware from `20260606-zdeck19-t-deck-tft`.
- Bumped runtime identity to `2.8.0.zdeck19` and pack label to `0.2.18-public`.
- Fixed Z-Deck map page switching so Mesh map, Live compass, DF/Radar, and Distance alert no longer overwrite the real map tile style.
- Pressing the Map tab while already on the map now cycles to the next Z-Deck map page.
- Enlarged the map menu's Next View and Remember controls to make switching and saving easier on the physical T-Deck.
- Kept the real tile loader on `zdeck-mesh` by default and filtered non-tile Z-Deck page folders from the map style dropdown.
- Moved map readiness/status text to a compact bottom-left overlay so it does not block the map view.
- Kept visible Home Action and System Z-Deck Updates, SD settings backup/restore, fresh GPS startup defaults, home RX overlap fixes, newest-first chats, stable node names, clearer send status, Modern Field UI, public LongFast defaults, and disabled USB SD mass storage.
- No private channel data, PSKs, channel URLs, private keys, or admin keys are bundled.

## Z-Deck 0.2.17-public - 2026-06-06

Visible on-device OTA entry plus the fresh T-Deck GPS startup fix for the public build.

- Rebuilt bundled firmware from `20260606-zdeck18-t-deck-tft`.
- Bumped runtime identity to `2.8.0.zdeck18` and pack label to `0.2.17-public`.
- Added `Z-Deck Updates` directly to the Home Action menu so update controls are not hidden in the nested System menu.
- Kept `System > Z-Deck Updates` for the same Check, Apply, Backup, Restore, and Status actions.
- Disabled the inherited T-Deck power-saving default for fresh Z-Deck installs so GPS stays active.
- Kept GPS enabled on RX44/TX43 with 5-second GPS updates for supported T-Deck/T-Deck Plus hardware.
- Kept SD settings backup/restore, pre-update SD backup verification, app-only Wi-Fi updates, home RX overlap fixes, saved map pages, newest-first chats, stable node names, clearer send status, Modern Field UI, public LongFast defaults, and disabled USB SD mass storage from 0.2.15.
- No private channel data, PSKs, channel URLs, private keys, or admin keys are bundled.

## Z-Deck 0.2.15-public - 2026-06-06

SD settings backup/restore and safer app-only Wi-Fi updates for the public build.

- Rebuilt bundled firmware from `20260606-zdeck16-t-deck-tft`.
- Bumped runtime identity to `2.8.0.zdeck16` and pack label to `0.2.15-public`.
- Added `System > Updates > Backup Settings` and `Restore Settings` for SD-card Meshtastic preference backups.
- `Apply Update` now writes and verifies `/zdeck/backups/preferences.proto` before downloading firmware.
- The SD backup includes Meshtastic config, module config, channels/PSKs, owner data, and security keys, so the SD card must be treated as private.
- Kept the home RX overlap fix, saved map pages, SD/offline map folder prep, newest-first chat pickers, stable node-name fallbacks, clearer send status, app-only Wi-Fi updates, Modern Field UI, public LongFast defaults, and disabled USB SD mass storage from 0.2.14.
- No private channel data, PSKs, channel URLs, private keys, or admin keys are bundled.

## Z-Deck 0.2.14-public - 2026-06-05

Physical T-Deck home-screen row-wrap fix for the public build.

- Rebuilt bundled firmware from `20260605-zdeck15-t-deck-tft`.
- Bumped runtime identity to `2.8.0.zdeck15` and pack label to `0.2.14-public`.
- Restored full-row layout space for the home LoRa RX status label so LVGL flex wrapping cannot put the next front-page icon into the same row.
- Kept the LoRa RX text compact with clipped status text, a smaller label font, and a short idle/readout line inside the reserved row.
- Kept map page/default selection, SD/offline map folder prep, newest-first chat pickers, stable node-name fallbacks, clearer send status, app-only Wi-Fi updates, Modern Field UI, public LongFast defaults, and disabled USB SD mass storage from 0.2.13.
- No private channel data, PSKs, channel URLs, private keys, or admin keys are bundled.

## Z-Deck 0.2.13-public - 2026-06-05

Home RX, map pages, chat ordering, names, and send-status cleanup for the public build.

- Rebuilt bundled firmware from `20260605-zdeck14-t-deck-tft`.
- Bumped runtime identity to `2.8.0.zdeck14` and pack label to `0.2.13-public`.
- Fixed the T-Deck home LoRa RX status as a clipped fixed-size label so it does not overlap neighboring front-page icons.
- Added map page/default selection for Mesh map, Live compass, DF/Radar, and Distance alert.
- Prepared SD/offline map folders under `/maps/zdeck-*` and changed the map status card so it reports offline readiness instead of staying stuck on loading.
- Sorted group and direct chat thread pickers by latest activity first.
- Improved node-name fallbacks so missing long/short names do not render as `??` or `?? ??`.
- Changed channel broadcast send labels to `BCAST SENT` / `BCAST TTL# SENT`, while keeping direct-message ACK/no-response labels.
- Kept app-only Wi-Fi updates, Modern Field UI, SD setup detection/progress fixes, boot progress fix, public LongFast defaults, and disabled USB SD mass storage from 0.2.12.
- No private channel data, PSKs, channel URLs, private keys, or admin keys are bundled.

## Z-Deck 0.2.12-public - 2026-06-02

Main screen signal row overlap correction for the public build.

- Rebuilt bundled firmware from `20260602-zdeck13-t-deck-tft`.
- Bumped runtime identity to `2.8.0.zdeck13` and pack label to `0.2.12-public`.
- Fixed the T-Deck home signal row so the short `Listening` / `RX` status keeps a full row slot and no longer pushes the next icon into the same line.
- Kept the LongFast default channel fallback, app-only Wi-Fi updates, Modern Field UI, SD setup detection/progress fixes, boot progress fix, public LongFast defaults, and disabled USB SD mass storage from 0.2.11.
- No private channel data, PSKs, channel URLs, private keys, or admin keys are bundled.

## Z-Deck 0.2.11-public - 2026-06-02

Physical T-Deck home screen layout correction for the public build.

- Rebuilt bundled firmware from 20260602-073938-t-deck-tft.
- Bumped runtime identity to 2.8.0.zdeck12 and pack label to 0.2.11-public.
- Fixed the physical T-Deck home RX/status layout so it stays inside the signal block and does not overlap the front-page icons.
- Kept the LongFast default channel fallback, app-only Wi-Fi updates, Modern Field UI, SD setup detection/progress fixes, boot progress fix, public LongFast defaults, and disabled USB SD mass storage from 0.2.10.
- No private channel data, PSKs, channel URLs, private keys, or admin keys are bundled.
## Z-Deck 0.2.10-public - 2026-06-02

Front-page radio status cleanup for the public T-Deck build.

- Rebuilt bundled firmware from `20260601-233903-t-deck-tft`.
- Bumped runtime identity to `2.8.0.zdeck11` and pack label to `0.2.10-public`.
- Fixed the home-screen LoRa status text so `RX` no longer overlaps the front page.
- Changed the public default channel fallback so empty/default LongFast no longer displays as `unset`.
- Kept app-only Wi-Fi updates, Modern Field UI, SD setup detection/progress fixes, boot progress fix, public LongFast defaults, and disabled USB SD mass storage from 0.2.9.
- No private channel data, PSKs, channel URLs, private keys, or admin keys are bundled.
## Z-Deck 0.2.9-public - 2026-06-02

On-device Wi-Fi update flow for the public T-Deck build.

- Rebuilt bundled firmware from `20260601-221536-t-deck-tft`.
- Bumped runtime identity to `2.8.0.zdeck10` and pack label to `0.2.9-public`.
- Added `System > Updates` on the T-Deck with `Check for Updates`, `Apply Update`, and `Update Status`.
- Added hosted `update.json` metadata for app-only Wi-Fi OTA updates.
- App-only OTA writes only the firmware app slot, preserving Meshtastic config, channels, keys, owner settings, and SD chat history.
- Kept the Modern Field UI, SD setup detection/progress fixes, boot progress fix, public LongFast defaults, and disabled USB SD mass storage from 0.2.8.
- No private channel data, PSKs, channel URLs, private keys, or admin keys are bundled.

## Z-Deck 0.2.8-public - 2026-06-01

Modern Field theme and layout refresh for the public T-Deck build.

- Rebuilt bundled firmware from `20260601-zdeck9-t-deck-tft`.
- Bumped runtime identity to `2.8.0.zdeck9` and pack label to `0.2.8-public`.
- Added the Modern Field dark theme palette for the T-Deck UI.
- Restyled the generated home/status layout with compact modern icon chips, a darker surface palette, and clearer active/inactive state colors.
- Restyled the Tools health panel, SD prepare/reset panel, SD setup popup, nav rail, and boot progress bar to match the new theme.
- Kept the 0.2.7 SD setup fixes: prepared cards are not treated as new on every insert, and setup/reset operations show visible progress readouts.
- No private channel data, PSKs, channel URLs, private keys, or admin keys are bundled.

## Z-Deck 0.2.7-public - 2026-06-01

SD setup detection and progress-readout fix for the public T-Deck build.

- Rebuilt bundled firmware from `20260601-zdeck8-t-deck-tft`.
- Bumped runtime identity to `2.8.0.zdeck8` and pack label to `0.2.7-public`.
- Fixed SD setup detection so a card prepared with the Z-Deck `/zdeck` and `/itsz/history` layout is not treated as new on every insert.
- Kept compatibility with cards prepared by the older `/maps`, `/ringtones`, `/messages`, `/backups`, and `/logs` layout.
- Added visible SD setup progress during popup setup and Tools reset/format work, including checking, formatting, remounting, and folder creation status.
- Kept the 0.2.6 public stack: corrected boot progress bar, US LongFast default, classic UI, serial recovery, disabled USB mass storage, SD history/ringtones, popup controls, map/status/delivery improvements, and sound-off setup compatibility.
- No private channel data, PSKs, channel URLs, private keys, or admin keys are bundled.

## Z-Deck 0.2.6-public - 2026-06-01

Boot progress and clean source rebuild fix for the public T-Deck build.

- Rebuilt bundled firmware from `20260601-zdeck7-t-deck-tft`.
- Bumped runtime identity to `2.8.0.zdeck7` and pack label to `0.2.6-public`.
- Fixed the boot progress bar so it renders as a compact foreground bar and does not overlap boot labels.
- Switched boot progress updates to non-animated LVGL updates so early boot state changes are visible reliably.
- Fixed the public source patch stack so clean rebuilds no longer depend on an unavailable `LittleFSService` map fallback include.
- Kept the 0.2.5 public stack: US LongFast default, classic UI, serial recovery, disabled USB mass storage, SD tools/history/ringtones, popup controls, map/status/delivery improvements, and sound-off setup compatibility.
- No private channel data, PSKs, channel URLs, private keys, or admin keys are bundled.

## Z-Deck 0.2.5-public - 2026-06-01

Region-default fix for the public T-Deck LongFast build.

- Rebuilt bundled firmware from `20260601-zdeck6-t-deck-tft`.
- Bumped runtime identity to `2.8.0.zdeck6` and pack label to `0.2.5-public`.
- Compiled the T-Deck public build with `USERPREFS_CONFIG_LORA_REGION=US` so setup cannot leave the radio in `UNSET` while using LongFast.
- Kept the previous Z-Deck public stack: classic UI, LongFast defaults, serial recovery, disabled USB mass storage, SD tools/history/ringtones, popup controls, boot progress, map/status/delivery improvements, and sound-off setup compatibility.
- No private channel data, PSKs, channel URLs, private keys, or admin keys are bundled.

## Z-Deck 0.2.4-public - 2026-06-01

Normal naming refresh for the public flasher package.

- Rebuilt bundled firmware from `20260601-zdeck5-t-deck-tft`.
- Bumped runtime identity to `2.8.0.zdeck5` and pack label to `0.2.4-public`.
- Restored the previous Z-Deck public stack: classic UI, LongFast-only defaults, serial recovery, disabled USB mass storage, SD tools, map/status/delivery improvements, SD history, and I2S ringtone playback fixes.
- Added USB/SD notice popup controls, SD setup prompt with ignore/format choices, boot progress bar, SD ringtone folder support, and SD-backed message history.
- No private channel data, PSKs, channel URLs, private keys, or admin keys are bundled.

## Z-Deck 0.2.3-public - 2026-06-01

Stability release for the public flasher.

- Rebuilt bundled firmware from `20260601-072002-t-deck-tft`.
- Bumped runtime identity to `2.8.0.zdeck4` and pack label to `0.2.3-public`.
- Disabled always-on USB SD mass storage in the public build because the CDC serial + MSC composite path could make Windows drop the device when opening the serial API.
- Kept the SD-card prepare/reset tool and local SD journal support, but the public build now reports USB SD as disabled.
- Preserved LongFast-only public defaults. No private channel data, PSKs, channel URLs, private keys, or admin keys are bundled.

## Z-Deck 0.2.1-public - 2026-05-31

Boot label hotfix public refresh.

- Rebuilt bundled firmware from 20260531-174556-t-deck-tft.
- Fixed the T-Deck boot/version label so it stays compact and does not overlap the boot screen graphic.
- Defaults remain LongFast only. No private channel data, PSKs, channel URLs, private keys, or admin keys are bundled.

## Z-Deck 0.2.0-public - 2026-05-30

Initial public beta flasher release.

- 2026-05-31 refresh: rebuilt bundled firmware from `20260531-150230-t-deck-tft`.
- Fixed T-Deck I2S ringtone playback so full RTTTL-style tone sequences play instead of stopping after the first note.
- Added USB SD-card mass storage for the T-Deck SD card with USB product name `TDECK SD CARD`.
- Added a Tools tab `Prepare / Reset SD` action with a two-press warning, Z-Deck folder setup, README creation, and FAT volume label `TDECKSDCARD` where supported.
- Added public GitHub Pages Web Serial flasher.
- Bundled non-secret T-Deck `t-deck-tft` firmware artifacts.
- Added Z-Deck Classic / Z-Deck beta release labeling.
- Added source patches for the custom firmware changes.
- Added compatibility, recovery, privacy, known-issues, and source attribution docs.
- Added advanced custom manifest URL support on the flasher page.

Firmware customization highlights:

- Z-Deck Classic low-color UI skin.
- GPS/compass refresh changes.
- Dynamic/safe map behavior and map cache menu work.
- Explicit on-device mesh idle, map GPS/WiFi/tile source, and message sent/heard/ACK/failed status labels.
- Follow-up map waiting card and compact TX/RX status chips so blank maps and message state are less ambiguous.
- Per-message hop indicators: received packets show measured `H#`, unknown routes show `H?`, and outgoing limits show `TTL#` instead of pretending the send limit is a measured hop count.
- Tools screen-correction sequence.
- Forced physical USB serial API access for recovery.
- SD-card message journal at `/itsz/history/messages.jsonl`.
