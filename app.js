const lines = [
  "deck bus: waiting for USB-C signal",
  "serial probe: ESP32-S3 target expected",
  "firmware: Z-Deck 0.2.0-public",
  "layout: app0 + app1 + littlefs",
  "ready: connect deck and authorize serial"
];

let index = 0;
const ticker = document.getElementById("ticker");
const installButton = document.getElementById("installButton");
const customManifest = document.getElementById("customManifest");
const applyManifest = document.getElementById("applyManifest");
const manifestStatus = document.getElementById("manifestStatus");
const commitList = document.getElementById("commitList");

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
