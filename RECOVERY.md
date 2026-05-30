# Recovery And Rollback

## Bootloader Mode

1. Plug in the T-Deck over USB.
2. Hold the center trackball / BOOT control.
3. Tap RESET, then release RESET.
4. Release BOOT after the serial port appears.
5. Flash again from the web flasher or from a trusted local tool.

## Roll Back To Stock Meshtastic

1. Download a stock Meshtastic T-Deck release from the official Meshtastic project.
2. Put the T-Deck into ESP32-S3 bootloader mode.
3. Flash the stock T-Deck image using the Meshtastic web flasher or `esptool`.
4. Reconfigure owner, region, channels, GPS, Bluetooth, and other device settings.

## If Serial Appears Wedged

- Unplug and replug the T-Deck.
- Try another USB cable and a direct USB port.
- Re-enter bootloader mode manually.
- Avoid flashing if the selected serial device is not the T-Deck.

## What This Flasher Writes

| Offset | File |
| ---: | --- |
| `0x0000` | `bootloader.bin` |
| `0x8000` | `partitions.bin` |
| `0xe000` | `boot_app0.bin` |
| `0x10000` | `zdeck-firmware.bin` |
| `0x650000` | `zdeck-firmware.bin` |
| `0xc90000` | `zdeck-littlefs.bin` |
