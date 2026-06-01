const idleLines = [
  "status: waiting for T-Deck",
  "firmware: Z-Deck 0.2.3-public / LongFast",
  "target: ESP32-S3 / t-deck-tft",
  "bundle: ringtone fix + stable serial recovery",
  "ready: connect deck and authorize serial"
];

const ticker = document.getElementById("ticker");
const installButton = document.getElementById("installButton");
const customManifest = document.getElementById("customManifest");
const applyManifest = document.getElementById("applyManifest");
const manifestStatus = document.getElementById("manifestStatus");
const commitList = document.getElementById("commitList");

function setTicker(lines) {
  if (!ticker) return;
  ticker.textContent = lines.map((line) => "> " + line).join("\n");
}

setTicker(idleLines);

installButton.addEventListener("click", () => {
  setTicker([
    "status: serial action requested",
    "next: choose the T-Deck port in the browser prompt",
    "firmware: Z-Deck 0.2.3-public / LongFast",
    "flash map: app0 + app1 + littlefs",
    "features: SD reset tool + USB SD disabled"
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

