# Z-Deck Device Setup Handoff - 2026-06-09

This note captures the live setup state before the USB devices were disconnected.
It is intentionally public-safe and does not include private channel keys, admin
keys, Wi-Fi passwords, or channel URLs.

## Goal

- Flash both LilyGo T-Decks with the ITSZ/Z-Deck firmware.
- Add a T-Deck system setting that keeps the left navigation/sidebar on the right side of the screen.
- Configure all Meshtastic devices with the user's normal settings, admin control, LongFast, and the ITSZ private channel from private local material only.
- Set the T-Dongle up as the computer-side web/control bridge for the T-Decks.
- Use the extra ESP32 as a useful support/control device after its role is confirmed.
- Publish only public-safe firmware/site/source changes to GitHub.

## Current USB Snapshot

Last Windows serial scan showed:

| Port | Observed device | Current interpretation |
| --- | --- | --- |
| COM16 | USB VID 303A/PID 1001, ESP32-S3, 16MB flash, PSRAM | Reachable T-Deck-class target. |
| COM22 | USB VID 303A/PID 1001 | Known T-Dongle / CyberDeck controller target. |
| COM14 | CP210x, ESP32-S3, 8MB flash | Reachable Heltec-class target. |
| COM9 | CP210x, Windows status error | Likely second Heltec or another CP210x Meshtastic device, blocked until replug/elevated restart. |
| COM23 | CH340, classic ESP32, 4MB flash | Generic ESP32 support device candidate. |
| COM3 | USB VID 3402/PID 0900 | Known non-target/false-positive hub-style serial device from prior local context. |

Notes:

- Only one T-Deck-class board and one Heltec-class board were reachable at the time of this note.
- The second T-Deck was not visible as a separate usable serial port in the current scan.
- COM9 could not be restarted from the non-elevated shell and should be unplugged/replugged before the next setup pass.
- It is safe to disconnect the devices now; no flashing session was left running.

## Work Completed Before Disconnect

- Added a T-Deck system/UI control named `Sidebar: right` / `Sidebar: left`.
- Default sidebar placement is right-side.
- The setting persists in the device UI filesystem at `/zdeck_sidebar.cfg`, so normal firmware updates should keep it.
- The sidebar patch was made durable as `itsz/device-ui-sidebar-layout.patch`.
- PlatformIO patch application now includes the sidebar patch.
- T-Deck build identity was bumped to:
  - firmware suffix: `zdeck24`
  - pack version: `0.2.23-cyberdeck`
  - build folder label: `20260609-zdeck24-sidebar-right-cyberdeck-t-deck-tft`
- The WSL T-Deck firmware build completed successfully.
- Latest local build artifact folder:
  - `F:\Dropbox\Dev Ops\T-Deck\firmware\builds\20260609-064241-t-deck-tft`

## Not Completed Yet

- The new zdeck24 firmware was built but not flashed to the connected T-Decks before this handoff.
- Private channel/admin settings were not pushed to any public repo and were not applied to the devices during this interrupted pass.
- The public web flasher release package for zdeck24 still needs to be assembled and published.
- T-Dongle pairing/web-control setup still needs to be verified on COM22 after reconnect.
- Heltec setup still needs to be flashed/configured after COM14/COM9 are confirmed.
- The extra ESP32 role still needs to be chosen and flashed/configured.

## Resume Checklist

1. Reconnect the devices and run a fresh serial-port inventory.
2. Recover COM9 by unplug/replug or elevated device restart if it still reports a Windows error.
3. Identify the second T-Deck serial port before flashing.
4. Flash the zdeck24 T-Deck build to each T-Deck.
5. Apply private Meshtastic settings from private local material only; do not publish those values.
6. Configure Heltecs with the same private/admin/channel profile.
7. Verify the T-Dongle web/control bridge and pair/control both T-Decks through it.
8. Package zdeck24 into the public flasher repo without secrets.
9. Push only public-safe docs, firmware binaries, manifests, source patches, and site updates.

## Safety Rule

Private channel material, admin keys, Wi-Fi credentials, and device-specific secrets must stay out of this public repo. Use the private local configuration sources when applying settings to hardware.
