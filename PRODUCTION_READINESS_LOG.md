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
