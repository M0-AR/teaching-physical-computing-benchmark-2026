"""Exp 06 — Reproduce everything end-to-end (zero-to-hero entry point)."""
import subprocess, sys

SCRIPTS = ["experiments/01_curriculum_audit.py",
           "experiments/02_hardware_benchmark.py",
           "experiments/03_literature_triangulation.py",
           "experiments/04_market_validation.py",
           "experiments/05_hidden_patterns.py"]

fails = 0
for s in SCRIPTS:
    print(f"\n===== {s} =====")
    r = subprocess.run([sys.executable, s])
    if r.returncode != 0:
        fails += 1
        print(f"FAILED: {s}")
print("\n" + ("ALL GREEN — reproducible" if fails == 0 else f"{fails} FAILED"))
sys.exit(fails)
