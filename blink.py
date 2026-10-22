import machine, neopixel, time

led = neopixel.NeoPixel(machine.Pin(8), 1)

while True:
    led[0] = (20, 0, 0)  # red
    led.write()
    time.sleep(0.5)
    led[0] = (0, 0, 0)   # off
    led.write()
    time.sleep(0.5)