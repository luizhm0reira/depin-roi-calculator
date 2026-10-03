# DePIN ROI Calculator

Honest payback math for DePIN hardware — per exact hardware variant.

Most trackers (e.g. Moken) don't let you pick the exact hardware variant, so ROI math silently assumes the wrong model (e.g. ROVR Tarantula TX $150 vs LC $2,500). This calculator fixes that: pick the network, the product, the exact variant, your electricity rate, and get payback months, $/day, and break-even date — with live token prices via CoinGecko.

## Live site

Hosted on GitHub Pages: enable it in **Settings → Pages → Deploy from branch → main → /**.

## Updating the data

1. Edit `data/hardware.json` (add products/variants — copy the structure of an existing entry).
2. Rebuild: `python3 build.py` (validates the dataset and regenerates `index.html`).
3. Commit and push — the site updates automatically.

## Project structure

- `index.html` — the deployable app (built, self-contained, no dependencies)
- `template.html` / `build.py` — source template and build script
- `data/hardware.json` — the hardware dataset (prices, power draw, networks, reward models)
- `data/README.md` — data freshness policy and known gaps

## Data policy

- Hardware prices re-verified monthly; token prices always fetched live, never hard-coded.
- Estimates are user-editable and clearly labeled — never presented as truth.
- Estimates only. Not financial advice.

Built October 2026.
