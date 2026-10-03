#!/usr/bin/env python3
"""Build the self-contained DePIN ROI calculator page.

Reads ../data/hardware.json and inlines it into template.html,
writing a single deployable index.html (no build step, no npm).

Usage: python3 build.py
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).parent
DATA = json.load(open(HERE.parent / "data" / "hardware.json"))
TEMPLATE = (HERE / "template.html").read_text()

# Validate dataset shape before inlining
prods = DATA["products"]
assert len(prods) == 22, f"expected 22 products, got {len(prods)}"
total_vars = sum(len(p["variants"]) for p in prods)
assert total_vars == 41, f"expected 41 variants, got {total_vars}"
for p in prods:
    for k in ("id", "name", "network", "token_symbol", "variants",
              "earnings_model", "typical_daily_tokens", "affiliate_url",
              "sources", "last_verified", "data_quality"):
        assert k in p, f"product {p.get('id')} missing key {k}"

# Escape closing tags so the JSON can't break out of the <script> block.
blob = json.dumps(DATA, ensure_ascii=False).replace("</", "<\\/")

html = TEMPLATE.replace("/*__DATA__*/", "const DATA = " + blob + ";")
assert "/*__DATA__*/" not in html, "data placeholder not replaced"
assert html.count("const DATA = ") == 1

out = HERE / "index.html"
out.write_text(html)
print(f"wrote {out} ({len(html)/1024:.1f} KB) — {len(prods)} products, {total_vars} variants")
