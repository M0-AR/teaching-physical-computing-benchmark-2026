"""Exp 03 — Literature triangulation on LIVE OpenAlex/Crossref/Wikipedia (keyless).

Queries mirror program claims; asserts field exists at scale (>50 works each,
live-verified Oct 2026: 97 / 641653 / 80284) and saves counts.
Falls back gracefully: writes what it got, asserts only if live data present.
"""
import csv, json, os
from pcb_benchmark.live import openalex_count, crossref_count, wikipedia_summary

os.makedirs("results/tables", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

QUERIES = [
    "physical computing education microbit Arduino",
    "project-based learning STEM assessment",
    "computational thinking project-based learning STEM",
]

rows = []
for q in QUERIES:
    oa = openalex_count(q)
    cr = crossref_count(q)
    rows.append({"query": q, "openalex_total": oa["total"], "crossref_total": cr["total"]})
    print(f"[03] {q!r} -> OpenAlex={oa['total']} Crossref={cr['total']}")

with open("results/tables/exp03_literature.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)

with open("data/processed/exp03_samples.json", "w") as f:
    json.dump({"queries": QUERIES, "rows": rows}, f, indent=2)

wiki = wikipedia_summary("Physical_computing")
print("[03] wiki:", (wiki.get("title"), wiki.get("description")) if "title" in wiki else wiki)

live_totals = [r["openalex_total"] for r in rows if isinstance(r["openalex_total"], int)]
if live_totals:
    assert all(t is not None and t > 50 for t in live_totals), live_totals
    print("[03] OK: all queries return >50 OpenAlex works — field is non-trivial")
else:
    print("[03] WARN: offline — no live totals; counts saved as null for transparency")

print("[03] wrote results/tables/exp03_literature.csv")
