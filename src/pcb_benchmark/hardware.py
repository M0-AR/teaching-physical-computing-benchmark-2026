"""Hardware ladder: public spec sheet for classroom benchmark.

Prices are 2026 street-price bands (USD) — verified via web search Oct 2026,
stored as ranges so the benchmark tests ORDER not exact price (robust to FX).
Specs are manufacturer public specs (Nordic nRF52833 / ATmega328P / RP2040 / BCM).
"""
HARDWARE = [
    {"device": "BBC micro:bit v2", "mcu": "nRF52833 64MHz Cortex-M4",
     "ram_kb": 128, "flash_kb": 512, "gpio": 25, "sensors_onboard": 5,
     "lang": "MakeCode blocks/Python", "price_usd": (14, 18),
     "power": "3V batt/USB", "classroom_score_entry": 10},
    {"device": "Arduino Uno R3", "mcu": "ATmega328P 16MHz AVR",
     "ram_kb": 2, "flash_kb": 32, "gpio": 20, "sensors_onboard": 0,
     "lang": "C++/Scratch-bridge", "price_usd": (23, 28),
     "power": "5V USB/7-12V", "classroom_score_entry": 7},
    {"device": "Raspberry Pi Pico W", "mcu": "RP2040 133MHz dual-M0+",
     "ram_kb": 264, "flash_kb": 2048, "gpio": 26, "sensors_onboard": 1,
     "lang": "MicroPython/C", "price_usd": (6, 10),
     "power": "USB/1.8-5.5V", "classroom_score_entry": 8},
    {"device": "Raspberry Pi 4B 4GB", "mcu": "BCM2711 1.5GHz quad-A72",
     "ram_kb": 4194304, "flash_kb": 0, "gpio": 40, "sensors_onboard": 0,
     "lang": "Python/Linux full", "price_usd": (55, 75),
     "power": "5V 3A USB-C", "classroom_score_entry": 5},
]

# Pedagogical affordance rubric (1-5) — scored from literature + Arm resources
AFFORDANCE = {
    # device: [tinkering_immediacy, scaffolding, resilience_to_failure, assessment_visibility, curriculum_fit_ages_9_14]
    "BBC micro:bit v2": [5, 5, 5, 5, 5],
    "Arduino Uno R3": [3, 3, 3, 4, 3],
    "Raspberry Pi Pico W": [4, 4, 4, 4, 4],
    "Raspberry Pi 4B 4GB": [2, 2, 2, 3, 2],
}
