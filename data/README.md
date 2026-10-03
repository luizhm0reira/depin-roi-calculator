# DePIN ROI Calculator — hardware dataset

`hardware.json` is the hardware catalog for the DePIN ROI calculator.
All content is in English. Prices are USD.

## What's in here

- **22 products / 41 variants** across 14 networks:
  Helium IoT, Helium Mobile, GEODNET, Wingbits, Onocoy, Hivemapper,
  WeatherXM, DIMO, Nubila, ROVR, DeNet, Silencio, Karrier One, Sensmos.
- The key differentiator is preserved: **variants are separate records**
  (ROVR Tarantula TX $150 vs LC $2,500; HYFIX WB200 vs MGW310;
  Helium Mobile Indoor vs Outdoor, etc.), so the calculator never has to
  assume the wrong model — the exact complaint from the Moken forum thread.
- App/software-only networks are included with empty `variants` and an
  explanatory note (DeNet, Silencio), so the calculator can show
  "$0 hardware needed" instead of a broken lookup.

## Verified vs estimated

- **Verified prices (official stores, Sep–Oct 2026):** RAK Hotspot Miner v2
  ($204), SenseCAP M1 ($519), Helium Mobile Indoor/Outdoor ($249.99/$499.99),
  HYFIX MobileCM triple-band ($695), HYFIX WB200 ($495) / MGW310 ($1,095),
  Hivemapper Bee LTE/WiFi ($589/$449), WeatherXM D1/H2/Pulse ($199/$239/$610),
  Sixents G20 for Onocoy ($649).
- **Community-reported prices:** ROVR Tarantula TX/LC ($150/$2,500, via Moken
  forum + HeliumDeploy), Nubila Marco ($299, distributor press).
- **DIY BOM estimates (marked in `notes`, never presented as retail):**
  Wingbits DIY build (~$300 — earns ZERO for new miners, kept as a warning),
  Onocoy UM980 DIY route (~$330, accepted), Sensmos ESP32 node (~$10).
- **`price_usd: null` (13 variants):** no verifiable current listing was found —
  the calculator must NOT guess these. See "Known gaps".

## Data freshness policy

- **This file covers hardware only.** Token prices move constantly — the
  calculator fetches live token prices separately (e.g. CoinGecko) and must
  never hard-code a token price here.
- **Hardware prices also rot.** Rule of thumb: re-verify `price_usd` for
  every product marked `data_quality: shaky` before any public launch, and
  refresh the whole file at least monthly. Each record carries
  `last_verified` (currently `2026-10-02`).
- **`typical_daily_tokens` is the weakest field** — only 4 products have one.
  Networks rarely publish per-device daily figures; treat any value here as a
  community-sourced starting point the user should override, not as truth.

## Known gaps (fix before launch)

1. **Daily token earnings are unverifiable for most networks.** Helium IOT,
   Hivemapper HONEY, WeatherXM WXM, Onocoy ONO publish no per-device daily
   figures. No source publishes 2026 per-hardware daily numbers for Helium
   hotspots; community consensus puts post-2025-halving hotspots at roughly
   $0–8/month. Do not invent these numbers in the UI.
2. **Power draw:** vendors publish connectivity/battery specs, not watts, for
   most USB/solar/OBD2 devices (`power_watts: null`). Electricity cost matters
   little for these (all <12W), but the field should show "n/a" not "0".
3. **DIMO prices are stale-risk:** all four DIMO prices come from a June 2025
   article; shop.dimo.zone wouldn't load. Marked `shaky` — re-verify.
4. **Milesight UG65/UG67:** no USD MSRP; only regional reseller prices
   (NZD/EUR/ZAR). Marked `shaky`.
5. **Karrier One (`sparse`):** the "$290 reseller phone / store closed" claim
   from earlier research could NOT be verified. What exists: HOTSPOT1 WiFi
   (~$200–300, Nov 2025 community guide, no live listing) and Gatekeeper
   cellular nodes; the official store still showed "Order Now" in an Aug 2026
   crawl. Price left null; needs a live-browser check.
6. **Nubra "dual miner" was a bad premise:** only the Marco station exists
   (validator nodes are Monad licenses, not hardware). Record corrected.
7. **SenseCAP M2 is NOT Helium-compatible** (current "Multi-Platform" SKU);
   record kept with an explicit exclusion note so the calculator never offers it.
8. **Nebra is effectively defunct** (dead storefronts, stale repos since
   ~Jul 2025); record kept as legacy with a warning.
9. **Helium Mobile:** MOBILE emissions ended 2026-01-15 per HIP-138 — rewards
   now in HNT. Any copy referencing "earn MOBILE" is wrong.
10. **Wingbits DIY:** BYOD closed to new entrants Oct 14, 2024. A new DIY build
    earns zero WINGS — kept in the dataset as an explicit warning, not an option.
11. **affiliate_url is null everywhere (placeholder).** Luiz adds his own links
    later. `affiliate_note` records which programs were found (HeliumDeploy
    Creator/distributor codes, WeatherXM reseller program, FreshMiners codes).

## Schema

Each product: `id`, `name`, `network`, `token_symbol`, `variants[]`
(`variant_name`, `price_usd`, `power_watts`, `notes`), `earnings_model`,
`estimate_source` (`official` | `community` | `unverifiable`),
`typical_daily_tokens` (`{low, high, basis}` or null), `affiliate_url`,
`sources[]`, `last_verified`, `data_quality` (`solid` | `shaky` | `sparse`),
`affiliate_note`.
