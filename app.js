const ticker = document.getElementById("ticker");
const installButton = document.getElementById("installButton");
const dualInstallButton = document.getElementById("dualInstallButton");
const otaTestInstallButton = document.getElementById("otaTestInstallButton");
const customManifest = document.getElementById("customManifest");
const applyManifest = document.getElementById("applyManifest");
const manifestStatus = document.getElementById("manifestStatus");
const commitList = document.getElementById("commitList");
const releaseNotes = document.getElementById("releaseNotes");
const recoveryButtons = Array.from(document.querySelectorAll("[data-recovery]"));
const recoveryModeLabel = document.getElementById("recoveryModeLabel");
const recoverySteps = document.getElementById("recoverySteps");
const recoveryHint = document.getElementById("recoveryHint");
const openDonglePairing = document.getElementById("openDonglePairing");
const donglePairingStatus = document.getElementById("donglePairingStatus");
const installModeButtons = Array.from(document.querySelectorAll("[data-install-mode]"));
const installModePanels = Array.from(document.querySelectorAll("[data-mode-panel]"));

let release = {
  title: "Z-Deck public release",
  packVersion: "loading",
  firmwareVersion: "loading"
};

const recoveryModes = {
  normal: {
    label: "Normal boot",
    steps: [
      "Release the center trackball / BOOT control completely.",
      "Tap RESET once, or unplug and reconnect USB normally.",
      "Wait for the Z-Deck screen instead of selecting the port again.",
      "Connect with Meshtastic only after the app-side serial port appears."
    ],
    hint: "A verified flash is already written. Do not reflash solely because the ROM loader still answers.",
    ticker: ["recovery: normal boot", "release: BOOT / trackball", "action: tap RESET", "expect: Z-Deck app serial"]
  },
  bootloader: {
    label: "Enter bootloader",
    steps: [
      "Plug the T-Deck in over USB.",
      "Hold the center trackball / BOOT control.",
      "Tap RESET, then release RESET.",
      "Release BOOT after the serial port appears in the browser prompt."
    ],
    hint: "Use this state only for USB flashing or recovery, then return to normal boot.",
    ticker: ["recovery: bootloader", "hold: BOOT / trackball", "tap: RESET", "release: BOOT after port appears"]
  },
  verify: {
    label: "Verify app mode",
    steps: [
      "Confirm the screen shows Z-Deck or MeshCore after reset.",
      "Confirm the board stops reconnecting to the ROM loader.",
      "Check that the expected app-side serial or Bluetooth interface responds.",
      "Configure owner, region, channels, private keys, and Wi-Fi locally."
    ],
    hint: "If Meshtastic times out while esptool still connects without reset, the board may still be in programming mode.",
    ticker: ["recovery: app verification", "screen: system UI visible", "serial: application responds", "next: local configuration"]
  }
};

function setTicker(lines) {
  if (!ticker) return;
  ticker.textContent = lines.map((line) => `> ${line}`).join("\n");
}

function releaseIdleLines() {
  return [
    "status: waiting for T-Deck",
    `release: ${release.packVersion}`,
    `firmware: ${release.firmwareVersion}`,
    "target: ESP32-S3 / t-deck-tft",
    "ready: choose a layout and connect USB"
  ];
}

function renderRecoveryMode(modeName) {
  const mode = recoveryModes[modeName] || recoveryModes.normal;
  recoveryButtons.forEach((button) => {
    const active = button.dataset.recovery === modeName;
    button.classList.toggle("active", active);
    button.setAttribute("aria-pressed", String(active));
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

function selectInstallMode(modeName) {
  installModeButtons.forEach((button) => {
    const active = button.dataset.installMode === modeName;
    button.setAttribute("aria-selected", String(active));
    button.tabIndex = active ? 0 : -1;
  });
  installModePanels.forEach((panel) => {
    const active = panel.dataset.modePanel === modeName;
    panel.hidden = !active;
    panel.classList.toggle("active", active);
  });
  setTicker(modeName === "dual" ? [
    "layout: Z-Deck OTA A/B + dedicated MeshCore",
    "storage: LittleFS and NVS are not written",
    "switch: manual only; current system stays active",
    "ready: connect T-Deck and authorize serial"
  ] : releaseIdleLines());
}

function armInstaller(label, layout) {
  setTicker([
    "status: serial action requested",
    "next: choose the T-Deck port",
    `release: ${label}`,
    `flash map: ${layout}`,
    "keep USB connected through verification"
  ]);
}

async function loadRelease() {
  try {
    const response = await fetch("update.json", { cache: "no-store" });
    if (!response.ok) throw new Error(`update.json returned ${response.status}`);
    const data = await response.json();
    if (!data.latest?.packVersion || !data.latest?.firmwareVersion) throw new Error("release metadata is incomplete");

    release = data.latest;
    document.querySelectorAll("[data-release-title]").forEach((element) => { element.textContent = release.title; });
    document.querySelectorAll("[data-firmware-version]").forEach((element) => { element.textContent = release.firmwareVersion; });
    document.querySelectorAll("[data-screen-version]").forEach((element) => { element.textContent = release.packVersion; });
    if (releaseNotes) releaseNotes.textContent = release.notes || "Current app-only OTA release preserves local configuration and SD data.";
    setTicker(releaseIdleLines());
  } catch (error) {
    document.querySelectorAll("[data-release-title]").forEach((element) => { element.textContent = "Release metadata unavailable"; });
    if (releaseNotes) releaseNotes.textContent = "The installer could not read update.json. Check the site connection before flashing.";
    setTicker(["status: release metadata failed", `error: ${error.message}`, "action: reload before flashing"]);
  }
}

async function loadCommits() {
  if (!commitList) return;
  try {
    const response = await fetch("https://api.github.com/repos/Its-ze/Z-Deck-Web-Flasher/commits?per_page=5", {
      headers: { Accept: "application/vnd.github+json" }
    });
    if (!response.ok) throw new Error("GitHub history unavailable");
    const commits = await response.json();
    commitList.replaceChildren(...commits.map((commit) => {
      const item = document.createElement("li");
      const link = document.createElement("a");
      link.href = commit.html_url;
      link.target = "_blank";
      link.rel = "noreferrer";
      link.textContent = commit.commit.message.split("\n")[0];
      const date = document.createElement("span");
      date.textContent = ` - ${new Date(commit.commit.author.date).toLocaleDateString()}`;
      item.append(link, date);
      return item;
    }));
  } catch {
    const item = document.createElement("li");
    item.textContent = "GitHub history did not load. Use the GitHub link for the complete commit list.";
    commitList.replaceChildren(item);
  }
}

installModeButtons.forEach((button) => button.addEventListener("click", () => selectInstallMode(button.dataset.installMode)));
installButton?.addEventListener("click", () => armInstaller(release.packVersion, "boot + Z-Deck OTA A/B + LittleFS"));
dualInstallButton?.addEventListener("click", () => armInstaller(`${release.packVersion} + MeshCore`, "boot + Z-Deck OTA A/B + dedicated MeshCore"));
otaTestInstallButton?.addEventListener("click", () => armInstaller("Legacy 0.2.53 OTA test", "zdeck54 baseline to zdeck57 OTA + dedicated MeshCore; use Standard for current zdeck64"));
recoveryButtons.forEach((button) => button.addEventListener("click", () => renderRecoveryMode(button.dataset.recovery)));

openDonglePairing?.addEventListener("click", () => {
  const url = "http://192.168.4.1/";
  window.open(url, "_blank", "noopener,noreferrer");
  if (donglePairingStatus) donglePairingStatus.textContent = `Opening dongle-hosted setup UI at ${url}`;
  setTicker(["status: VoidLink UI requested", "network: T-Dongle USB adapter", `url: ${url}`, "pairing: controlled by dongle web UI"]);
});

applyManifest?.addEventListener("click", () => {
  const value = customManifest?.value.trim() || "";
  if (!value) {
    installButton?.setAttribute("manifest", "manifest.json");
    if (manifestStatus) manifestStatus.textContent = "Using bundled standard Z-Deck manifest.";
    setTicker(releaseIdleLines());
    return;
  }

  try {
    const parsed = new URL(value);
    const local = ["localhost", "127.0.0.1"].includes(parsed.hostname);
    if (parsed.protocol !== "https:" && !local) throw new Error("Manifest must use HTTPS or localhost");
    installButton?.setAttribute("manifest", parsed.href);
    if (manifestStatus) manifestStatus.textContent = `Custom standard manifest armed: ${parsed.href}`;
    setTicker(["status: custom manifest armed", `manifest: ${parsed.href}`, "warning: only flash manifests you trust"]);
  } catch (error) {
    if (manifestStatus) manifestStatus.textContent = error.message || "Invalid manifest URL";
    setTicker(["status: manifest rejected", `error: ${error.message || "invalid URL"}`]);
  }
});

document.addEventListener("DOMContentLoaded", () => window.lucide?.createIcons());
renderRecoveryMode("normal");
loadRelease();
loadCommits();
