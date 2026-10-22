import machine
import neopixel
import time

led = neopixel.NeoPixel(machine.Pin(8), 1)
button = machine.Pin(9, machine.Pin.IN, machine.Pin.PULL_UP)

TOTAL_SECONDS = 40
DEFUSE_SECONDS = 10

def show(color):
    led[0] = color
    led.write()

start = time.ticks_ms()
next_flash = 0
hold_start = None

while True:
    now = time.ticks_ms()
    elapsed = time.ticks_diff(now, start) / 1000

    if elapsed >= TOTAL_SECONDS:
        show((20, 0, 0))
        print("BOOM")
        break

    if button.value() == 0:
        if hold_start is None:
            hold_start = now
        held = time.ticks_diff(now, hold_start) / 1000
        show((0, 20, 0))
        if held >= DEFUSE_SECONDS:
            print("DEFUSED")
            break
    else:
        hold_start = None
        remaining = TOTAL_SECONDS - elapsed
        if time.ticks_diff(now, next_flash) >= 0:
            show((20, 0, 0))
            time.sleep(0.05)
            show((0, 0, 0))
            wait_ms = int((0.1 + remaining / TOTAL_SECONDS * 0.9) * 1000)
            next_flash = time.ticks_add(now, wait_ms)

    time.sleep(0.01)