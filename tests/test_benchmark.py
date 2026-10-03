from pcb_benchmark.curriculum import COURSES, PROGRAM_TOTALS, total_modules
from pcb_benchmark.hardware import HARDWARE, AFFORDANCE

def test_program_totals():
    assert sum(c.weeks for c in COURSES) == 42
    assert PROGRAM_TOTALS["courses"] == 4
    assert total_modules() == 42

def test_every_course_ends_with_investigation():
    for c in COURSES:
        assert c.modules[-1] == "Classroom investigation"

def test_hardware_ladder_order():
    means = {d: sum(v)/len(v) for d, v in AFFORDANCE.items()}
    assert means["BBC micro:bit v2"] > means["Raspberry Pi Pico W"]
    assert means["Raspberry Pi Pico W"] > means["Arduino Uno R3"]
    assert means["Arduino Uno R3"] > means["Raspberry Pi 4B 4GB"]

def test_price_floor():
    los = sorted(HARDWARE, key=lambda h: h["price_usd"][0])
    assert los[0]["device"] == "Raspberry Pi Pico W"
