const lines = [
  "deck bus: waiting for USB-C signal",
  "serial probe: ESP32-S3 target expected",
  "firmware: Z-Deck 2.8.0.itsz1",
  "layout: app0 + app1 + littlefs",
  "ready: connect deck and authorize serial"
];

let index = 0;
const ticker = document.getElementById("ticker");
const installButton = document.getElementById("installButton");
const customManifest = document.getElementById("customManifest");
const applyManifest = document.getElementById("applyManifest");
const manifestStatus = document.getElementById("manifestStatus");

function tick() {
  index = (index + 1) % lines.length;
  const visible = [];
  for (let i = 0; i < 4; i += 1) {
    visible.push("> " + lines[(index + i) % lines.length]);
  }
  ticker.textContent = visible.join("\n");
}

tick();
window.setInterval(tick, 1400);

applyManifest.addEventListener("click", () => {
  const value = customManifest.value.trim();
  if (!value) {
    installButton.setAttribute("manifest", "manifest.json");
    manifestStatus.textContent = "Default manifest: bundled Z-Deck firmware.";
    return;
  }

  try {
    const parsed = new URL(value);
    if (parsed.protocol !== "https:" && parsed.hostname !== "localhost" && parsed.hostname !== "127.0.0.1") {
      throw new Error("Manifest must be HTTPS or localhost.");
    }
    installButton.setAttribute("manifest", parsed.href);
    manifestStatus.textContent = "Custom manifest armed: " + parsed.href;
  } catch (error) {
    manifestStatus.textContent = error.message || "That manifest URL is not valid.";
  }
});
