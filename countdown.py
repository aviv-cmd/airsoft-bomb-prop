import machine
import neopixel
import time

led = neopixel.NeoPixel(machine.Pin(8), 1)

TOTAL_SECONDS = 20

def flash():
    led[0] = (20, 0, 0)
    led.write()
    time.sleep(0.05)
    led[0] = (0, 0, 0)
    led.write()

start = time.ticks_ms()

while True:
    elapsed = time.ticks_diff(time.ticks_ms(), start) / 1000
    if elapsed >= TOTAL_SECONDS:
        break
    remaining = TOTAL_SECONDS - elapsed
    flash()
    time.sleep(0.1 + remaining / TOTAL_SECONDS * 0.9)

led[0] = (20, 0, 0)
led.write()
print("BOOM")