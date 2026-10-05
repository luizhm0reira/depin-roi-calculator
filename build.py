#!/usr/bin/env python3
"""Build the self-contained DePIN ROI calculator page.

Reads data/hardware.json and inlines it into template.html,
writing a single deployable index.html (no build step, no npm).

Works from both layouts:
  - <project>/app/build.py  with data at <project>/data/hardware.json
  - <repo>/build.py         with data at <repo>/data/hardware.json

Usage: python3 build.py
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).parent

# Locate the dataset in either layout.
candidates = [HERE.parent / "data" / "hardware.json", HERE / "data" / "hardware.json"]
DATA_PATH = next((p for p in candidates if p.exists()), None)
if DATA_PATH is None:
    raise SystemExit(f"hardware.json not found; tried: {', '.join(map(str, candidates))}")
DATA = json.load(open(DATA_PATH))

TEMPLATE = (HERE / "template.html").read_text()

# Structural validation (no fixed counts — products/variants are meant to grow).
PRODUCT_KEYS = ("id", "name", "network", "token_symbol", "variants",
                "earnings_model", "typical_daily_tokens", "affiliate_url",
                "sources", "last_verified", "data_quality")
VARIANT_KEYS = ("variant_name", "price_usd", "power_watts", "notes")

prods = DATA["products"]
assert isinstance(prods, list) and len(prods) > 0, "products must be a non-empty list"
seen_ids = set()
for p in prods:
    for k in PRODUCT_KEYS:
        assert k in p, f"product {p.get('id')} missing key {k}"
    assert p["id"] not in seen_ids, f"duplicate product id {p['id']}"
    seen_ids.add(p["id"])
    assert isinstance(p["variants"], list), f"product {p['id']}: variants must be a list"
    for v in p["variants"]:
        for k in VARIANT_KEYS:
            assert k in v, f"variant in {p['id']} missing key {k}"
        assert v["price_usd"] is None or isinstance(v["price_usd"], (int, float)), \
            f"variant {v['variant_name']} in {p['id']}: price_usd must be a number or null"
total_vars = sum(len(p["variants"]) for p in prods)

# Escape closing tags so the JSON can't break out of the <script> block.
blob = json.dumps(DATA, ensure_ascii=False).replace("</", "<\\/")

html = TEMPLATE.replace("/*__DATA__*/", "const DATA = " + blob + ";")
assert "/*__DATA__*/" not in html, "data placeholder not replaced"
assert html.count("const DATA = ") == 1

out = HERE / "index.html"
out.write_text(html)
print(f"wrote {out} ({len(html)/1024:.1f} KB) — {len(prods)} products, {total_vars} variants")
