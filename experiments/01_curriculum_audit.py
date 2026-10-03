"""Exp 01 — Curriculum audit: verify 4-course / 42-week / IPO-invariant structure."""
import csv, json, os
from pcb_benchmark.curriculum import COURSES, PROGRAM_TOTALS, total_modules

OUT = "results/tables/exp01_curriculum.csv"
os.makedirs("results/tables", exist_ok=True)

rows = [{"code": c.code, "title": c.title, "weeks": c.weeks,
         "hours_pw": c.hours_per_week, "modules": len(c.modules),
         "ends_with_investigation": c.modules[-1].lower() == "classroom investigation"}
        for c in COURSES]

with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)

total_weeks = sum(c.weeks for c in COURSES)
assert total_weeks == PROGRAM_TOTALS["weeks"] == 42, total_weeks
assert len(COURSES) == 4
assert all(r["ends_with_investigation"] for r in rows), "HIDDEN PATTERN: every course ends with classroom investigation"
assert total_modules() == 42, total_modules()  # 10+12+10+10 modules = 42 — mirrors weeks

print(f"[01] OK: {len(COURSES)} courses, {total_weeks} weeks, {total_modules()} modules")
print(f"[01] PATTERN: modules==weeks==42; 100% end with 'Classroom investigation' (transfer task)")
print(f"[01] wrote {OUT}")
