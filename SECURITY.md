# Security Policy

## Supported Versions

Z-Deck Web Flasher follows a rolling release model. Only the latest public release is actively maintained.

| Version | Supported |
| ------- | --------- |
| Latest (`0.2.25-cyberdeck`) | :white_check_mark: |
| Older releases | :x: |

If you are on an older build, please update to the latest release before reporting a security issue.

## Scope

This repository covers:
- The browser-based Web Serial flasher (`index.html`, `app.js`, `style.css`)
- The bundled non-secret firmware artifacts and `manifest.json`
- The Z-Deck source patch set under `source/patches/`

This repository does **not** contain and you should **never** submit:
- Private Meshtastic channels, PSKs, or channel URLs
- Admin keys, private keys, SD settings backups, or personal setup data
- Any credentials or secrets of any kind

## Reporting a Vulnerability

If you discover a security vulnerability in the Z-Deck Web Flasher (e.g. a flaw in the flashing page that could allow malicious firmware injection, a cross-site scripting issue in the hosted page, or a supply-chain concern with a bundled artifact), please report it **privately** rather than opening a public issue.

How to report:

1. Open a [GitHub Security Advisory](https://github.com/Its-ze/Z-Deck-Web-Flasher/security/advisories/new) for this repository (private disclosure).
2. Describe the vulnerability, the affected component, and steps to reproduce.
3. Include your assessment of the impact and any suggested fix if you have one.
4. You can expect an acknowledgement within a few days and a status update as the issue is investigated. If the vulnerability is confirmed, a fix will be issued in a new release. If it is declined, you will receive an explanation.
5. Please do not disclose vulnerabilities publicly until a fix has been released or you have received confirmation that the issue is not considered a security risk.

## Upstream Security Issues

This firmware is derived from [Meshtastic firmware](https://github.com/meshtastic/firmware) (GPL v3). If the vulnerability is in the upstream Meshtastic codebase rather than the Z-Deck patches or flasher, please also report it to the [Meshtastic project](https://github.com/meshtastic/firmware/security).
