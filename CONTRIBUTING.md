# Contributing to Z-Deck Web Flasher

Thanks for your interest in contributing to the Z-Deck Web Flasher! This project is a public browser flasher for the Z-Deck Firmware Pack, built on top of the Meshtastic T-Deck platform.

## Before You Start

- This repo intentionally contains only the browser flashing site, non-secret firmware artifacts, and source patches.
- **Never include** private Meshtastic channels, PSKs, channel URLs, admin keys, or private setup data in any contribution.
- Read the [Code of Conduct](CODE_OF_CONDUCT.md) before participating.

## Ways to Contribute

### Bug Reports

Use the [bug report issue template](https://github.com/Its-ze/Z-Deck-Web-Flasher/issues/new/choose) to report flashing, boot, display, GPS, map, SD journal, or Meshtastic issues.

When reporting a bug, please include:
- Your device (T-Deck, T-Deck Plus, or other hardware)
- The Z-Deck firmware version (e.g. `0.2.23-cyberdeck`)
- What happened vs. what you expected
- Steps to reproduce
- Non-sensitive logs or screenshots if available

Do **not** paste private keys, PSKs, channel URLs, admin keys, or private messages in any issue.

### Flasher / Web UI Improvements

The flasher is a static GitHub Pages site (`index.html`, `app.js`, `style.css`). Contributions that improve the flashing UX, error messaging, or browser compatibility are welcome.

- Keep the flasher compatible with Chrome and Edge (Web Serial API).
- Do not add dependencies that require a build step unless discussed first.
- Test against both standard `manifest.json` and a custom HTTPS manifest URL.

### Documentation

Improvements to `README.md`, `COMPATIBILITY.md`, `RECOVERY.md`, `KNOWN_ISSUES.md`, `PRIVACY.md`, or the hosted wiki are welcome.

### Firmware Source Patches

The `source/patches/` directory contains the Z-Deck patch set layered on top of upstream Meshtastic firmware (branch `2.8`, target `t-deck-tft`).

- Patches must apply cleanly against the upstream Meshtastic `2.8` branch.
- Contributions must be GPL v3 compatible (see [LICENSE](LICENSE)).
- Do not include proprietary code, private channel config, or build secrets.
- Reference the upstream project: https://github.com/meshtastic/firmware

## Submitting a Pull Request

1. Fork the repository and create a descriptive branch (e.g. `fix/flasher-reconnect` or `docs/recovery-update`).
2. Make your changes, keeping commits focused and messages clear.
3. Open a pull request against `main` describing what changed and why.
4. Be responsive to review feedback.

## What This Repo Does Not Accept

- Private network configs, PSKs, admin keys, or channel URLs.
- Closed-source firmware blobs or patches without attribution.
- Breaking changes to the Web Serial flashing flow without prior discussion.
- Contributions that make the public build depend on private infrastructure.

## License

By contributing, you agree your contributions are licensed under the [GNU General Public License v3.0](LICENSE), consistent with the rest of this project.
