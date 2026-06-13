# Z-Deck Production Readiness Log

This file is the running checklist for hourly T-Deck/Z-Deck production readiness passes.

Rules for each run:
- Preserve LittleFS, SD settings backups, private channels, admin settings, owner names, and chat data unless the task explicitly requires changing them.
- Do not store PSKs, private keys, admin channel URLs, full Meshtastic info dumps, or raw backup contents here.
- Each run must either add one scoped feature/improvement or complete one concrete bug check with evidence.
- Record exact pages, controls, status labels, hardware ports, and visible elements checked.
- Separate confirmed behavior from blockers that require physical reset, replug, pairing approval, GPS sky view, or another external action.

## Exact Check Matrix

### Public Web Flasher

- Page: `https://its-ze.github.io/Z-Deck-Web-Flasher/`
  - Version badges: firmware version, pack version, chip family, public channel label.
  - Installer element: `esp-web-install-button#installButton`.
  - Manifest field: `input#customManifest`.
  - Status ticker: `#statusTicker`.
  - Recovery assistant: Normal boot, Enter bootloader, Verify app mode buttons.
  - Feature cards: Wi-Fi scan/select, OTA, SD backup, map pages, chat ordering/status, themes, diagnostics.
  - Source/docs links: README, recovery, source patches, privacy/security docs.
  - Layout checks: desktop width, mobile width, no icon/text overlap, no off-screen buttons.

- Endpoint: `https://its-ze.github.io/Z-Deck-Web-Flasher/manifest.json`
  - Firmware package version.
  - ESP32-S3 offsets and file paths.
  - Public package path points at the current release folder.

- Endpoint: `https://its-ze.github.io/Z-Deck-Web-Flasher/update.json`
  - `latest.firmwareVersion`.
  - `latest.packVersion`.
  - App-only update mode.
  - Firmware URL, size, SHA256, and MD5.

- Endpoint: hosted firmware binary
  - HTTP status is `200`.
  - Content length matches `update.json`.
  - SHA256 matches `update.json` when locally downloaded or already available.

### On-Device T-Deck Pages

- Home page
  - Owner name is visible and unique per device.
  - RX/LoRa signal row does not overlap icons.
  - Top bar does not overlap the right sidebar.
  - Battery icon and percent both render inside the safe header lane.
  - Right/left sidebar placement leaves content gutters clear.

- Settings > Wi-Fi
  - Scan button is visible.
  - Network list/dropdown is visible.
  - Select/connect flow gives status feedback.
  - Manual SSID/password controls remain available.

- Settings > Z-Deck OTA
  - CHECK button.
  - APPLY button.
  - STATUS button.
  - BACKUP SD button.
  - guarded RESTORE SD button.
  - Status/progress text updates during backup, download, write, verify, and reboot preparation.

- Map section
  - Mesh Map page.
  - Live Compass page.
  - DF/Radar page.
  - Distance Alert page.
  - Compact options menu is fully visible.
  - Page switch control is easy to use.
  - Default map page persists across restart.
  - GPS/MAP coordinate label matches the current center source.
  - Map stops showing loading once GPS or positioned mesh-node data is available.

- Chat section
  - Direct chat list newest active thread first.
  - Group chat list newest active thread first.
  - Message order in a thread is newest/oldest as intended for the current view.
  - Message input is bounded and does not span the full screen awkwardly.
  - Sender names/nicknames render instead of `?? ??` when node info is available.
  - Missing names fall back to stable node labels.
  - Send status, ACK status, and hop counters are visible.

- Diagnostics page
  - Firmware version.
  - Device role and region.
  - GPS fix state.
  - SD backup status.
  - OTA state.
  - Bluetooth enabled/advertising/pairing state.
  - Last send/receive status.

### Hardware and Radio Checks

- USB serial inventory
  - Record COM port, USB VID/PID, and device identity.
  - Do not run parallel Meshtastic reads on the same COM port.

- T-Deck serial/API
  - Metadata readback.
  - Firmware version.
  - Owner long/short names.
  - Non-secret channel names only.
  - GPS configuration and live position state.
  - Bluetooth enabled state.

- RF send/receive
  - Base-to-T-Deck receive proof.
  - T-Deck-to-base transmit proof.
  - ACK result where applicable.
  - Hop start/limit and RSSI/SNR where safely available.

- Bluetooth
  - Windows adapter visibility.
  - Bluetooth service state.
  - BLE scan API usability.
  - T-Deck Bluetooth config readback.
  - Pairing/discovery blocker, if any.
  - Do not record pairing PINs, private keys, or channel secrets.

## Run Entries

### 2026-06-13 07:51 -04:00

Scope: hourly automation hardening, first explicit Bluetooth baseline, and production checklist creation.

Changed:
- Updated the `t-deck-production-readiness-follow-up` automation to run hourly through the current production-readiness window.
- Tightened the automation prompt so each run must add a scoped improvement or record concrete bug-check evidence.
- Created this running checklist so exact pages, controls, and hardware elements have a durable audit trail.

Public web checks:
- Confirmed the public flasher repo was clean before creating this log.
- Confirmed the live public page includes `2.8.0.zdeck36`, `0.2.35-cyberdeck`, and `Amber Terminal`.
- Confirmed live `update.json` reports firmware `2.8.0.zdeck36`, pack `0.2.35-cyberdeck`, and firmware SHA256 `e7480173d7c7504103ebaf5703a1308a84346c8240ea7a90c261fe7072384a32`.
- Confirmed hosted firmware binary returned HTTP `200` with content length `3697280`.

Device checks:
- Available T-Deck app port: `COM17`.
- `COM17` metadata readback reported firmware `2.8.0.zdeck36`, role `CLIENT`, hardware `T_DECK`.
- Bluetooth config on `COM17` initially read back disabled.
- Bluetooth was enabled on `COM17` and then read back as enabled.

Bluetooth checks:
- Windows Bluetooth service `bthserv` was running.
- `DeviceAssociationService` was running.
- Working Bluetooth adapter: `USB\VID_0489&PID_E112\00E04C000001`, status `OK`, problem code `0`.
- Second Bluetooth adapter: `USB\VID_0B05&PID_1D70\6&D596480&0&2`, status `Error`, problem code `31`; not usable until driver/device issue is cleared.
- Python `bleak` is installed.
- BLE scanner call completed successfully, but discovered `0` advertisements during the scan window.

Blockers / next check:
- BLE scan did not yet prove T-Deck advertising or pairing; retest after the T-Deck is reset/replugged or Bluetooth pairing mode is visible on-device.
- The second T-Deck was not present on USB during this pass; it still needs physical reset/replug before flashing or verification.

### 2026-06-13 11:53 -04:00

Scope: hourly public-release surface and Bluetooth usability bug check.

Changed:
- No firmware or private settings were changed.
- Appended this evidence entry to keep the production checklist current.

Repo / release state:
- Public flasher repo head before this entry: `857df98 Link production readiness log`.
- Local public repo was clean before this log update.

Public web checks:
- Page checked: `https://its-ze.github.io/Z-Deck-Web-Flasher/`.
- Confirmed visible/crawled elements: `2.8.0.zdeck36`, `0.2.35-cyberdeck`, `Readiness Log`, `PRODUCTION_READINESS_LOG.md`, `Z-Deck OTA`, `Amber Terminal`, `Slate Signal`, `Arctic High`, `Wi-Fi`, and `BACKUP SD`.
- Endpoint checked: `https://its-ze.github.io/Z-Deck-Web-Flasher/update.json`.
- Confirmed update manifest: firmware `2.8.0.zdeck36`, pack `0.2.35-cyberdeck`, update mode `app-only`, app size `3697280`, app SHA256 `e7480173d7c7504103ebaf5703a1308a84346c8240ea7a90c261fe7072384a32`.
- Endpoint checked: `https://its-ze.github.io/Z-Deck-Web-Flasher/firmware/zdeck-2.8.0-zdeck36-public/zdeck-firmware.bin`.
- Confirmed hosted app binary: HTTP `200`, content type `application/octet-stream`, content length `3697280`.
- Endpoint checked: `https://raw.githubusercontent.com/Its-ze/Z-Deck-Web-Flasher/main/PRODUCTION_READINESS_LOG.md`.
- Confirmed public raw readiness log includes the production title, Bluetooth check matrix, and run entries.

Hardware / serial checks:
- Windows serial ports visible: `COM17` as USB VID `303A` PID `1001` T-Deck app-side serial, and `COM3` as USB VID `3402` PID `0900`.
- Second T-Deck was still not visible as an app or bootloader port during this pass.

On-device config checks:
- Page/control area represented by API readback: T-Deck Bluetooth, role, LoRa preset, and GPS configuration.
- `COM17` readback confirmed Bluetooth enabled, Bluetooth mode `0`, role `0` client, LoRa modem preset `0`, and GPS mode `1`.
- No channel names, PSKs, private keys, admin URLs, or full info dumps were read into this log.

Bluetooth checks:
- Windows Bluetooth service `bthserv` was running.
- `DeviceAssociationService` was running.
- Working Bluetooth adapter remained present: `USB\VID_0489&PID_E112\00E04C000001`, status `OK`.
- Second Bluetooth adapter remained in error state: `USB\VID_0B05&PID_1D70\6&D596480&0&2`, status `Error`.
- Python `bleak` BLE scan completed successfully.
- BLE scan result remained `0` advertisements during a 12 second scan window.

Blockers / next check:
- Bluetooth stack is callable and T-Deck Bluetooth config is enabled, but pairing/discovery is not proven because Windows saw zero BLE advertisements.
- Retest after a physical T-Deck reset/replug or after opening the on-device Bluetooth/pairing screen.
- Second T-Deck still requires physical reset/replug before it can be flashed, verified, or added to the checklist.

### 2026-06-13 12:49 -04:00

Scope: second T-Deck recovery/update and public Bluetooth readiness feature.

Changed:
- Added a public `Bluetooth readiness` feature card to the flasher page.
- Appended this run entry after updating the second visible T-Deck.

Repo / release state:
- Public flasher repo head before this entry: `4bed189 Record hourly readiness bluetooth check`.
- Local public repo was clean before this change.

Public web checks:
- Page checked: `https://its-ze.github.io/Z-Deck-Web-Flasher/`.
- Confirmed visible/crawled elements before the edit: `Readiness Log`, `PRODUCTION_READINESS_LOG.md`, `Z-Deck OTA`, `Amber Terminal`, `Slate Signal`, `Arctic High`, and `BACKUP SD`.
- Gap found: the public page did not mention `Bluetooth`, even though Bluetooth is now part of the production-readiness checks.
- Fix added: `Bluetooth readiness` feature card describing adapter checks, BLE scan checks, and T-Deck Bluetooth config checks.
- Endpoint checked: `https://its-ze.github.io/Z-Deck-Web-Flasher/update.json`.
- Confirmed update manifest remained firmware `2.8.0.zdeck36`, pack `0.2.35-cyberdeck`, update mode `app-only`, app size `3697280`, app SHA256 `e7480173d7c7504103ebaf5703a1308a84346c8240ea7a90c261fe7072384a32`.

Hardware / serial checks:
- Windows serial ports visible at start: `COM17`, `COM21`, and `COM3`.
- `COM21` was visible again as USB VID `303A` PID `1001` T-Deck app-side serial.
- `COM21` metadata before update reported firmware `2.8.0.zdeck35`, role `CLIENT`, hardware `T_DECK`.
- `COM21` entered DFU through the Meshtastic admin API and re-enumerated as bootloader port `COM20`.
- First bootloader flash attempt with `--before no-reset` failed before any write with a Windows serial configure error.
- Board returned app-side as `COM21`; a second admin DFU request re-exposed `COM20`.
- App-only flash then succeeded through `flash-latest-tdeck-build.ps1` using build `20260613-072354-t-deck-tft` with LittleFS skipped.
- Esptool hash-verified bootloader, partitions, boot_app0, app slot at `0x10000`, and app slot at `0x650000`.
- `COM21` returned app-side after reset.

On-device config checks:
- `COM21` metadata after update confirmed firmware `2.8.0.zdeck36`, role `CLIENT`, hardware `T_DECK`.
- Non-secret readback confirmed role `0`, LoRa modem preset `0`, GPS mode `1`, display timeout `120`, and Bluetooth enabled.
- No channel names, PSKs, private keys, admin URLs, or full info dumps were stored in this log.

Bluetooth checks:
- After the zdeck36 app-only flash, `COM21` initially read back Bluetooth disabled.
- CLI `--set bluetooth.enabled true` reported success but did not persist on readback.
- Direct Python Meshtastic API write to `localConfig.bluetooth.enabled` plus `writeConfig('bluetooth')` persisted successfully.
- `COM21` readback then confirmed `bluetooth.enabled: True` and `bluetooth.mode: 0`.
- Python `bleak` BLE scan completed successfully but still found `0` advertisements in a 15 second window.

Blockers / next check:
- COM21 is now updated to zdeck36 and has Bluetooth enabled, but Windows BLE discovery still does not see advertisements.
- COM17 was visible but a metadata read hung earlier in this pass; do not stack more serial reads on COM17 until it is physically reset/replugged or it answers a narrow API read.
- Bluetooth pairing still needs an on-device pairing screen/reset test or a known-good phone pairing attempt.

### 2026-06-13 13:07 -04:00

Scope: OTA release verification and app-only update guardrail.

Changed:
- Added `tools/verify-ota-release.py` to validate the public OTA update contract.
- Added `.github/workflows/verify-ota-release.yml` so future update metadata, manifest, and firmware artifact changes are checked in GitHub Actions.

Public OTA checks:
- Page/control represented: on-device `Settings > Z-Deck OTA` block with `CHECK`, `APPLY`, `STATUS`, `BACKUP SD`, and guarded `RESTORE SD`.
- Local command checked: `python tools\verify-ota-release.py`.
- Live command checked: `python tools\verify-ota-release.py --live`.
- Confirmed local and hosted `update.json` describe firmware `2.8.0.zdeck36`, pack `0.2.35-cyberdeck`, update mode `app-only`.
- Confirmed OTA firmware path is `firmware/zdeck-2.8.0-zdeck36-public/zdeck-firmware.bin`, not LittleFS or a factory image.
- Confirmed app size `3697280`, SHA256 `e7480173d7c7504103ebaf5703a1308a84346c8240ea7a90c261fe7072384a32`, and MD5 `56a3cbe5f1f6d323e420edcd234a9563` match local and hosted bytes.
- Confirmed `manifest.json` app slot offsets `0x10000` and `0x650000` point at the same app firmware payload, while LittleFS remains separate at `0xc90000`.
- Confirmed update metadata requires SD pre-update backup at `/zdeck/backups/preferences.proto` and preserves Meshtastic config, channels, keys, owner settings, SD chat journal, and SD settings backup.
- Confirmed installed `0.2.35-cyberdeck` / `2.8.0.zdeck36` devices should report current/no update against this manifest.

Hardware / serial checks:
- Windows serial ports visible during this pass: `COM17`, `COM21`, and `COM3`.
- `COM17` and `COM21` are visible as ESP32-S3/T-Deck app-side serial ports.
- No channel names, PSKs, private keys, admin URLs, Wi-Fi passwords, or full info dumps were stored in this log.

Blockers / next check:
- The custom OTA `CHECK` and `APPLY` handlers are exposed through the T-Deck UI path, not as a Meshtastic serial command, so this pass verified the hosted app-only release bundle and preservation contract but did not remotely press the on-device `APPLY` button.
- ARP did not show a clear T-Deck LAN IP on `192.168.50.0/24`, so there was no reachable network surface to watch the device pull the update.
- To complete the physical OTA apply test, connect the T-Deck to Wi-Fi, open `Settings > Z-Deck OTA`, press `CHECK`, then press `APPLY`; the expected result for zdeck36 already installed is current/no update.

### 2026-06-13 13:12 -04:00

Scope: post-push public deploy, OTA CI, and Bluetooth usability check.

Concrete bug check:
- Verified the public release/deploy did not regress after adding the OTA release verifier.

Public pages / controls checked:
- Page checked: `https://its-ze.github.io/Z-Deck-Web-Flasher/`.
- Confirmed visible/crawled release labels: `2.8.0.zdeck36` and `0.2.35-cyberdeck`.
- Confirmed visible/crawled feature/status labels: `Z-Deck OTA`, `Bluetooth readiness`, `Readiness Log`, `Amber Terminal`, `Slate Signal`, `Arctic High`, and `BACKUP SD`.
- Endpoint checked: `https://its-ze.github.io/Z-Deck-Web-Flasher/update.json` through `python tools\verify-ota-release.py --live`.
- Confirmed app-only OTA metadata, hosted firmware size/hash, SD pre-update backup path, manifest app slot paths, and LittleFS separation all still pass.

GitHub checks:
- Commit checked: `572afad Add OTA release verifier`.
- Workflows checked for that commit: `Verify OTA Release`, `Broken Link Checker`, `Release Drafter`, `pages build and deployment`, `Push on main`, and `CodeQL`.
- Result: all listed workflows completed with `success`.

Hardware / serial checks:
- Windows serial ports visible: `COM17`, `COM21`, and `COM3`.
- `COM17` and `COM21` were visible as USB VID `303A` PID `1001` ESP32-S3/T-Deck app-side serial ports.
- `COM3` remained visible as USB VID `3402` PID `0900`.
- Narrow non-secret Meshtastic read on `COM21` confirmed `bluetooth.enabled: True` and `bluetooth.mode: 0`.
- `COM17` Bluetooth config was not read in this pass because earlier metadata reads on that port hung; avoid stacking serial reads there until physical reset/replug or a narrow read answers cleanly.

Bluetooth checks:
- Windows service `bthserv` was running.
- Windows service `DeviceAssociationService` was running.
- Bluetooth adapter `USB\VID_0489&PID_E112\00E04C000001` was `OK`.
- Bluetooth adapter `USB\VID_0B05&PID_1D70\6&D596480&0&2` remained in `Error` with problem `CM_PROB_FAILED_ADD`.
- Microsoft Bluetooth LE Enumerator was `OK`.
- Python `bleak` scan completed successfully for 12 seconds.
- BLE scan result: `device_count=0`, `named_count=0`, `mesh_like_count=0`.

Blockers / next check:
- Bluetooth stack is callable and COM21 has Bluetooth enabled, but Windows still saw zero BLE advertisements; pairing/discovery is not proven.
- Retest Bluetooth after opening the on-device Bluetooth/pairing screen or physically resetting/replugging the T-Deck.
- OTA `APPLY` still needs a physical on-device `Settings > Z-Deck OTA` button test because the custom OTA path is UI-driven, not serial-driven.

### 2026-06-13 14:14 -04:00

Scope: SD backup/restore guardrails feature verification.

Concrete feature unit:
- Verified the `SD settings backup / restore` feature path is still wired through public release metadata, hosted page copy, on-device OTA controls, and firmware backup/restore code.

Public pages / controls checked:
- Page checked: `https://its-ze.github.io/Z-Deck-Web-Flasher/`.
- Confirmed visible/crawled labels: `SD settings backup`, `BACKUP SD`, `RESTORE SD`, `Z-Deck OTA`, `0.2.35-cyberdeck`, and `2.8.0.zdeck36`.
- Endpoint checked: `https://its-ze.github.io/Z-Deck-Web-Flasher/update.json`.
- Confirmed release metadata: pack `0.2.35-cyberdeck`, firmware `2.8.0.zdeck36`, update mode `app-only`, backup enabled `true`, backup location `sd`, backup path `/zdeck/backups/preferences.proto`, preserve list count `9`, firmware size `3697280`.
- Command checked: `python tools\verify-ota-release.py --live`.
- Confirmed verifier evidence: hosted `update.json` matches local metadata, hosted app firmware size/SHA256/MD5 matches, SD pre-update backup is required, manifest app slots stay separate from LittleFS.

On-device pages / controls represented by source:
- On-device page represented: `Settings > Z-Deck OTA`.
- Controls represented: `CHECK`, `APPLY`, `STATUS`, `BACKUP SD`, `RESTORE SD`.
- Source evidence: `itsz\device-ui-ota-controls.patch` creates `BACKUP SD` and `RESTORE SD` buttons, calls `nodeDB->backupPreferences(...BackupLocation_SD)`, and requires a second `RESTORE SD` press before restore/reboot.
- Source evidence: `src\itsz\ZDeckUpdateService.cpp` calls `nodeDB->backupPreferences(...BackupLocation_SD)` before OTA write.
- Source evidence: `src\mesh\NodeDB.h` defines the SD backup file as `/zdeck/backups/preferences.proto`.
- Source evidence: `src\mesh\NodeDB.cpp` contains SD backup and restore handling for `BackupLocation_SD`.

Hardware / serial checks:
- Windows serial ports visible: `COM17`, `COM21`, and `COM3`.
- `COM17` and `COM21` were visible as USB VID `303A` PID `1001` ESP32-S3/T-Deck app-side serial ports.
- `COM3` remained visible as USB VID `3402` PID `0900`.
- No SD backup file, channel names, PSKs, private keys, admin URLs, Wi-Fi passwords, or full info dumps were read or stored.

Bluetooth checks:
- Windows service `bthserv` was running.
- Windows service `DeviceAssociationService` was running.
- Bluetooth adapter `USB\VID_0489&PID_E112\00E04C000001` was `OK`.
- Bluetooth adapter `USB\VID_0B05&PID_1D70\6&D596480&0&2` remained in `Error` with problem `CM_PROB_FAILED_ADD`.
- Microsoft Bluetooth LE Enumerator was `OK`.
- Python `bleak` scan completed successfully for 12 seconds.
- BLE scan result: `device_count=0`, `named_count=0`, `mesh_like_count=0`.
- Narrow non-secret Meshtastic read on `COM21` confirmed `bluetooth.enabled: True` and `bluetooth.mode: 0`.

GitHub checks:
- Commit checked before this log entry: `822e533 Record deploy and bluetooth readiness check`.
- Workflows checked for that commit: `Broken Link Checker`, `Release Drafter`, `pages build and deployment`, and `Push on main`.
- Result: all listed workflows completed with `success`.

Blockers / next check:
- Physical `BACKUP SD` / `RESTORE SD` button execution was not pressed remotely because the custom controls are on-device UI actions.
- To complete device-side proof, use a T-Deck with SD installed, open `Settings > Z-Deck OTA`, press `BACKUP SD`, confirm the status label reports backup success, then verify restore only proceeds after the second guarded `RESTORE SD` press.
- Bluetooth pairing/discovery remains unproven until a physical pairing/reset check produces BLE advertisements.

### 2026-06-13 15:14 -04:00

Scope: map/GPS/compass feature verification.

Concrete feature unit:
- Verified the current public package still exposes the map/GPS/compass feature stack and that the plugged-in T-Deck still has production GPS config enabled without reading or storing coordinates.

Public pages / controls checked:
- Page checked: `https://its-ze.github.io/Z-Deck-Web-Flasher/`.
- Confirmed visible/crawled labels: `GPS`, `map`, `compass`, `radar`, `distance`, `0.2.35-cyberdeck`, `2.8.0.zdeck36`, and `Z-Deck OTA`.
- Endpoint checked: `https://its-ze.github.io/Z-Deck-Web-Flasher/update.json`.
- Confirmed release notes include GPS/MAP coordinate labels, real compass/radar/alert pages, compact map options, and GPS/map recovery.
- Command checked: `python tools\verify-ota-release.py --live`.
- Confirmed hosted `update.json` and hosted app firmware still match local metadata and hashes for `0.2.35-cyberdeck` / `2.8.0.zdeck36`.

Public source archive checked:
- Archive checked: `source\patches\2026-06-13-zdeck36-public`.
- Confirmed source archive includes `device-ui-map-pages.patch`, `device-ui-map-switching-fix.patch`, `device-ui-map-autocenter.patch`, `device-ui-map-fullscreen.patch`, and `device-ui-compass-pages.patch`.
- Confirmed map pages include `Live compass` / `COMPASS`, `DF/Radar` / `RADAR`, and `Distance alert` / `ALERT`.
- Confirmed fullscreen map descriptions include `GPS fix and nearest node bearing` and `Positioned nodes, nearest range, and scan status`.
- Confirmed auto-center status labels include `CENTER`, `NEXT VIEW`, `Centered on GPS`, and `Waiting for GPS or node positions`.
- Confirmed compass page source creates a dedicated compass/radar panel and uses dynamic compass mode handling.

On-device pages / controls represented:
- On-device page represented: map page stack.
- Controls represented: `NEXT VIEW`, `CENTER`, `COMPASS`, `RADAR`, `ALERT`, map status overlay, and map options area.
- Status labels represented: `GPS off`, `nodes located`, `nodes lack GPS`, `no node coords`, `Centered on GPS`, and `Waiting for GPS or node positions`.

Hardware / serial checks:
- Windows serial ports visible: `COM17`, `COM21`, and `COM3`.
- `COM17` and `COM21` were visible as USB VID `303A` PID `1001` ESP32-S3/T-Deck app-side serial ports.
- `COM3` remained visible as USB VID `3402` PID `0900`.
- Narrow metadata read on `COM21` confirmed firmware `2.8.0.zdeck36`, role `CLIENT`, hardware `T_DECK`.
- Narrow non-secret GPS config read on `COM21` confirmed `position.gps_mode: 1`, `position.rx_gpio: 44`, `position.tx_gpio: 43`, `position.gps_update_interval: 5`, `position.gps_attempt_time: 600`, and `power.is_power_saving: False`.
- No live latitude, longitude, channel names, PSKs, private keys, admin URLs, Wi-Fi passwords, SD backup contents, or full info dumps were read or stored.

Bluetooth checks:
- Windows service `bthserv` was running.
- Windows service `DeviceAssociationService` was running.
- Bluetooth adapter `USB\VID_0489&PID_E112\00E04C000001` was `OK`.
- Bluetooth adapter `USB\VID_0B05&PID_1D70\6&D596480&0&2` remained in `Error` with problem `CM_PROB_FAILED_ADD`.
- Microsoft Bluetooth LE Enumerator was `OK`.
- Python `bleak` scan completed successfully for 12 seconds.
- BLE scan result: `device_count=0`, `named_count=0`, `mesh_like_count=0`.
- Narrow non-secret Meshtastic read on `COM21` confirmed `bluetooth.enabled: True` and `bluetooth.mode: 0`.

GitHub checks:
- Commit checked before this log entry: `be6eb7a Record SD guardrail readiness check`.
- Workflows checked for that commit: `Broken Link Checker`, `Release Drafter`, `pages build and deployment`, and `Push on main`.
- Result: all listed workflows completed with `success`.

Blockers / next check:
- Physical map/compass screen rendering was not visually inspected on the T-Deck during this pass.
- GPS lock quality and live position were not read to avoid storing location data in the log.
- To complete device-side proof, open the T-Deck map stack, cycle `NEXT VIEW` through `COMPASS`, `RADAR`, and `ALERT`, press `CENTER`, and confirm the status label changes from waiting to centered when GPS or positioned nodes are available.
- Bluetooth pairing/discovery remains unproven until a physical pairing/reset check produces BLE advertisements.
