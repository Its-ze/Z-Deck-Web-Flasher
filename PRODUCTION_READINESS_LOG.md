# Z-Deck Production Readiness Log

This file is the running checklist for hourly T-Deck/Z-Deck production readiness passes.

Rules for each run:
- Preserve LittleFS, SD settings backups, private channels, admin settings, owner names, and chat data unless the task explicitly requires changing them.
- Do not store PSKs, private keys, admin channel URLs, full Meshtastic info dumps, or raw backup contents here.
- Each run must either add one scoped feature/improvement or complete one concrete bug check with evidence.
- Record exact pages, controls, status labels, hardware ports, and visible elements checked.
- Separate confirmed behavior from blockers that require physical reset, replug, pairing approval, GPS sky view, or another external action.

## 2026-07-11 - zdeck52 Validated Dual-Mesh Quick Handoff

- Feature/fix: fast switching between Z-Deck/Meshtastic app 0 and MeshCore app 1 without reflashing or erasing shared storage.
- Z-Deck Home control: compact `MESH >` button in `TopPanel`, positioned left of the centered logo/title and outside the sidebar and 64 px battery safe lane.
- Z-Deck Settings control: full-width `MESHCORE >` in `Settings > Z-Deck OTA`; one press validates MeshCore, displays transition status, selects app 1, disables duplicate input, and schedules reboot after 750 ms.
- MeshCore control: `Z-Deck` Home page displays `hot switch`; Enter or trackball long-press/release validates app 0, requires `appDesc.version` to contain `zdeck`, selects app 0, and reboots.
- Architecture boundary: this is a quick A/B reboot handoff, not simultaneous protocol execution. Meshtastic and MeshCore require exclusive LoRa-radio ownership.
- Storage boundary: handoff uses `esp_ota_set_boot_partition` only. No NVS, LittleFS, SD, channel, key, owner, chat, map, or layout partition is written.
- Z-Deck build evidence: full WSL PlatformIO `t-deck-tft` app and `buildfs` targets passed; binary contains `2.8.0.zdeck52`, `0.2.51-cyberdeck`, `MESH >`, `MESHCORE >`, and the transition status.
- MeshCore build evidence: `LilyGo_TDeck_companion_radio_usb` passed; app size `624864` and binary contains `hot switch`, `release: switching`, `App0 is not Z-Deck`, and `Booting Z-Deck`.
- Artifact evidence: Z-Deck app size `3713424`, SHA256 `5a278b5b6ba4a888297a1f0d14a93af66f4350ee65a82ddd4aed80f67f068d48`; MeshCore app SHA256 `a5680eb4644864acf3311ac9e34eaa153942b769969bde0c927559609ef54730`.
- Release validation: `verify-ota-release.py` passed the app-only OTA path, size/hash metadata, required preservation list, SD preflight backup contract, and current-version comparison. `verify-dual-release.py` passed bootloader, partition table, app 0 at `0x10000`, and MeshCore app 1 at `0x650000`; no storage partition is written.
- Public flasher page checked locally at desktop `1280x720` and mobile `390x844`: `Z-Deck 0.2.51-cyberdeck`, `2.8.0.zdeck52`, the `Z-Deck + MeshCore` layout tab, storage `Not written`, and both switch directions were visible. Both viewports had zero horizontal overflow and the browser console had no errors.
- Release-scoped secret scan passed for manifests, page copy, source archive, and patch files; no private channel data or credentials are included.
- Remaining physical check: install the dual zdeck52 package on a verified T-Deck, switch Z-Deck to MeshCore, then use MeshCore's Z-Deck page to return and confirm both network configurations remain intact.

## 2026-07-11 - zdeck51 UI Audit And Map State Rebuild

- Feature/fix: replaced shared map page/centering flags with `ZDeckMapState`, a standalone C++17 controller for page selection, manual interaction, first-fix GPS recovery, center source, and tile state.
- On-device pages checked in composed source: Home, Nodes, Node Options, Groups, Group Chat, Chats, Messages, Map, Controller, Settings, Advanced Settings, Mesh Detector, Signal Scanner, Trace Route, Details, Statistics, Packet Log, Initial Setup, and their top status panels.
- Layout controls checked: left/right 36 px sidebar, 4 px content gutter, 64 px battery safe lane, bounded 85% message composer plus keyboard button, top panels, settings tool controls, map location/status overlays, GPS lock, zoom buttons, OSD, and pan pad.
- Map controls added: persistent bottom `MAP`, `COMP`, `RADAR`, and `ALERT` buttons. The 30 px bar is outside the 186 px compass/radar tool surface; the 99 px pan pad is raised above it; the 180 px OSD ends above it.
- GPS behavior: live GPS wins over saved-home and peer-cluster fallbacks; fallback centering remains pending when GPS is expected; manual pan/zoom cancels snapping; Follow GPS resumes it immediately.
- Distance/tile behavior: mesh nearest-node range now uses the same latitude-aware distance helper as DeFlock; tile state is classified once as closed, drawing, missing, ready, online, SD, or grid.
- Build evidence: ESP32-S3 controller and test translation units compiled with `-Wall -Wextra -Werror`; the full WSL PlatformIO `t-deck-tft` app and `buildfs` targets passed for `2.8.0.zdeck51` / `0.2.50-cyberdeck`.
- Artifact evidence: app size `3713312`, SHA256 `ca20c8b842e29cc78eb0f0d695cfc1d241bf94826eb0be23d05da56218abb997`, MD5 `2e6dcadc9f419ca26526981151d7f828`.
- Storage boundary: OTA metadata references only `zdeck-firmware.bin`; it does not write NVS, LittleFS, SD, app 1, private settings, channels, keys, chats, map defaults, or sidebar preferences.
- Public page evidence: local page loaded `0.2.50-cyberdeck` / `2.8.0.zdeck51`, both standard and dual installer tabs switched correctly, the 390 px layout had no horizontal overflow or clipped controls, and the browser console had no errors.
- Live release evidence: GitHub Pages served zdeck51 `update.json`; the hosted app size, SHA256, and MD5 matched local release metadata and `tools/verify-ota-release.py --live` passed.
- Hardware blocker: Windows exposed `COM9` via CP210x and `COM3`, but no native T-Deck `303A:1001` app port. A narrow read-only Meshtastic metadata probe did not identify `COM9`, so no device write was attempted.
- Remaining physical checks: reconnect the T-Deck in app or verified ESP32-S3 bootloader mode, install app-only zdeck51, inspect all four map modes on the display, obtain an outdoor GPS fix, pan then enable Follow GPS, and confirm mode/button touch targets on hardware.

## 2026-07-11 - zdeck50 Dual-System Switch And Flasher Workspace

- Feature/fix: guarded Z-Deck app 0 to MeshCore app 1 switching, MeshCore return-to-Z-Deck page, separate dual browser installer, and modernized public flasher workspace.
- On-device page changed: `Settings > Z-Deck OTA`; added full-width `SWITCH TO MESHCORE` below `CHECK`, `APPLY`, `STATUS`, `BACKUP SD`, and `RESTORE SD`.
- Guardrail evidence: first switch press arms confirmation; second press validates app 1 and reboots. App 1 must be bootable and contain the MeshCore image marker in its first 2048 bytes. The bundled MeshCore image marker is at `0x4f8`; the Z-Deck image's first marker is at `0xc9006`, so a standard Z-Deck recovery slot is rejected.
- Build evidence: WSL PlatformIO `t-deck-tft` app and `buildfs` targets passed for firmware `2.8.0.zdeck50` / pack `0.2.49-cyberdeck`; app size `3713824` bytes, SHA256 `53cd50bf20eac9408db1c7cd187c7e517237ee77953ee521fe75a3dbbdbbcf4a`.
- Device evidence: attached T-Deck app 0 flashed and hash-verified at `0x10000` on `COM20`; write range ended before app 1 and no NVS/LittleFS/SD address was written. It returned in app mode on `COM21`.
- Runtime evidence: narrow Meshtastic readback reported `firmware_version: 2.8.0.zdeck50`, hardware `T_DECK`, role `CLIENT`, GPS mode enabled, and GPS update interval `5`.
- OTA evidence: the updated T-Deck accepted the redacted USB `itsz zdeck ota check` command and reported `OTA: Z-Deck is current` against the hosted zdeck50 manifest; no apply/write was requested.
- Public page checked locally at `http://127.0.0.1:4174/`: `Z-Deck` and `Z-Deck + MeshCore` tabs, standard and dual install buttons, write maps, dual switch instructions, recovery buttons, VoidLink controls, feature list, release metadata, and installer ticker.
- Responsive evidence: desktop screenshot and 390 px mobile screenshot showed no horizontal overflow; install controls stayed within the viewport and the mode panels switched with correct selected/hidden state.
- Manifest evidence: `tools/verify-ota-release.py` passed app-only size/SHA256/MD5 and storage-preservation checks; `tools/verify-dual-release.py` passed exact offsets `0x0`, `0x8000`, `0xe000`, `0x10000`, and `0x650000` and confirmed no storage partition is written.
- Flash-helper evidence: generated dual package validates all five SHA256 values, parses successfully, and completes dry run. The helper now uses `usb-reset`, defaults to `460800`, and throws on nonzero `esptool` exit.
- Security boundary: no PSK, channel URL, private key, Wi-Fi password, owner value, raw backup, or full Meshtastic info output was printed or added.
- Remaining physical check: use the on-device control to enter MeshCore and the MeshCore `Z-Deck` page to return; this requires direct keyboard/display interaction and was not forced over USB during this run.

## 2026-06-16 - zdeck38 SD Backup/Restore Decode Hotfix

- Feature/fix: `Settings > Z-Deck OTA` `BACKUP SD`, guarded `RESTORE SD`, and OTA preflight settings backup verification.
- Root cause found in firmware source: SD backup restore/verify decoded `/zdeck/backups/preferences.proto` with `meshtastic_BackupPreferences_size` instead of the actual file size, so valid shorter protobuf files could fail decode at EOF.
- Code change: `src/mesh/NodeDB.cpp` now checks the SD file size, rejects empty or oversized backups, and passes the actual byte count into `pb_decode`.
- Build evidence: WSL PlatformIO build completed for `t-deck-tft`; exported build folder `F:\Dropbox\Dev Ops\T-Deck\firmware\builds\20260616-113921-t-deck-tft`.
- Release evidence staged locally: firmware `2.8.0.zdeck38`, pack `0.2.37-cyberdeck`, app size `3697632`, SHA256 `b4d2d77e89c4abb0a973ae94e79f923cafe2f1b67547f6e031c52388ce9c7b14`.
- Public page evidence checked locally at `http://127.0.0.1:4173/`: title `Z-Deck Firmware Pack Public`, H1 `Flash Z-Deck 0.2.37`, visible `zdeck38`/`Z38`, visible `/zdeck/backups/preferences.proto`, and no captured console errors.
- Public pages/files touched: `index.html`, `app.js`, `README.md`, `CHANGELOG.md`, `PRIVACY.md`, `manifest.json`, `update.json`, `firmware/zdeck-2.8.0-zdeck38-public`, `source/patches/2026-06-16-zdeck38-public`, and `source/patches/patch-manifest.json`.
- Security boundary: no raw backup file, PSK, private key, admin URL, Wi-Fi password, full `--info`, or owner-specific private settings were printed or bundled.
- Remaining physical check: install zdeck38 on a T-Deck with SD inserted, press `BACKUP SD`, confirm the status label reports success, then use the second guarded `RESTORE SD` press only when ready to reboot and verify restored settings.

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

### 2026-06-13 16:16 -04:00

Scope: chat ordering/send-status/hop counter feature verification.

Concrete feature unit:
- Verified the current public package still exposes newest-first chats, stable node names, send status, and hop counters through live page/release metadata, the zdeck36 public source archive, OTA verifier evidence, and non-secret T-Deck config readback.

Public pages / controls checked:
- Page checked: `https://its-ze.github.io/Z-Deck-Web-Flasher/`.
- Confirmed visible/crawled labels: `chat`, `newest-first`, `send status`, `hop`, `node names`, `0.2.35-cyberdeck`, and `2.8.0.zdeck36`.
- Endpoint checked: `https://its-ze.github.io/Z-Deck-Web-Flasher/update.json`.
- Confirmed release notes include newest-first chats, stable node names, send status, and hop counters.
- Command checked: `python tools\verify-ota-release.py --live`.
- Confirmed verifier evidence: hosted `update.json` matches local metadata, hosted app firmware size/SHA256/MD5 matches, SD pre-update backup is required, and app slots stay separate from LittleFS.

Public source archive checked:
- Archive checked: `source\patches\2026-06-13-zdeck36-public`.
- Confirmed files: `device-ui-delivery-status.patch`, `device-ui-state-diagnostics.patch`, and `device-ui-sd-message-journal.patch`.
- Confirmed delivery-status patch passes hop data through chat message creation and text-message response handling.
- Confirmed status labels represented in source: `WAIT ACK`, `BCAST TTL`, `TX ACK`, `TX HEARD`, `NO ACK`, `RX CH`, `H?`, and `TTL`.
- Confirmed source archive README lists chat ordering, send status, and hop counters in the public-safe stack.
- No chat bodies, node lists, channel names, PSKs, private keys, admin URLs, Wi-Fi passwords, SD backup contents, or full info dumps were read or stored.

On-device pages / controls represented:
- On-device pages represented: chat list, chats page, message panel, group chat page, and message status label.
- Controls/status labels represented: send path status, latest chat ordering, ACK wait status, broadcast TTL status, ACK/heard/no-ACK status, and hop/TTL counters.

Hardware / serial checks:
- Windows serial ports visible: `COM17`, `COM21`, and `COM3`.
- `COM17` and `COM21` were visible as USB VID `303A` PID `1001` ESP32-S3/T-Deck app-side serial ports.
- `COM3` remained visible as USB VID `3402` PID `0900`.
- Narrow metadata read on `COM21` confirmed firmware `2.8.0.zdeck36`, role `CLIENT`, and hardware `T_DECK`.
- Narrow non-secret config read on `COM21` confirmed `device.role: 0`, `display.screen_on_secs: 120`, `lora.hop_limit: 3`, and `lora.modem_preset: 0`.

Bluetooth checks:
- Windows service `bthserv` was running.
- Windows service `DeviceAssociationService` was running.
- Bluetooth adapter `USB\VID_0489&PID_E112\00E04C000001` was `OK`.
- Bluetooth adapter `USB\VID_0B05&PID_1D70\6&D596480&0&2` remained in `Error`.
- Microsoft Bluetooth LE Enumerator was `OK`.
- Python `bleak` scan completed successfully for 12 seconds.
- BLE scan result: `device_count=0`.
- Narrow non-secret Meshtastic read on `COM21` confirmed `bluetooth.enabled: True` and `bluetooth.mode: 0`.

GitHub checks:
- Commit checked before this log entry: `669ed2c Record map GPS compass readiness check`.
- Workflows checked for that commit: `Scheduled`, `Broken Link Checker`, `Release Drafter`, `pages build and deployment`, and `Push on main`.
- Result: all listed workflows completed with `success`.

Blockers / next check:
- Physical chat ordering/status rendering was not visually inspected on the T-Deck screen during this pass.
- No live send/receive test was run to avoid unsolicited mesh traffic; next safe proof is an approved short LongFast/private two-device test that verifies latest chat ordering and status transitions.
- Bluetooth pairing/discovery remains unproven until a physical pairing/reset check produces BLE advertisements.

### 2026-06-13 17:14 -04:00

Scope: Wi-Fi scan/select setup feature verification.

Concrete feature unit:
- Verified the current public package still exposes the on-device Wi-Fi scan/select setup path through the live public page, live OTA metadata, source archive, OTA verifier, and non-secret T-Deck readback.

Public pages / controls checked:
- Page checked: `https://its-ze.github.io/Z-Deck-Web-Flasher/`.
- Confirmed visible/crawled labels: `Wi-Fi`, `Scan`, `select`, `settings`, `Z-Deck OTA`, `0.2.35-cyberdeck`, and `2.8.0.zdeck36`.
- Endpoint checked: `https://its-ze.github.io/Z-Deck-Web-Flasher/update.json`.
- Confirmed release metadata: pack `0.2.35-cyberdeck`, firmware `2.8.0.zdeck36`, update mode `app-only`, and notes include `Wi-Fi scan/select`.
- Command checked: `python tools\verify-ota-release.py --live`.
- Confirmed verifier evidence: hosted `update.json` matches local metadata, hosted app firmware size/SHA256/MD5 matches, SD pre-update backup is required, and app slots stay separate from LittleFS.

Public source archive checked:
- Archive checked: `source\patches\2026-06-13-zdeck36-public`.
- Confirmed Wi-Fi scan/select source symbols: `wifiScanButton`, `wifiNetworkDropdown`, `wifiScanStatusLabel`, `scanWifiNetworks`, `ui_event_wifi_scan_button`, and `ui_event_wifi_network_dropdown`.
- Confirmed Wi-Fi setup labels/statuses represented in source: `SCAN`, `WAIT`, `Press Scan`, `Scanning...`, `Scanning nearby WiFi...`, `Found %u networks. Pick one.`, `No networks found`, `Scan unavailable`, `Open network selected. Press OK.`, and `Network selected. Enter password, then OK.`
- Confirmed source event path writes selected network text into the existing Wi-Fi SSID field and focuses the password field for secured networks.
- No SSIDs, Wi-Fi passwords, channel names, PSKs, private keys, admin URLs, SD backup contents, node lists, messages, or full info dumps were read or stored.

On-device pages / controls represented:
- On-device pages represented: settings Wi-Fi panel, map/internet Wi-Fi button path, and Settings/Z-Deck OTA network status surface.
- Controls/status labels represented: Wi-Fi button, `SCAN` button, Wi-Fi network dropdown, SSID field, password field, scan status label, `OK` action, `WIFI`, `SET WIFI`, `EDIT WIFI`, `WIFI ON`, `WIFI OFF`, and `NO WIFI`.

Hardware / serial checks:
- Windows serial ports visible: `COM17`, `COM21`, and `COM3`.
- `COM17` and `COM21` were visible as USB VID `303A` PID `1001` ESP32-S3/T-Deck app-side serial ports.
- `COM3` remained visible as USB VID `3402` PID `0900`.
- Narrow metadata read on `COM21` returned firmware `2.8.0.zdeck36`, role `CLIENT`, and hardware `T_DECK`.
- Narrow non-secret config read on `COM21` confirmed `device.role: 0`, `display.screen_on_secs: 120`, `lora.hop_limit: 3`, and `lora.modem_preset: 0`.

Bluetooth checks:
- Windows service `bthserv` was running.
- Windows service `DeviceAssociationService` was running.
- Bluetooth adapter `USB\VID_0489&PID_E112\00E04C000001` was `OK`.
- Bluetooth adapter `USB\VID_0B05&PID_1D70\6&D596480&0&2` remained in `Error`.
- Microsoft Bluetooth LE Enumerator was `OK`.
- Python `bleak` scan completed successfully for 12 seconds.
- BLE scan result: `device_count=0`.
- Narrow non-secret Meshtastic read on `COM21` confirmed `bluetooth.enabled: True` and `bluetooth.mode: 0`.

GitHub checks:
- Commit checked before this log entry: `233fc69 Record chat status readiness check`.
- Workflows checked for that commit: `Release Drafter`, `Broken Link Checker`, `pages build and deployment`, and `Push on main`.
- Result: all listed workflows completed with `success`.

Blockers / next check:
- Physical `SCAN` button execution and dropdown selection were not pressed on the T-Deck screen during this pass.
- No live Wi-Fi SSID/password config read was performed by design because those values are private.
- Next safe proof is to open the on-device Wi-Fi settings panel, press `SCAN`, confirm the status changes through `WAIT`/`Scanning...`, pick a visible network from the dropdown, and confirm it fills the SSID field without revealing or logging the network password.
- Bluetooth pairing/discovery remains unproven until a physical pairing/reset check produces BLE advertisements.

### 2026-06-13 18:13 -04:00

Scope: on-device selectable themes feature verification.

Concrete feature unit:
- Verified the current public package still exposes the selectable on-device theme stack, including `Amber Terminal`, `Slate Signal`, and `Arctic High`, through the live public page, live OTA metadata, source archive, OTA verifier, and non-secret T-Deck readback.

Public pages / controls checked:
- Page checked: `https://its-ze.github.io/Z-Deck-Web-Flasher/`.
- Confirmed visible/crawled labels: `theme`, `themes`, `Amber Terminal`, `Slate Signal`, `Arctic High`, `Z-Deck OTA`, `0.2.35-cyberdeck`, and `2.8.0.zdeck36`.
- Endpoint checked: `https://its-ze.github.io/Z-Deck-Web-Flasher/update.json`.
- Confirmed release metadata: pack `0.2.35-cyberdeck`, firmware `2.8.0.zdeck36`, update mode `app-only`, and notes state that the build adds three selectable on-device screen themes.
- Command checked: `python tools\verify-ota-release.py --live`.
- Confirmed verifier evidence: hosted `update.json` matches local metadata, hosted app firmware size/SHA256/MD5 matches, SD pre-update backup is required, and app slots stay separate from LittleFS.

Public source archive checked:
- Archive checked: `source\patches\2026-06-13-zdeck36-public`.
- Confirmed theme definitions: `ThemeID::AmberTerminal`, `ThemeID::SlateSignal`, `ThemeID::ArcticHigh`, and existing `ThemeID::Q10Classic`.
- Confirmed theme names represented in source: `Amber Terminal`, `Slate Signal`, and `Arctic High`.
- Confirmed theme menu/source path: `ThemeMenu`, `themeMenu()`, `Q10 Classic Theme`, and `kThemes`.
- Confirmed source archive README states that existing theme IDs remain stable and saved configs continue to resolve safely.
- No channel names, PSKs, private keys, admin URLs, Wi-Fi passwords, SD backup contents, node lists, messages, or full info dumps were read or stored.

On-device pages / controls represented:
- On-device pages represented: display/theme menu, home screen theme rendering, map/compass pages that include `Themes.h`, and Settings/Z-Deck OTA release status surface.
- Controls/status labels represented: theme menu entry, selectable theme rows, active theme rendering, `Amber Terminal`, `Slate Signal`, `Arctic High`, `Q10 Classic Theme`, and release current/status text.

Hardware / serial checks:
- Windows serial ports visible: `COM17`, `COM21`, and `COM3`.
- `COM17` and `COM21` were visible as USB VID `303A` PID `1001` ESP32-S3/T-Deck app-side serial ports.
- `COM3` remained visible as USB VID `3402` PID `0900`.
- Narrow metadata read on `COM21` returned firmware `2.8.0.zdeck36`, role `CLIENT`, and hardware `T_DECK`.
- Narrow non-secret config read on `COM21` confirmed `device.role: 0`, `display.screen_on_secs: 120`, `lora.hop_limit: 3`, `lora.modem_preset: 0`, `bluetooth.enabled: True`, and `bluetooth.mode: 0`.

Bluetooth checks:
- Windows service `bthserv` was running.
- Windows service `DeviceAssociationService` was running.
- Bluetooth adapter `USB\VID_0489&PID_E112\00E04C000001` was `OK`.
- Bluetooth adapter `USB\VID_0B05&PID_1D70\6&D596480&0&2` remained in `Error`.
- Microsoft Bluetooth LE Enumerator was `OK`.
- Python `bleak` scan completed successfully for 12 seconds.
- BLE scan result: `device_count=0`.
- Narrow non-secret Meshtastic read on `COM21` confirmed `bluetooth.enabled: True` and `bluetooth.mode: 0`.

GitHub checks:
- Commit checked before this log entry: `3faa506 Record wifi setup readiness check`.
- Workflows checked for that commit: `Release Drafter`, `Broken Link Checker`, `pages build and deployment`, and `Push on main`.
- Result: all listed workflows completed with `success`.

Blockers / next check:
- Physical theme menu navigation and visual switching were not performed on the T-Deck screen during this pass.
- Next safe proof is to open the on-device theme menu, select each of `Amber Terminal`, `Slate Signal`, and `Arctic High`, and confirm the home/map/chat/status pages repaint without clipped text or overlap.
- Bluetooth pairing/discovery remains unproven until a physical pairing/reset check produces BLE advertisements.

### 2026-06-13 19:15 -04:00

Scope: on-device diagnostics/state surface feature verification.

Concrete feature unit:
- Verified the current public package still exposes the Z-Deck diagnostics/state surface through the live public page, live OTA metadata, source archive, OTA verifier, workflow status, and non-secret T-Deck readback.

Public pages / controls checked:
- Page checked: `https://its-ze.github.io/Z-Deck-Web-Flasher/`.
- Confirmed visible/crawled labels: `diagnostics`, `diagnostic`, `status`, `state`, `Z-Deck OTA`, `0.2.35-cyberdeck`, and `2.8.0.zdeck36`.
- Endpoint checked: `https://its-ze.github.io/Z-Deck-Web-Flasher/update.json`.
- Confirmed release metadata: pack `0.2.35-cyberdeck`, firmware `2.8.0.zdeck36`, update mode `app-only`, and notes include `diagnostics`.
- Command checked: `python tools\verify-ota-release.py --live`.
- Confirmed verifier evidence: hosted `update.json` matches local metadata, hosted app firmware size/SHA256/MD5 matches, SD pre-update backup is required, and app slots stay separate from LittleFS.

Public source archive checked:
- Archive checked: `source\patches\2026-06-13-zdeck36-public`.
- Confirmed diagnostics patch: `device-ui-state-diagnostics.patch`.
- Confirmed diagnostics controls/statuses represented in source: `Z-Deck Diagnostics`, `Z-Deck diagnostics refreshed`, `Primary:`, `SD`, `WiFi`, `nodes`, and `stateLines`.
- Confirmed state model symbols represented in source: `ZDeckStateModel`, `formatCompact`, `formatDiagnostics`, `formatLine`, `setOta`, `setSd`, `setMap`, and `setChat`.
- Confirmed subsystem labels represented in source: `OTA`, `SD`, `Map`, and `Chat`.
- Confirmed state tokens represented in source: `READY`, `BUSY`, `WAIT`, `WARN`, and `ERR`.
- Confirmed initial state messages represented in source: `No update check yet.`, `SD state not checked.`, `Map not opened yet.`, and `No chat activity yet.`
- No channel names, PSKs, private keys, admin URLs, Wi-Fi passwords, SD backup contents, node lists, messages, or full info dumps were read or stored.

On-device pages / controls represented:
- On-device pages represented: Z-Deck diagnostics panel, SD tool panel, Settings/Z-Deck OTA panel, map status overlay, and chat status/state hooks.
- Controls/status labels represented: `Z-Deck Diagnostics` button, diagnostics refreshed alert, compact subsystem state lines, OTA progress/error state, SD backup/restore/prepare state, map ready/waiting/warning state, and chat activity state.

Hardware / serial checks:
- Windows serial ports visible: `COM17`, `COM21`, and `COM3`.
- `COM17` and `COM21` were visible as USB VID `303A` PID `1001` ESP32-S3/T-Deck app-side serial ports.
- `COM3` remained visible as USB VID `3402` PID `0900`.
- Narrow metadata read on `COM21` returned firmware `2.8.0.zdeck36`, role `CLIENT`, and hardware `T_DECK`.
- Narrow non-secret config read on `COM21` confirmed `device.role: 0`, `display.screen_on_secs: 120`, `lora.hop_limit: 3`, `lora.modem_preset: 0`, `bluetooth.enabled: True`, and `bluetooth.mode: 0`.

Bluetooth checks:
- Windows service `bthserv` was running.
- Windows service `DeviceAssociationService` was running.
- Bluetooth adapter `USB\VID_0489&PID_E112\00E04C000001` was `OK`.
- Bluetooth adapter `USB\VID_0B05&PID_1D70\6&D596480&0&2` remained in `Error`.
- Microsoft Bluetooth LE Enumerator was `OK`.
- Python `bleak` scan completed successfully for 12 seconds.
- BLE scan result: `device_count=0`.
- Narrow non-secret Meshtastic read on `COM21` confirmed `bluetooth.enabled: True` and `bluetooth.mode: 0`.

GitHub checks:
- Commit checked before this log entry: `2536c87 Record theme readiness check`.
- Workflows checked for that commit: `Broken Link Checker`, `Release Drafter`, `pages build and deployment`, and `Push on main`.
- Result: all listed workflows completed with `success`.

Blockers / next check:
- Physical `Z-Deck Diagnostics` button execution was not pressed on the T-Deck screen during this pass.
- Next safe proof is to open the diagnostics panel on-device, press/refresh it, and confirm the OTA/SD/Map/Chat rows update without clipped text or overlap while avoiding any secret-bearing details.
- Bluetooth pairing/discovery remains unproven until a physical pairing/reset check produces BLE advertisements.

### 2026-06-13 20:15 -04:00

Scope: battery/header/sidebar overlap guardrail verification.

Concrete feature unit:
- Verified the current public package still exposes the battery/header/sidebar overlap fixes through the live public page, live OTA metadata, source archive, OTA verifier, workflow status, and non-secret T-Deck readback.

Public pages / controls checked:
- Page checked: `https://its-ze.github.io/Z-Deck-Web-Flasher/`.
- Confirmed visible/crawled labels: `battery`, `header`, `sidebar`, `overlap`, `Z-Deck OTA`, `0.2.35-cyberdeck`, and `2.8.0.zdeck36`.
- Endpoint checked: `https://its-ze.github.io/Z-Deck-Web-Flasher/update.json`.
- Confirmed release metadata: pack `0.2.35-cyberdeck`, firmware `2.8.0.zdeck36`, update mode `app-only`, preserve list includes `sidebar_layout`, and notes include `battery/header/sidebar fixes`.
- Command checked: `python tools\verify-ota-release.py --live`.
- Confirmed verifier evidence: hosted `update.json` matches local metadata, hosted app firmware size/SHA256/MD5 matches, SD pre-update backup is required, and app slots stay separate from LittleFS.

Public source archive checked:
- Archive checked: `source\patches\2026-06-13-zdeck36-public`.
- Confirmed README states this release keeps `battery/header/sidebar fixes`.
- Confirmed sidebar files: `device-ui-sidebar-layout.patch` and `device-ui-sidebar-overlap-fix.patch`.
- Confirmed sidebar controls/statuses represented in source: `Sidebar: right`, `Sidebar: left`, `zDeckSidebarButton`, `/zdeck_sidebar.cfg`, `zDeckSidebarWidth`, `zDeckSidebarGutter`, `zDeckSidebarContentWidth`, `zDeckSidebarRightX`, and fixed placement for top/header panels.
- Confirmed home overlap guardrail: `device-ui-home-layout-fix.patch` moves `HomeSignalLabel` to `42,42`, widens it to `LV_PCT(80)`, and keeps `HomeSignalPctLabel` inside a bounded row.
- Confirmed header/battery guardrails in full source patch: `drawBoundedHeaderTitle`, reserved left/right header lanes, `hasBattery`, `displayChargePercent`, `showUsbOnly`, clamped battery fill dimensions, visible battery percent text, and `statusLeftEndX` reserved before drawing the title.
- Confirmed public page copy states the right-side sidebar keeps top panels clear of the rail and the home header clips owner title between the battery/percent block and right-side status icons.
- No channel names, PSKs, private keys, admin URLs, Wi-Fi passwords, SD backup contents, node lists, messages, or full info dumps were read or stored.

On-device pages / controls represented:
- On-device pages represented: home screen, common header/status bar, top panels, basic settings sidebar placement control, map/chat/settings top panels, and Settings/Z-Deck OTA release status surface.
- Controls/status labels represented: battery icon, battery percent text, owner/header title, right-side status icons, navigation/sidebar rail, `Sidebar: right`, `Sidebar: left`, `HomeSignalLabel`, `HomeSignalPctLabel`, and `Z-Deck OTA`.

Hardware / serial checks:
- Windows serial ports visible: `COM17`, `COM21`, and `COM3`.
- `COM17` and `COM21` were visible as USB VID `303A` PID `1001` ESP32-S3/T-Deck app-side serial ports.
- `COM3` remained visible as USB VID `3402` PID `0900`.
- Narrow metadata read on `COM21` returned firmware `2.8.0.zdeck36`, role `CLIENT`, and hardware `T_DECK`.
- Narrow non-secret config read on `COM21` confirmed `device.role: 0`, `display.screen_on_secs: 120`, `lora.hop_limit: 3`, `lora.modem_preset: 0`, `power.is_power_saving: False`, `bluetooth.enabled: True`, and `bluetooth.mode: 0`.

Bluetooth checks:
- Windows service `bthserv` was running.
- Windows service `DeviceAssociationService` was running.
- Bluetooth adapter `USB\VID_0489&PID_E112\00E04C000001` was `OK`.
- Bluetooth adapter `USB\VID_0B05&PID_1D70\6&D596480&0&2` remained in `Error`.
- Microsoft Bluetooth LE Enumerator was `OK`.
- Python `bleak` scan completed successfully for 12 seconds.
- BLE scan result: `device_count=0`.
- Narrow non-secret Meshtastic read on `COM21` confirmed `bluetooth.enabled: True` and `bluetooth.mode: 0`.

GitHub checks:
- Commit checked before this log entry: `6e25881 Record diagnostics readiness check`.
- Workflows checked for that commit: `Broken Link Checker`, `Release Drafter`, `pages build and deployment`, and `Push on main`.
- Result: all listed workflows completed with `success`.

Blockers / next check:
- Physical home/header/sidebar rendering was not visually inspected on the T-Deck screen during this pass.
- Next safe proof is to inspect the home screen and several top-panel pages on-device with the sidebar on both left and right, confirming the battery percent, owner title, right status icons, Home RX row, and navigation rail do not overlap.
- Bluetooth pairing/discovery remains unproven until a physical pairing/reset check produces BLE advertisements.

### 2026-06-13 21:16 -04:00

Scope: public GitHub Pages artifact and release traceability verification.

Concrete feature unit:
- Verified the current public artifact set for `0.2.35-cyberdeck` / `2.8.0.zdeck36` end-to-end and added the missing public Git tag anchor for this package.

Public pages / controls checked:
- Page checked: `https://its-ze.github.io/Z-Deck-Web-Flasher/`.
- Confirmed live page HTTP content includes `Z-Deck Web Flasher`, `0.2.35-cyberdeck`, `2.8.0.zdeck36`, `Install`, `Web Serial`, `Z-Deck OTA`, `features`, and `source`.
- Endpoint checked: `https://its-ze.github.io/Z-Deck-Web-Flasher/update.json`.
- Confirmed `update.json` returned HTTP `200`, content type `application/json; charset=utf-8`, pack `0.2.35-cyberdeck`, firmware `2.8.0.zdeck36`, update mode `app-only`, firmware URL over HTTPS, firmware size `3697280`, SD backup enabled, and backup path `/zdeck/backups/preferences.proto`.
- Endpoint checked: hosted firmware binary URL from `update.json`.
- Confirmed firmware `HEAD` returned HTTP `200`, content type `application/octet-stream`, and content length `3697280`.
- Command checked: `python tools\verify-ota-release.py --live`.
- Confirmed verifier evidence: hosted `update.json` matches local metadata, hosted app firmware size/SHA256/MD5 matches, SD pre-update backup is required, and app slots stay separate from LittleFS.

Public source / package artifacts checked:
- Firmware package checked: `firmware\zdeck-2.8.0-zdeck36-public`.
- Confirmed package files: `bootloader.bin`, `boot_app0.bin`, `partitions.bin`, `zdeck-factory.bin`, `zdeck-firmware.bin`, `zdeck-littlefs.bin`, `zdeck-meshtastic-metadata.json`, `SHA256SUMS.json`, and `README.md`.
- Confirmed `SHA256SUMS.json` lists six binary artifacts and the app binary hash matches `update.json`.
- Confirmed package README states firmware `2.8.0.zdeck36`, pack `0.2.35-cyberdeck`, build `20260613-zdeck36-production-themes-t-deck-tft`, app slots at `0x10000` and `0x650000`, and app-only OTA preservation.
- Source archive checked: `source\patches\2026-06-13-zdeck36-public`.
- Confirmed archive includes `README.md`, `meshtastic-firmware-src.patch`, `zdeck-full-source.patch`, and the public-safe patch stack.
- Confirmed source archive README states no private channel data, PSKs, channel URLs, Wi-Fi credentials, admin keys, owner-specific settings, or saved chats are bundled.

GitHub checks:
- Commit checked before this log entry: `6e22603 Record UI overlap readiness check`.
- Workflows checked for that commit: `Release Drafter`, `Broken Link Checker`, `Push on main`, and `pages build and deployment`.
- Result: all listed workflows completed with `success`.
- GitHub tag/release check before this log entry found existing tags/releases only through older public versions; no `zdeck-0.2.35-cyberdeck` tag or release was present.
- Commit created from this log entry: `53a6902 Record public artifact readiness check`.
- Public tag created and pushed: `zdeck-0.2.35-cyberdeck`.
- GitHub API tag check confirmed `zdeck-0.2.35-cyberdeck` resolves to commit `53a69029fc5474d0452f4c67fe18d42c85c884a4`.
- GitHub release-object check for `zdeck-0.2.35-cyberdeck` returned HTTP `404`, so tag traceability exists but a formal release page was still not created.
- Workflows checked for commit `53a6902`: `Release Drafter`, `Broken Link Checker`, `Push on main`, and `pages build and deployment`.
- Result: all listed workflows completed with `success`.

On-device pages / controls represented:
- On-device pages represented by artifacts: first-install web flasher, Settings/Z-Deck OTA, SD backup/restore controls, Wi-Fi scan/select setup, diagnostics, map/GPS/compass pages, chat/status pages, and sidebar/settings surfaces.
- Controls/status labels represented: `Install`, `CHECK`, `APPLY`, `STATUS`, `BACKUP SD`, `RESTORE SD`, `SCAN`, `Z-Deck OTA`, and update progress/status text.

Hardware / serial checks:
- Windows serial ports visible: `COM17`, `COM21`, and `COM3`.
- `COM17` and `COM21` were visible as USB VID `303A` PID `1001` ESP32-S3/T-Deck app-side serial ports.
- `COM3` remained visible as USB VID `3402` PID `0900`.
- Narrow metadata read on `COM21` returned firmware `2.8.0.zdeck36`, role `CLIENT`, and hardware `T_DECK`.
- Narrow non-secret config read on `COM21` confirmed `device.role: 0`, `display.screen_on_secs: 120`, `lora.hop_limit: 3`, `lora.modem_preset: 0`, `power.is_power_saving: False`, `bluetooth.enabled: True`, and `bluetooth.mode: 0`.

Bluetooth checks:
- Windows service `bthserv` was running.
- Windows service `DeviceAssociationService` was running.
- Bluetooth adapter `USB\VID_0489&PID_E112\00E04C000001` was `OK`.
- Bluetooth adapter `USB\VID_0B05&PID_1D70\6&D596480&0&2` remained in `Error`.
- Microsoft Bluetooth LE Enumerator was `OK`.
- Python `bleak` scan completed successfully for 12 seconds.
- BLE scan result: `device_count=0`.
- Narrow non-secret Meshtastic read on `COM21` confirmed `bluetooth.enabled: True` and `bluetooth.mode: 0`.

Blockers / next check:
- GitHub release object for `zdeck-0.2.35-cyberdeck` was not created by this pass; tag traceability is added, but a formal release page/assets would still need a release-create step.
- Live page copy did not literally include the string `update.json`, though the live endpoint itself passed.
- Physical on-device OTA/apply from the public artifact was not pressed during this pass.
- Bluetooth pairing/discovery remains unproven until a physical pairing/reset check produces BLE advertisements.

### 2026-06-13 22:22 -04:00

Scope: public OTA manifest visibility on the flasher home page.

Concrete feature unit:
- Added a first-screen `OTA manifest` row to the release payload card on the public flasher page, linking directly to `update.json`.
- Feature commit: `1705d49 Expose public OTA manifest link`.
- Changed files: `index.html` and `style.css`.

Public pages / controls checked:
- Page checked locally: `http://127.0.0.1:4180/`.
- Confirmed local page returned HTTP `200`.
- Confirmed local page includes visible `update.json` text and `href="update.json"`.
- Confirmed local `http://127.0.0.1:4180/update.json` returned HTTP `200`, pack `0.2.35-cyberdeck`, firmware `2.8.0.zdeck36`, and update mode `app-only`.
- Page checked live after Pages deployment: `https://its-ze.github.io/Z-Deck-Web-Flasher/`.
- Confirmed live page returned HTTP `200`.
- Confirmed live page includes visible `update.json` text and `href="update.json"`.
- Endpoint checked live: `https://its-ze.github.io/Z-Deck-Web-Flasher/update.json`.
- Confirmed live manifest returned HTTP `200`, pack `0.2.35-cyberdeck`, firmware `2.8.0.zdeck36`, update mode `app-only`, and firmware size `3697280`.
- Command checked: `python tools\verify-ota-release.py --live`.
- Confirmed verifier evidence: hosted `update.json` matches local metadata, hosted app firmware size/SHA256/MD5 matches, SD pre-update backup is required, and app slots stay separate from LittleFS.

Public controls/status labels represented:
- First-screen release payload card labels checked: `Update mode`, `OTA manifest`, `Backup path`, and `Firmware SHA256`.
- Public link/control checked: `update.json`.
- On-device pages represented by the linked manifest: `Settings > Z-Deck OTA`, `CHECK`, `APPLY`, `STATUS`, `BACKUP SD`, and guarded `RESTORE SD`.

GitHub checks:
- Workflows checked for feature commit `1705d49`: `Release Drafter`, `Broken Link Checker`, `Push on main`, and `pages build and deployment`.
- Result: all listed workflows completed with `success`.
- Broken Link Checker success confirms the new `update.json` link is valid from the public HTML.

Hardware / serial checks:
- Windows serial ports visible: `COM17`, `COM21`, and `COM3`.
- `COM17` and `COM21` were visible as USB VID `303A` PID `1001` ESP32-S3/T-Deck app-side serial ports.
- `COM3` remained visible as USB VID `3402` PID `0900`.
- Narrow non-secret config read on `COM21` confirmed `device.role: 0`, `display.screen_on_secs: 120`, `bluetooth.enabled: True`, `bluetooth.mode: 0`, and `power.is_power_saving: False`.

Bluetooth checks:
- Windows service `bthserv` was running.
- Windows service `DeviceAssociationService` was running.
- Bluetooth adapter `USB\VID_0489&PID_E112\00E04C000001` was `OK`.
- Bluetooth adapter `USB\VID_0B05&PID_1D70\6&D596480&0&2` remained in `Error`.
- Microsoft Bluetooth LE Enumerator was `OK`.
- Python `bleak` scan completed successfully for 12 seconds.
- BLE scan result: `device_count=0`.
- Narrow non-secret Meshtastic read on `COM21` confirmed Bluetooth was enabled.

Blockers / next check:
- Physical on-device OTA/apply from `Settings > Z-Deck OTA` was not pressed during this pass.
- Bluetooth pairing/discovery remains unproven until a physical pairing/reset check produces BLE advertisements.
- Formal GitHub release object for `zdeck-0.2.35-cyberdeck` remains separate from this page/link improvement.

### 2026-06-13 23:19 -04:00

Scope: formal public GitHub release object for `zdeck-0.2.35-cyberdeck`.

Concrete feature unit:
- Created the missing formal GitHub prerelease for tag `zdeck-0.2.35-cyberdeck`.
- Release URL: `https://github.com/Its-ze/Z-Deck-Web-Flasher/releases/tag/zdeck-0.2.35-cyberdeck`.
- Release is public, non-draft, and marked prerelease.
- Release notes are public-safe and do not include private channel data, PSKs, channel URLs, Wi-Fi passwords, admin keys, owner-specific settings, or saved chats.

Public release assets checked:
- `bootloader.bin`: `15104` bytes.
- `partitions.bin`: `3072` bytes.
- `boot_app0.bin`: `8192` bytes.
- `zdeck-firmware.bin`: `3697280` bytes.
- `zdeck-factory.bin`: `3762816` bytes.
- `zdeck-littlefs.bin`: `3538944` bytes.
- `SHA256SUMS.json`: `1009` bytes.
- `zdeck-meshtastic-metadata.json`: `2208` bytes.
- `README.md`: `1410` bytes.
- Public GitHub API release check confirmed `assetCount: 9`.

Public pages / controls checked:
- Release page checked: `https://github.com/Its-ze/Z-Deck-Web-Flasher/releases/tag/zdeck-0.2.35-cyberdeck`.
- Confirmed release page returned HTTP `200`.
- Page checked live: `https://its-ze.github.io/Z-Deck-Web-Flasher/`.
- Confirmed live page returned HTTP `200` and still includes visible `update.json` text plus `href="update.json"`.
- Endpoint checked live: `https://its-ze.github.io/Z-Deck-Web-Flasher/update.json`.
- Confirmed live manifest returned HTTP `200`, pack `0.2.35-cyberdeck`, firmware `2.8.0.zdeck36`, update mode `app-only`, and firmware size `3697280`.
- Command checked: `python tools\verify-ota-release.py --live`.
- Confirmed verifier evidence: hosted `update.json` matches local metadata, hosted app firmware size/SHA256/MD5 matches, SD pre-update backup is required, and app slots stay separate from LittleFS.

On-device pages / controls represented:
- On-device page represented by the release and OTA manifest: `Settings > Z-Deck OTA`.
- Controls/status labels represented: `CHECK`, `APPLY`, `STATUS`, `BACKUP SD`, guarded `RESTORE SD`, app-only OTA mode, SD pre-update backup, and update progress/status text.

Hardware / serial checks:
- Windows serial ports visible: `COM17`, `COM21`, and `COM3`.
- `COM17` and `COM21` were visible as USB VID `303A` PID `1001` ESP32-S3/T-Deck app-side serial ports.
- `COM3` remained visible as USB VID `3402` PID `0900`.
- Narrow non-secret config read on `COM21` confirmed `device.role: 0`, `display.screen_on_secs: 120`, `bluetooth.enabled: True`, `bluetooth.mode: 0`, and `power.is_power_saving: False`.

Bluetooth checks:
- Windows service `bthserv` was running.
- Windows service `DeviceAssociationService` was running.
- Bluetooth adapter `USB\VID_0489&PID_E112\00E04C000001` was `OK`.
- Bluetooth adapter `USB\VID_0B05&PID_1D70\6&D596480&0&2` remained in `Error`.
- Microsoft Bluetooth LE Enumerator was `OK`.
- Python `bleak` scan completed successfully for 12 seconds.
- BLE scan result: `device_count=0`.
- Narrow non-secret Meshtastic read on `COM21` confirmed Bluetooth was enabled.

Blockers / next check:
- Physical on-device OTA/apply from `Settings > Z-Deck OTA` was not pressed during this pass.
- Bluetooth pairing/discovery remains unproven until a physical pairing/reset check produces BLE advertisements.
- The release object now exists; future release checks should verify both Pages `update.json` and the GitHub release page/assets.

### 2026-06-14 15:34 -04:00

Scope: zdeck37 OTA-test release and duplicate found-device cleanup.

Concrete feature unit:
- Added duplicate-node filtering in the T-Deck firmware source before the on-device node list, message destination picker, and favorite-node pages render NodeDB records.
- Rebuilt public firmware as `2.8.0.zdeck37` / `0.2.36-cyberdeck` from `20260614-zdeck37-ota-test-t-deck-tft`.
- Published local package folder `firmware\zdeck-2.8.0-zdeck37-public`.
- Published source archive folder `source\patches\2026-06-14-zdeck37-public`.

Public pages / controls checked locally:
- Page file checked: `index.html`.
- Status text checked: `Flash Z-Deck 0.2.36`, `2.8.0.zdeck37`, `0.2.36-cyberdeck`, `Firmware SHA256`, `update.json`, and `Z-Deck OTA`.
- Script file checked: `app.js`.
- Ticker labels checked: `firmware: Z-Deck 0.2.36-cyberdeck / LongFast` and `duplicate-device cleanup + OTA test`.
- Wiki page checked: `wiki\index.html`.
- Documentation checked: `README.md`, `CHANGELOG.md`, `KNOWN_ISSUES.md`, `PRIVACY.md`, `SECURITY.md`, and `CONTRIBUTING.md`.

On-device pages / controls represented:
- On-device pages represented by the release and OTA manifest: `Found devices` / node list, message destination picker, favorite-node pages, and `Settings > Z-Deck OTA`.
- Controls/status labels represented: `CHECK`, `APPLY`, `STATUS`, `BACKUP SD`, guarded `RESTORE SD`, app-only OTA mode, SD pre-update backup, and update progress/status text.

Build / package evidence:
- WSL PlatformIO build completed successfully.
- Metadata reports firmware `2.8.0.zdeck37`, pack `0.2.36-cyberdeck`, hardware `T_DECK`, environment `t-deck-tft`.
- App payload: `firmware\zdeck-2.8.0-zdeck37-public\zdeck-firmware.bin`.
- App size: `3697536`.
- App SHA256: `84a37baac2ca75796a3d65d4f1f4ed2026d95bd67cced0d23a6a98855c07d3b8`.
- App MD5: `de633ec3339af516e9c4aec9fdfdb348`.
- New package checksum entries verified for `boot_app0.bin`, `bootloader.bin`, `partitions.bin`, `zdeck-factory.bin`, `zdeck-firmware.bin`, and `zdeck-littlefs.bin`.

Validation commands:
- `python tools\verify-ota-release.py` passed.
- Patch manifest check passed with all `23` root patch files accounted for.
- `git diff --check` passed after cleaning generated patch whitespace.

Blockers / next check:
- Live GitHub Pages verification must run after this release is pushed.
- Physical on-device OTA apply still requires the user to connect Wi-Fi, open `Settings > Z-Deck OTA`, press `CHECK`, then press `APPLY`.

### 2026-06-22 00:06 -04:00

Scope: BACKUP SD crash investigation and zdeck45 public hotfix.

Concrete feature unit:
- Fixed the on-device `BACKUP SD` / guarded `RESTORE SD` crash path by queuing SD maintenance through `ZDeckMaint` instead of running SD setup/write/restore directly inside LVGL/classic UI button handlers.
- Added USB diagnostic command `itsz zdeck backup-queue` plus helper command `backup-queue` so the same deferred path can be triggered while serial debug is running.
- Fixed backup completion state mapping so a completed SD backup reports `OTA READY` instead of remaining `OTA BUSY`.
- Rebuilt and flashed app-only firmware `2.8.0.zdeck45` / `0.2.44-cyberdeck`; LittleFS was skipped to preserve device settings/channels/keys/owner data.

Hardware / serial checks:
- Windows serial ports observed: `COM17` normal app mode, `COM16` ESP32-S3 bootloader mode, and `COM3` unrelated serial.
- Flash target verified as ESP32-S3 over `COM16`; both app slots were written and verified by esptool.
- Device returned to normal mode on `COM17`.

On-device pages / controls represented:
- `Settings > Z-Deck OTA` controls represented by the release and source patch stack: `CHECK`, `APPLY`, `STATUS`, `BACKUP SD`, and guarded `RESTORE SD`.
- USB commands checked: `status`, `backup`, and `backup-queue`.
- Status labels checked: `OTA IDLE`, `SD READY`, `OTA BUSY SD backup queued`, `OTA READY Settings backup saved to SD`, and debug breadcrumb `ui-backup/deferred.ok`.

Build / package evidence:
- WSL PlatformIO build completed successfully from `20260622-zdeck45-sd-backup-ready-state-t-deck-tft`.
- App payload: `firmware\zdeck-2.8.0-zdeck45-public\zdeck-firmware.bin`.
- App size: `3711712`.
- App SHA256: `820bc045cce984ce2484161b5741ac1640c1d57c249d2d1c1a51ec36dc7519c2`.
- App MD5: `37d16c58f777e5cc31def1601872a876`.
- Direct USB backup passed with `sd-backup/api.ok`, SD size detected, backup file saved, and restore/decode verification OK.
- Deferred USB backup passed with `ui-backup/deferred.begin`, `sd-backup/api.ok`, and `ui-backup/deferred.ok`.
- Final post-backup status passed: `OTA READY Settings backup saved to SD` and `SD READY Settings backup saved to SD`.
- Live GitHub Pages OTA verification passed after Pages caught up to commit `0ac0e90`: live `update.json` SHA256 matched local, live firmware size matched, live firmware SHA256 matched, and live firmware MD5 matched.
- Device Wi-Fi status over USB passed without printing credentials: Wi-Fi enabled/configured/connected, IP present, RSSI reported.
- Device OTA check over USB passed against live public manifest: HTTP `200`, manifest parsed, payload size `3711712`, `newer=0`, and status `Z-Deck is current 0.2.44-cyberdeck`.

Validation commands:
- `python tools\verify-ota-release.py` passed.
- `git diff --check` passed apart from normal line-ending warnings.
- JSON parse checks passed for `manifest.json`, `update.json`, and `source\patches\patch-manifest.json`.
- Text-only public secret scan passed for zdeck45 package/source JSON, Markdown, patch, and text files.
- `SHA256SUMS.json` package hash verification passed.
- `python tools\verify-ota-release.py --live` passed after GitHub Pages propagation.
- `.\tools\zdeck-usb-debug.ps1 -Port COM17 -Command wifi-status -MonitorSeconds 12` passed.
- `.\tools\zdeck-usb-debug.ps1 -Port COM17 -Command ota-check -MonitorSeconds 35` passed.

Blockers / next check:
- Physical touchscreen press of `BACKUP SD` should be checked by the user, but the USB `backup-queue` command exercised the same deferred service path that the button now calls.

### 2026-06-22 09:56 -04:00

Scope: zdeck46 public release for right-sidebar battery indicator overlap.

Concrete feature unit:
- Fixed the T-Deck right-sidebar battery overlap by constraining `battery_panel` to a 64px safe zone inside the 280px content area when the sidebar is on the right.
- Tightened battery icon and percentage offsets so the percent text stays visible beside the icon instead of sitting under the right rail.
- Rebuilt public firmware as `2.8.0.zdeck46` / `0.2.45-cyberdeck` from `20260622-zdeck46-battery-sidebar-clearance-t-deck-tft`.

On-device pages / controls represented:
- Home/top status bar battery panel.
- Right sidebar layout preference.
- `Settings > Z-Deck OTA` app-only update path with SD pre-update backup preserved.

Build / package evidence:
- WSL PlatformIO build completed successfully.
- App payload: `firmware\zdeck-2.8.0-zdeck46-public\zdeck-firmware.bin`.
- App size: `3711792`.
- App SHA256: `983c3f6d1b85b62be44d53b26ccedfc9466342d6ddc9cb4c457f0925a234a9a7`.
- App MD5: `aa35756c80fa6f874805c2b5d810b65a`.
- `SHA256SUMS.json` package hash verification passed for 7 files.
- Text-only high-risk public secret scan passed without printing any sensitive values.

Validation commands:
- `python tools\verify-ota-release.py` passed.
- JSON parse checks passed for `manifest.json`, `update.json`, `source\patches\patch-manifest.json`, and `firmware\zdeck-2.8.0-zdeck46-public\SHA256SUMS.json`.
- `git diff --check` passed apart from normal line-ending warnings.

Blockers / next check:
- Live GitHub Pages verification and physical device OTA apply still need to run after this release is pushed.

### 2026-06-22 10:08 -04:00

Scope: zdeck47 OTA apply hotfix after zdeck46 OTA test exposed an old preflight reset.

Concrete feature unit:
- Confirmed zdeck46 public package and live Pages hashes were valid.
- Device on `COM17` saw zdeck46 as available: manifest HTTP `200`, payload size `3711792`, and `newer=1`.
- OTA apply from the old installed app reset twice immediately after `ota/preflight.backup.begin`, before `sd-backup/api.begin`.
- Confirmed direct `backup` and deferred `backup-queue` both save and verify `/zdeck/backups/preferences.proto`, so the reset is specific to the old OTA apply preflight path.
- Built zdeck47 to split OTA preflight SD backup from the HTTP/download install frame while keeping the right-sidebar battery safe-zone fix.

Hardware / serial checks:
- Windows serial port observed: `COM17` normal app mode.
- Wi-Fi status over USB: enabled/configured/connected, IP present, RSSI reported.
- OTA apply failure was observed through USB debug without printing credentials or private channel material.

Build / package evidence:
- WSL PlatformIO build completed successfully from `20260622-zdeck47-ota-preflight-stack-t-deck-tft`.
- App payload: `firmware\zdeck-2.8.0-zdeck47-public\zdeck-firmware.bin`.
- App size: `3711824`.
- App SHA256: `e4cf16a1ed90d89e847ae91461cccb454fff457005ea186968dcea69b0457fc2`.
- App MD5: `75a833d938888a5af03ccfa005ea8c86`.

Validation commands:
- `python tools\verify-ota-release.py` pending for zdeck47.
- Live GitHub Pages verification pending after push.

Blockers / next check:
- The currently installed zdeck45 app cannot OTA apply past its own preflight reset. Use an app-only USB flash once to bootstrap onto zdeck47, then verify future OTA apply from zdeck47.

### 2026-06-22 10:24 -04:00

Scope: zdeck48 public validation release for OTA apply testing from zdeck47.

Concrete feature unit:
- Packaged zdeck48 as a distinct app-only OTA target so a device already bootstrapped to zdeck47 can exercise the full Wi-Fi OTA apply path.
- Preserved the zdeck46 right-sidebar battery safe-zone fix and the zdeck47 OTA preflight stack split.
- Kept the web flasher LittleFS image as an install-time artifact only; `update.json` remains app-only and preserves config, channels, keys, owner settings, sidebar/layout preferences, map defaults, and SD data.

Build / package evidence:
- WSL PlatformIO build completed successfully from `20260622-zdeck48-ota-apply-validation-t-deck-tft`.
- App payload: `firmware\zdeck-2.8.0-zdeck48-public\zdeck-firmware.bin`.
- App size: `3711824`.
- App SHA256: `74e60b4942afcee0cd8dae0b037e9fae17502db17a551fb738ebd6bf68ed5b85`.
- App MD5: `facb0ec221190f1734beb019f1bafefa`.
- Source archive: `source\patches\2026-06-22-zdeck48-public`.

Validation commands:
- `python tools\verify-ota-release.py` passed.
- `git diff --check` passed apart from normal line-ending warnings.
- `SHA256SUMS.json` package hash verification passed for 7 files.
- Release-scoped literal secret scan passed for manifest/update/package/source-archive text files without printing secret-like values.

Blockers / next check:
- Commit and push zdeck48, wait for GitHub Pages propagation, then run OTA check/apply on the T-Deck over USB debug while preserving LittleFS/private settings.

### 2026-06-22 10:31 -04:00

Scope: zdeck48 live OTA availability and attempted on-device OTA watch.

Concrete feature unit:
- Confirmed GitHub Pages caught up to the zdeck48 public release.
- Live `update.json` and live `zdeck-firmware.bin` matched local metadata, size, SHA256, and MD5.
- Attempted to start the device OTA watch over USB after Pages validation.

Hardware / serial checks:
- Expected normal T-Deck app port `COM17` was not present.
- Windows reported only active serial port `COM3` with USB VID:PID `3402:0900`.
- Meshtastic metadata probe on `COM3` timed out, so `COM3` was not treated as the T-Deck.
- Non-writing ESP probe on `COM3` failed with no serial data received.
- Last known T-Deck Wi-Fi IP `192.168.50.204` did not answer ping.

Validation commands:
- `python tools\verify-ota-release.py --live` passed after one propagation wait.
- `python -m serial.tools.list_ports` showed only `COM3`.
- `python -m meshtastic --port COM3 --no-nodes --timeout 20 --device-metadata` timed out.
- `python -m esptool --port COM3 --baud 115200 chip_id` did not connect and did not write anything.

Blockers / next check:
- The T-Deck is not currently reachable over USB or Wi-Fi from this computer, so the zdeck47-to-zdeck48 OTA apply could not be triggered or watched. Reconnect the T-Deck in normal app mode, confirm its port appears, then run `ota-check` and `ota-apply` over USB debug.

### 2026-06-22 19:38 -04:00

Scope: resumed zdeck47-to-zdeck48 OTA apply attempt after the T-Deck was reconnected.

Concrete feature unit:
- Confirmed the expected T-Deck reappeared as `COM17` with USB VID:PID `303A:1001` and serial `E072A1CD2AC8`.
- Read-only Meshtastic metadata confirmed app mode on firmware `2.8.0.zdeck47`, hardware `T_DECK`, role `CLIENT`, and PKC present.
- USB debug Wi-Fi status confirmed Wi-Fi enabled/configured/connected at `192.168.50.204` with RSSI reported.
- OTA apply was not started because the device disappeared before `ota-check` could open `COM17`.

Hardware / serial checks:
- `COM16` bootloader mode appeared briefly at `19:22:26` and removed at `19:22:27`.
- `COM17` app mode appeared at `19:22:27` and removed at `19:23:35`.
- After removal, Windows again showed the T-Deck ports as `CM_PROB_PHANTOM`; only `COM3` remained present, and `COM3` is not a T-Deck.
- A fast OTA watcher monitored for `COM17` for 10 minutes and it did not return.

Validation commands:
- `python -m meshtastic --port COM17 --no-nodes --timeout 25 --device-metadata` passed before the disconnect.
- `.\tools\zdeck-usb-debug.ps1 -Port COM17 -Command wifi-status -MonitorSeconds 15` passed before the disconnect.
- `.\tools\zdeck-usb-debug.ps1 -Port COM17 -Command ota-check -MonitorSeconds 45` could not open the port because `COM17` had already been removed.

Blockers / next check:
- The device is reachable briefly, then drops from both USB and Wi-Fi before OTA can be checked or applied. Next attempt should skip nonessential probes and start with `ota-check` immediately when `COM17` returns, or use a stable power/cable/port path before retrying.

### 2026-06-22 20:26 -04:00

Scope: confirmed zdeck47-to-zdeck48 OTA apply and isolated the USB debug DTR/session issue.

Concrete feature unit:
- Ran OTA check and OTA apply in one continuous serial session with DTR held, avoiding the previous close/reopen cycle between `ota-check` and `ota-apply`.
- Device on `COM17` reported zdeck48 available from live `update.json`: HTTP `200`, payload size `3711824`, and `newer=1`.
- OTA apply completed the SD preflight backup, HTTP firmware download, and app write from `0%` through `100%`.
- Update finished with `ota/update.end.ok`, then the device rebooted as expected.
- Post-reboot Meshtastic metadata verified firmware `2.8.0.zdeck48`, hardware `T_DECK`, role `CLIENT`, and PKC present.
- Post-reboot OTA check verified live manifest current state: HTTP `200`, payload size `3711824`, `newer=0`, and status `Z-Deck is current 0.2.47-cyberdeck`.

Hardware / serial checks:
- T-Deck target: `COM17`, USB VID:PID `303A:1001`, serial `E072A1CD2AC8`.
- Wi-Fi before OTA: connected at `192.168.50.204`; RSSI was weak but usable.
- The earlier failure pattern was reproduced as a host-side tooling issue: `--no-dtr` keeps the port stable but silent, while separate DTR-open/close sessions can cause the T-Deck port to drop before the next command.
- After the successful OTA and current-state check, `COM17` later dropped again and the device IP became unreachable, so the remaining issue is serial/power/session stability after host serial close, not OTA payload failure.

Validation commands:
- Combined DTR-held Python serial session sent `itsz zdeck ota check` and `itsz zdeck ota apply` without closing the port between them.
- `python -m meshtastic --port COM17 --no-nodes --timeout 30 --device-metadata` passed after the reboot and reported `2.8.0.zdeck48`.
- A second combined serial session sent `itsz zdeck ota check` and confirmed `newer=0`.
- `python -m py_compile tools\zdeck-usb-debug.py` passed after adding the local helper-side `ota-update` command.

Changed local helper files:
- `F:\Dropbox\Dev Ops\T-Deck\tools\zdeck-usb-debug.py` now supports `ota-update`, which checks and applies in the same serial session.
- `F:\Dropbox\Dev Ops\T-Deck\tools\zdeck-usb-debug.ps1` exposes `ota-update` and `-HoldDtrOnClose`.

Blockers / next check:
- Firmware OTA is confirmed working on zdeck48. The remaining defect to investigate is the T-Deck disappearing from USB/Wi-Fi after host serial close; future USB debug should use `ota-update` or one held-open serial session and avoid separate check/apply helper calls.
