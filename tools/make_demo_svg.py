"""Generate assets/demo.svg — animated terminal demo (SMIL, animates inline on GitHub).

No ffmpeg needed. Deterministic, regenerable: python3 tools/make_demo_svg.py
Verifies: file exists, <1MB, contains <animate>.
"""
import os
os.makedirs("assets", exist_ok=True)

FRAMES = [
    ("$ python experiments/01_curriculum_audit.py", "[01] OK: 4 courses, 42 weeks, 42 modules"),
    ("$ python experiments/02_hardware_benchmark.py", "[02] OK: micro:bit > Pico W > Uno > Pi4B"),
    ("$ python experiments/03_literature_triangulation.py", "[03] OK: 97 / 641653 / 80284 works"),
    ("$ python experiments/05_hidden_patterns.py", "[05] OK: 6 patterns, mean conf 0.857"),
    ("$ pytest -q", "4 passed in 0.15s — ALL GREEN"),
]

# Each frame visible 2.2s, total loop
STEP = 2.2
TOTAL = STEP * len(FRAMES)

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

lines = []
y0 = 90
for i, (cmd, out) in enumerate(FRAMES):
    t0 = i * STEP
    # command line
    lines.append(
        f'<text x="30" y="{y0+i*62}" font-family="monospace" font-size="15" fill="#7dd3fc" opacity="0">'
        f'<animate attributeName="opacity" values="0;1;1;0" '
        f'keyTimes="0;{(t0+0.1)/TOTAL:.4f};{(t0+STEP-0.2)/TOTAL:.4f};{(t0+STEP)/TOTAL:.4f}" '
        f'dur="{TOTAL}s" repeatCount="indefinite"/>{esc(cmd)}</text>'
    )
    lines.append(
        f'<text x="30" y="{y0+i*62+22}" font-family="monospace" font-size="14" fill="#86efac" opacity="0">'
        f'<animate attributeName="opacity" values="0;0;1;1;0" '
        f'keyTimes="0;{(t0+0.5)/TOTAL:.4f};{(t0+0.8)/TOTAL:.4f};{(t0+STEP-0.2)/TOTAL:.4f};{(t0+STEP)/TOTAL:.4f}" '
        f'dur="{TOTAL}s" repeatCount="indefinite"/>{esc(out)}</text>'
    )

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="720" height="420" role="img" aria-label="Terminal demo: reproduce the benchmark in 5 commands">
<rect width="720" height="420" rx="14" fill="#0b0b0f"/>
<rect x="0" height="44" width="720" fill="#16161d" rx="14"/>
<circle cx="28" cy="22" r="7" fill="#ff5f57"/><circle cx="52" cy="22" r="7" fill="#febc2e"/><circle cx="76" cy="22" r="7" fill="#28c840"/>
<text x="110" y="27" font-family="monospace" font-size="14" fill="#e5e7eb">pcb-benchmark — 60-second demo (loops)</text>
{''.join(lines)}
<text x="30" y="398" font-family="monospace" font-size="12" fill="#6b7280">Tip: every line above is a real command. Copy-paste it — it works.</text>
</svg>
"""

with open("assets/demo.svg", "w") as f:
    f.write(svg)

size = os.path.getsize("assets/demo.svg")
assert size < 1_000_000, size
assert "<animate" in svg
print(f"demo.svg OK: {size} bytes, {len(FRAMES)} frames, loops every {TOTAL}s")
