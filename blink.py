import machine, neopixel, time

led = neopixel.NeoPixel(machine.Pin(8), 1)

while True:
    led[0] = (20, 0, 0)
    led.write()
    time.sleep(0.1)
    led[0] = (0, 0, 0)
    led.write()
    time.sleep(0.5)