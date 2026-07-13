# Changelog

## Z-Deck 0.2.56-cyberdeck - 2026-07-13

Manual-only dual-mesh choice.

- Added `ADVICE ONLY` and `STAY ZD` controls to the Mesh Networks hub.
- Changed the hub status to state that Meshtastic stays active and that its network recommendation is informational only.
- Kept maps, channels, chats, settings, GPS, OTA, SD, and diagnostics usable without switching firmware.
- Retained the guarded two-press MeshCore action; an expired or single press leaves Z-Deck active.
- Updated the MeshCore `Z-DECK` page to state that MeshCore stays active and that return is manual.
- Rebuilt and verified both ESP32-S3 images and updated the dual installer without changing storage offsets.

## Z-Deck 0.2.55-cyberdeck - 2026-07-13

Integrated Z-Deck launcher and dual-mesh control.

- Replaced the launcher Dashboard tile's fall-through to the stock Meshtastic home panel with a dedicated Z-Deck dashboard.
- Added live Meshtastic status, nearby nodes, RX age, GPS, battery, SD, unread-message, and MeshCore-readiness fields to the dashboard.
- Replaced the old Mesh Mode settings shortcut with a dedicated Mesh Networks hub and guarded MeshCore switch control.
- Added explicit `READY` and `USB INSTALL NEEDED` states so a missing dedicated MeshCore image is actionable.
- Cached MeshCore image validation once per boot to avoid repeated flash reads during UI refreshes.
- Fixed the local dual-package helper to seed Z-Deck into both A/B OTA slots and label MeshCore as the dedicated partition rather than app1.
- Updated the dual browser installer and OTA metadata to zdeck56 while preserving NVS, LittleFS, SD files, channels, keys, and local preferences.

## Z-Deck 0.2.54-cyberdeck - 2026-07-12

Strict GPS quality and safe dual-slot OTA architecture.

- Added a GPS acceptance policy requiring a fresh 3D fix, at least five satellites, HDOP at or below 2.5, and valid signed coordinate ranges before replacing the last accepted position.
- Replaced the old Z-Deck/MeshCore app-slot collision with two 5 MB Z-Deck OTA slots and a dedicated 2.5 MB MeshCore partition.
- Kept NVS and LittleFS offsets unchanged so the preservation-safe installers retain device settings, channels, keys, UI preferences, chats, and SD files.
- Moved OTA Check and Apply into the deferred service state machine so HTTP/download/write work does not freeze the UI callback.
- Removed mandatory SD backup from the OTA preflight. Manual Backup and Restore remain separate queued actions with status reporting.
- Added `update-ota.json` for migrated A/B devices and made legacy `update.json` require USB migration rather than risk overwriting MeshCore.
- Added `manifest-ota-test.json` with zdeck54 as a repeatable baseline for testing the zdeck55 OTA transition.
- Updated the public flasher, source patches, checksum workflow, recovery map, and dual-system validator for the new layout.

## Z-Deck 0.2.53-cyberdeck - 2026-07-12

USB migration baseline for the dual-slot partition layout and dynamic OTA manifest routing.

## Z-Deck 0.2.52-cyberdeck - 2026-07-12

Smart map fallback and GPS acquisition status.

- Fixed the tile state machine so a completely missing tile set cannot remain `drawing` forever.
- Added a visible coordinate grid and center reticle whenever no tile has rendered.
- Added live coordinates after a GPS fix and separate `GPS ACQUIRING`/`GPS SEARCHING` states before a fix.
- Kept map nodes, navigation controls, the persistent MAP/COMP/RADAR/ALERT bar, and dual-mesh switching above the fallback layer.
- Updated the USB OTA helper to treat the expected disconnect after `ota/update.end.ok` as a successful reboot.
- App-only OTA still preserves NVS, LittleFS, SD data, channels, keys, chats, owner settings, and UI preferences.


## Z-Deck 0.2.51-cyberdeck - 2026-07-11

Validated quick switching between Meshtastic and MeshCore.

- Bumped the T-Deck runtime identity to `2.8.0.zdeck52` and pack label to `0.2.51-cyberdeck`.
- Added a compact `MESH >` button to the Z-Deck Home header, clear of the logo, sidebar, and battery safe lane.
- Changed the Settings control to one-press `MESHCORE >`; it validates app 1, selects it, disables both switch controls, and reboots after the transition status is rendered.
- Updated the MeshCore Z-Deck page to show the hot-switch state and reject app 0 unless its application descriptor identifies a `zdeck` firmware version.
- Kept the serial `itsz zdeck switch meshcore` recovery/control path and the existing app-image validation.
- Switching changes the ESP32 boot partition only. It does not reflash or erase NVS, LittleFS, SD data, channels, keys, chats, map defaults, or sidebar preferences.
- No private channel data, PSKs, channel URLs, Wi-Fi credentials, admin keys, or owner-specific settings are bundled.

## Z-Deck 0.2.50-cyberdeck - 2026-07-11

On-device UI audit and map-system rebuild.

- Bumped the T-Deck runtime identity to `2.8.0.zdeck51` and pack label to `0.2.50-cyberdeck`.
- Replaced scattered map page and auto-center flags with a standalone, host-testable map state controller.
- Added an always-visible, fixed-size `MAP`, `COMP`, `RADAR`, and `ALERT` mode bar that remains clear of map pan, zoom, OSD, compass, and radar controls.
- Changed fallback centering so a saved map or peer cluster remains eligible for replacement by the first valid live GPS fix.
- Made manual pan/zoom stop automatic snapping, while enabling Follow GPS explicitly resumes centering.
- Unified mesh proximity distance on the latitude-aware distance helper and centralized tile-state classification.
- Rechecked source geometry for home, nodes, groups, chats, message composer, map, settings, tools, diagnostics, top status lanes, battery safe zone, and left/right sidebar placement.
- Kept dual-system switching, app-only OTA, SD backup/restore guardrails, selectable themes, Wi-Fi scan/select, newest-first chats, delivery state, and hop counters.
- No private channel data, PSKs, channel URLs, Wi-Fi credentials, admin keys, or owner-specific settings are bundled.

## Z-Deck 0.2.49-cyberdeck - 2026-07-11

Dual-system switching and public flasher redesign.

- Bumped the T-Deck runtime identity to `2.8.0.zdeck50` and pack label to `0.2.49-cyberdeck`.
- Added a validated app-slot switch module shared by the USB console and the on-device Settings page.
- Added a two-press `SWITCH TO MESHCORE` control under `Settings > Z-Deck OTA`; unavailable or invalid app 1 images are rejected without rebooting.
- Added a separate `manifest-dual.json` browser path that writes Z-Deck to app 0 and MeshCore to app 1 without writing NVS or LittleFS.
- Redesigned the public flasher around the actual install workflow with standard/dual tabs, storage write maps, recovery controls, VoidLink handoff, and responsive mobile layout.
- Made release labels load from `update.json` instead of stale hard-coded HTML and JavaScript values.
- Fixed the dual-package flash helper to validate every package SHA256, use ESP32-S3 USB reset at a stable baud rate, and fail on any nonzero `esptool` result.
- Kept the existing map legibility, GPS/compass, chat, Wi-Fi, OTA, SD, diagnostics, battery/header, sidebar, and theme improvements.
- No private channel data, PSKs, channel URLs, Wi-Fi credentials, admin keys, or owner-specific settings are bundled.

## Z-Deck 0.2.37-cyberdeck - 2026-06-16

SD backup/restore decode hotfix.

- Rebuilt bundled firmware from `20260616-zdeck38-sd-backup-restore-hotfix-t-deck-tft`.
- Bumped runtime identity to `2.8.0.zdeck38` and pack label to `0.2.37-cyberdeck`.
- Fixed SD settings backup verification and restore by decoding `/zdeck/backups/preferences.proto` using the actual SD file size instead of the maximum protobuf size.
- Added explicit rejection for empty or oversized SD backup files so bad backup media fails clearly.
- Kept zdeck37 duplicate found-device cleanup plus selectable themes, GPS/MAP labels, compass/radar/alert pages, compact map controls, diagnostics, OTA/backup repaint fixes, GPS recovery, Wi-Fi scan/select, newest-first chats, node-name, hop counter, battery/header, and sidebar fixes.
- No private channel data, PSKs, channel URLs, Wi-Fi credentials, admin keys, or owner-specific settings are bundled.

## Z-Deck 0.2.36-cyberdeck - 2026-06-14

OTA test release for duplicate found-device cleanup.

- Rebuilt bundled firmware from `20260614-zdeck37-ota-test-t-deck-tft`.
- Bumped runtime identity to `2.8.0.zdeck37` and pack label to `0.2.36-cyberdeck`.
- Deduped repeated NodeDB records before rendering the on-device node list, message destination picker, and favorite-node pages, so TDK1 or the local device should not appear multiple times in found devices.
- Kept zdeck36 selectable themes plus GPS/MAP labels, compass/radar/alert pages, compact map menu, diagnostics, OTA/backup repaint fixes, GPS recovery, Wi-Fi scan/select, SD backup/restore, newest-first chats, node-name, hop counter, battery/header, and sidebar fixes.
- No private channel data, PSKs, channel URLs, Wi-Fi credentials, admin keys, or owner-specific settings are bundled.

## Z-Deck 0.2.35-cyberdeck - 2026-06-13

Production theme and validation pass for the physical T-Deck UI.

- Rebuilt bundled firmware from `20260613-zdeck36-production-themes-t-deck-tft`.
- Bumped runtime identity to `2.8.0.zdeck36` and pack label to `0.2.35-cyberdeck`.
- Added three selectable screen themes: `Amber Terminal`, `Slate Signal`, and `Arctic High`.
- Verified zdeck36 app-only flashing on TDK1 without flashing LittleFS; owner/config survived, GPS produced a live fix, receive worked from the base bridge, and LongFast direct transmit received an ACK from the base node.
- Kept zdeck35 GPS/MAP labels plus compass/radar/alert pages, compact map menu, diagnostics, OTA/backup repaint fixes, GPS recovery, Wi-Fi scan/select, SD backup/restore, newest-first chats, node-name, hop counter, battery/header, and sidebar fixes.
- No private channel data, PSKs, channel URLs, Wi-Fi credentials, admin keys, or owner-specific settings are bundled.
## Z-Deck 0.2.34-cyberdeck - 2026-06-13

Map GPS/MAP readout hotfix for the physical T-Deck UI.

- Rebuilt bundled firmware from `20260613-zdeck35-map-gps-label-t-deck-tft`.
- Bumped runtime identity to `2.8.0.zdeck35` and pack label to `0.2.34-cyberdeck`.
- Changed the map coordinate readout to label live centered GPS coordinates as `GPS` and manually scrolled map-center coordinates as `MAP`.
- Verified the app-only image on two plugged-in T-Decks without flashing LittleFS; both boards booted zdeck35 and kept existing settings/channels.
- Kept zdeck32-zdeck34 compass/radar/alert pages, compact map menu, diagnostics, OTA/backup repaint fixes, GPS recovery, Wi-Fi scan/select, SD backup/restore, newest-first chats, node-name, hop counter, battery/header, and sidebar fixes.

## Z-Deck 0.2.31-cyberdeck - 2026-06-11

Compass and map-options hotfix for the physical T-Deck UI.

- Rebuilt bundled firmware from `20260611-zdeck32-compass-map-menu-t-deck-tft`.
- Bumped runtime identity to `2.8.0.zdeck32` and pack label to `0.2.31-cyberdeck`.
- Added a real LVGL compass/radar/alert panel for the non-map position pages so those pages no longer stay visually stuck on the map.
- Compacted the map options overlay so page switching, Center, GPS status, Wi-Fi, and cache readouts fit on the T-Deck screen.
- Kept zdeck31 OTA/backup repaint fixes plus GPS recovery, visible Settings OTA, Wi-Fi scan/select, SD backup/restore, newest-first chats, node-name, hop counter, battery/header, and sidebar fixes.

## Z-Deck 0.2.30-cyberdeck - 2026-06-11

OTA and SD backup button repaint hotfix.

- Rebuilt bundled firmware from `20260611-zdeck31-ota-ui-progress-t-deck-tft`.
- Bumped runtime identity to `2.8.0.zdeck31` and pack label to `0.2.30-cyberdeck`.
- Fixed CHECK, APPLY, BACKUP SD, STATUS, and RESTORE SD so the pressed state is cleared and the status label repaints before long Wi-Fi, flash, or SD work starts.
- Added screen pumps during app-only OTA download/write progress so the device does not look frozen while the update is moving.
- Kept zdeck30 map GPS recovery plus the existing Settings OTA, Wi-Fi scan/select, SD backup/restore, newest-first chats, node-name, hop counter, battery/header, and sidebar fixes.

## Z-Deck 0.2.29-cyberdeck - 2026-06-11

Physical T-Deck map GPS recovery and zdeck30 public-safe release package.

- Rebuilt bundled firmware from `20260611-zdeck30-map-gps-recovery-t-deck-tft`.
- Bumped runtime identity to `2.8.0.zdeck30` and pack label to `0.2.29-cyberdeck`.
- Fixed map centering priority so live GPS and positioned mesh nodes recover the view before stale saved map-home data.
- Kept automatic map centering pending until live GPS becomes usable, instead of stopping after a saved-home fallback.
- Added coordinate-aware GPS text to the map overlay so the device shows the location it is actually using.
- Published a new app-only OTA manifest that preserves Meshtastic config, channels, keys, owner settings, sidebar placement, map page default, and SD chat history.
- Kept visible Settings OTA controls, Wi-Fi scan/select, SD settings backup/restore, battery/header fixes, sidebar gutter fixes, newest-first chats, stable node names, send status, hop counters, public-safe labels, and disabled USB SD mass storage.
- No private channel data, PSKs, channel URLs, Wi-Fi credentials, admin keys, or owner-specific settings are bundled.

## Z-Deck 0.2.28-cyberdeck - 2026-06-10

Visible OTA controls for the physical T-Deck UI.

- Rebuilt bundled firmware from `20260610-zdeck29-ota-controls-t-deck-tft`.
- Bumped runtime identity to `2.8.0.zdeck29` and pack label to `0.2.28-cyberdeck`.
- Added a visible `Z-Deck OTA` block to the active LVGL Settings screen with `CHECK`, `APPLY`, `STATUS`, `BACKUP SD`, and guarded `RESTORE SD` controls.
- The OTA block shows a live readout from the updater service so checks, cached update status, app-only apply state, and SD backup/restore actions are visible on device.
- Kept zdeck28 battery-safe owner header behavior, fixed sidebar gutter, safe top-panel placement, map UI, Wi-Fi scan/select, app-only Wi-Fi updates, SD settings backup/restore, SD chat history, newest-first chats, stable node names, clearer send status, hop counters, Modern Field UI, home RX overlap fixes, and disabled USB SD mass storage.
- No private channel data, PSKs, channel URLs, private keys, Wi-Fi credentials, or admin keys are bundled.

## Z-Deck 0.2.27-cyberdeck - 2026-06-10

Battery/header overlap fix for the physical T-Deck UI.

- Rebuilt bundled firmware from `20260610-zdeck28-header-battery-safe-t-deck-tft`.
- Bumped runtime identity to `2.8.0.zdeck28` and pack label to `0.2.27-cyberdeck`.
- Clips the configured owner title into the safe lane between the left battery/percent block and the right-side time/status icons.
- Keeps real battery percent visible when a full or USB-powered T-Deck reports charge value 101 by clamping the displayed percent to `100%` instead of switching to USB-only status.
- Kept zdeck27 owner-name header behavior, fixed sidebar gutter, safe top-panel placement, map UI, Wi-Fi scan/select, app-only Wi-Fi updates, SD settings backup/restore, SD chat history, newest-first chats, stable node names, clearer send status, hop counters, Modern Field UI, home RX overlap fixes, and disabled USB SD mass storage.
- No private channel data, PSKs, channel URLs, private keys, Wi-Fi credentials, or admin keys are bundled.

## Z-Deck 0.2.26-cyberdeck - 2026-06-10

Owner-name home header fix for the physical T-Deck UI.

- Rebuilt bundled firmware from `20260610-zdeck27-owner-home-title-cyberdeck-t-deck-tft`.
- Bumped runtime identity to `2.8.0.zdeck27` and pack label to `0.2.26-cyberdeck`.
- Fixed the home screen header that made both T-Decks look like the same `ITSZ CyberDeck` device by showing the configured Meshtastic owner name instead.
- Clips long owner names before they can run into the top status/battery area.
- Kept zdeck26 fixed sidebar gutter, safe top-panel placement, map UI, Wi-Fi scan/select, app-only Wi-Fi updates, SD settings backup/restore, SD chat history, newest-first chats, stable node names, clearer send status, hop counters, Modern Field UI, home RX overlap fixes, and disabled USB SD mass storage.
- No private channel data, PSKs, channel URLs, private keys, Wi-Fi credentials, or admin keys are bundled.

## Z-Deck 0.2.25-cyberdeck - 2026-06-10

Sidebar gutter and header overlap fix for the physical T-Deck UI.

- Rebuilt bundled firmware from `20260610-zdeck26-sidebar-gutter-cyberdeck-t-deck-tft`.
- Bumped runtime identity to `2.8.0.zdeck26` and pack label to `0.2.25-cyberdeck`.
- Replaced percentage sidebar sizing with a fixed 36 px rail plus 4 px gutter so the right-side bar no longer covers content.
- Moved setup, search, neighbors, LoRa TX, and initial setup panels into the safe content area when the sidebar is on either side.
- Kept zdeck25 map UI progress/defaults, Wi-Fi scan/select, app-only Wi-Fi updates, SD settings backup/restore, SD chat history, newest-first chats, stable node names, clearer send status, hop counters, Modern Field UI, home RX overlap fixes, and disabled USB SD mass storage.
- No private channel data, PSKs, channel URLs, private keys, Wi-Fi credentials, or admin keys are bundled.

## Z-Deck 0.2.24-cyberdeck - 2026-06-10

Map UI and zdeck25 public-safe release package.

- Rebuilt bundled firmware from `20260610-zdeck25-map-ui-cyberdeck-t-deck-tft`.
- Bumped runtime identity to `2.8.0.zdeck25` and pack label to `0.2.24-cyberdeck`.
- Tightened the T-Deck map menu so controls fit the physical 320 x 240 screen without overlapping.
- Added persistent default map page storage for Mesh map, Live compass, DF/Radar, and Distance alert.
- Added tile slots, loaded-tile, and missing-tile counters so the map reports real progress/readiness.
- Updated map overlays with compact Mesh/Compass/DF/Distance status, nearest-node range, and distance warning text.
- Fixed the PlatformIO device-ui patch marker so repeated build hook passes do not fail after later map-label changes.
- Kept sidebar placement, Wi-Fi scan/select, app-only Wi-Fi updates, SD settings backup/restore, SD chat history, newest-first chats, stable node names, clearer send status, hop counters, Modern Field UI, home RX overlap fixes, and disabled USB SD mass storage.
- No private channel data, PSKs, channel URLs, private keys, Wi-Fi credentials, or admin keys are bundled.

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
