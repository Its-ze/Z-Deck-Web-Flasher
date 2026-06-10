const idleLines = [
  "status: waiting for T-Deck",
  "firmware: Z-Deck 0.2.23-cyberdeck / LongFast",
  "target: ESP32-S3 / t-deck-tft",
  "bundle: sidebar-right + Wi-Fi scan + SD backup",
  "ready: connect deck and authorize serial"
];

const ticker = document.getElementById("ticker");
const installButton = document.getElementById("installButton");
const customManifest = document.getElementById("customManifest");
const applyManifest = document.getElementById("applyManifest");
const manifestStatus = document.getElementById("manifestStatus");
const commitList = document.getElementById("commitList");
const recoveryButtons = Array.from(document.querySelectorAll("[data-recovery]"));
const recoveryModeLabel = document.getElementById("recoveryModeLabel");
const recoverySteps = document.getElementById("recoverySteps");
const recoveryHint = document.getElementById("recoveryHint");

const recoveryModes = {
  normal: {
    label: "Normal boot",
    steps: [
      "Release the center trackball / BOOT control completely.",
      "Tap RESET once, or unplug and reconnect USB normally.",
      "Wait for the Z-Deck screen instead of selecting the port again.",
      "Use the Meshtastic app or CLI only after the app-side port appears."
    ],
    hint: "Do not reflash just because the ROM loader still answers; a verified flash usually means the bytes are already on the board.",
    ticker: [
      "recovery: normal boot",
      "release: BOOT / trackball / GPIO0",
      "action: tap RESET or unplug/replug",
      "expect: Z-Deck screen and app-side serial"
    ]
  },
  bootloader: {
    label: "Enter bootloader",
    steps: [
      "Plug the T-Deck in over USB.",
      "Hold the center trackball / BOOT control.",
      "Tap RESET, then release RESET.",
      "Release BOOT only after the serial port appears in the browser prompt."
    ],
    hint: "Use bootloader mode for flashing or rollback. Leave it only after the flash finishes and verifies.",
    ticker: [
      "recovery: bootloader entry",
      "hold: BOOT / trackball",
      "tap: RESET",
      "release: BOOT after port appears"
    ]
  },
  verify: {
    label: "Verify app mode",
    steps: [
      "The screen should show Z-Deck or Meshtastic UI after reset.",
      "The board should stop reconnecting immediately to the ROM loader.",
      "Meshtastic serial commands should connect instead of timing out.",
      "Then configure owner, channels, private keys, and Wi-Fi."
    ],
    hint: "If Meshtastic API still times out and esptool still connects with no reset, the board is still in programming mode.",
    ticker: [
      "recovery: app-mode check",
      "screen: Z-Deck UI visible",
      "serial: Meshtastic API responds",
      "next: configure mesh settings"
    ]
  }
};

function setTicker(lines) {
  if (!ticker) return;
  ticker.textContent = lines.map((line) => "> " + line).join("\n");
}

function renderRecoveryMode(modeName) {
  const mode = recoveryModes[modeName] || recoveryModes.normal;
  recoveryButtons.forEach((button) => {
    const isActive = button.dataset.recovery === modeName;
    button.classList.toggle("active", isActive);
    button.setAttribute("aria-pressed", isActive ? "true" : "false");
  });
  if (recoveryModeLabel) recoveryModeLabel.textContent = mode.label;
  if (recoverySteps) {
    recoverySteps.replaceChildren(...mode.steps.map((step) => {
      const item = document.createElement("li");
      item.textContent = step;
      return item;
    }));
  }
  if (recoveryHint) recoveryHint.textContent = mode.hint;
  setTicker(mode.ticker);
}

setTicker(idleLines);

installButton.addEventListener("click", () => {
  setTicker([
    "status: serial action requested",
    "next: choose the T-Deck port in the browser prompt",
    "firmware: Z-Deck 0.2.23-cyberdeck / LongFast",
    "flash map: app0 + app1 + littlefs",
    "features: sidebar setting + safer OTA"
  ]);
});

applyManifest.addEventListener("click", () => {
  const value = customManifest.value.trim();
  if (!value) {
    installButton.setAttribute("manifest", "manifest.json");
    manifestStatus.textContent = "Default manifest: bundled Z-Deck firmware.";
    setTicker(idleLines);
    return;
  }

  try {
    const parsed = new URL(value);
    if (parsed.protocol !== "https:" && parsed.hostname !== "localhost" && parsed.hostname !== "127.0.0.1") {
      throw new Error("Manifest must be HTTPS or localhost.");
    }
    installButton.setAttribute("manifest", parsed.href);
    manifestStatus.textContent = "Custom manifest armed: " + parsed.href;
    setTicker([
      "status: custom manifest armed",
      "manifest: " + parsed.href,
      "next: connect deck and authorize serial",
      "note: only flash manifests you trust"
    ]);
  } catch (error) {
    manifestStatus.textContent = error.message || "That manifest URL is not valid.";
    setTicker([
      "status: manifest rejected",
      "error: " + (error.message || "invalid manifest URL"),
      "allowed: HTTPS, localhost, or 127.0.0.1"
    ]);
  }
});

recoveryButtons.forEach((button) => {
  button.addEventListener("click", () => renderRecoveryMode(button.dataset.recovery));
});

async function loadCommits() {
  if (!commitList) return;

  try {
    const response = await fetch("https://api.github.com/repos/Its-ze/Z-Deck-Web-Flasher/commits?per_page=5", {
      headers: { Accept: "application/vnd.github+json" }
    });

    if (!response.ok) throw new Error("GitHub history unavailable.");

    const commits = await response.json();
    commitList.replaceChildren(...commits.map((commit) => {
      const item = document.createElement("li");
      const link = document.createElement("a");
      const date = new Date(commit.commit.author.date);
      link.href = commit.html_url;
      link.target = "_blank";
      link.rel = "noreferrer";
      link.textContent = commit.commit.message.split("\n")[0];
      item.append(link, " ", date.toLocaleDateString());
      return item;
    }));
  } catch (error) {
    const item = document.createElement("li");
    item.textContent = "GitHub change history did not load. Open the GitHub button for commits and releases.";
    commitList.replaceChildren(item);
  }
}

loadCommits();
