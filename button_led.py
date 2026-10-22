import machine
import neopixel
import time

led = neopixel.NeoPixel(machine.Pin(8), 1)
button = machine.Pin(9, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    if button.value() == 0:
        led[0] = (0, 20, 0)
    else:
        led[0] = (20, 0, 0)
    led.write()
    time.sleep(0.02)