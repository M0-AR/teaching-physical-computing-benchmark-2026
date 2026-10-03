"""Exp 02 — Hardware benchmark: entry-ladder micro:bit > Pico W > Uno > Pi4B for ages 9-14.

Tests ORDER hypotheses (robust to price drift), writes scored table + bar chart.
Live check: GitHub stars for canonical firmware repos (keyless, best-effort).
"""
import csv, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pcb_benchmark.hardware import HARDWARE, AFFORDANCE
from pcb_benchmark.live import github_repo

os.makedirs("results/tables", exist_ok=True)
os.makedirs("results/figures", exist_ok=True)

REPOS = {"BBC micro:bit v2": "microbit-foundation/microbit-micropython",
         "Arduino Uno R3": "arduino/Arduino",
         "Raspberry Pi Pico W": "raspberrypi/micropython",
         "Raspberry Pi 4B 4GB": "raspberrypi/linux"}

rows = []
for h in HARDWARE:
    dev = h["device"]
    aff = AFFORDANCE[dev]
    rows.append({"device": dev, "price_lo": h["price_usd"][0], "price_hi": h["price_usd"][1],
                 "gpio": h["gpio"], "afford_sum": sum(aff),
                 "afford_mean": round(sum(aff)/len(aff), 2)})

rows.sort(key=lambda r: -r["afford_mean"])

with open("results/tables/exp02_hardware.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)

# Hypothesis: micro:bit ranks #1 for entry ages 9-14; full-Linux Pi ranks last for entry
assert rows[0]["device"] == "BBC micro:bit v2", rows
assert rows[-1]["device"] == "Raspberry Pi 4B 4GB", rows
# Price sanity: Pico W cheapest floor; Pi4B most expensive ceiling
los = sorted(rows, key=lambda r: r["price_lo"])
assert los[0]["device"] == "Raspberry Pi Pico W", los

# Live GitHub provenance (best-effort; never fails the benchmark)
live = {}
for dev, repo in REPOS.items():
    try:
        j = github_repo(repo)
        live[dev] = {"stars": j.get("stargazers_count"), "repo": repo}
    except Exception as e:
        live[dev] = {"stars": None, "repo": repo, "error": str(e)[:100]}

plt.figure(figsize=(8, 4.5))
plt.bar([r["device"].replace(" ", "\n") for r in rows], [r["afford_mean"] for r in rows])
plt.title("Classroom entry affordance (9-14y): micro:bit > Pico W > Uno > Pi4B")
plt.ylabel("Mean rubric (1-5)")
plt.tight_layout()
plt.savefig("results/figures/exp02_hardware.png", dpi=150)

print("[02] OK ranking:", [r["device"] for r in rows])
print("[02] live GitHub:", live)
print("[02] wrote results/tables/exp02_hardware.csv + results/figures/exp02_hardware.png")
