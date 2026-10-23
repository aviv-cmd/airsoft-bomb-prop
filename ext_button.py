from machine import Pin
import time

# Push button (or two touching wires) between pin 3 and GND
btn = Pin(3, Pin.IN, Pin.PULL_UP)
last = 1

while True:
    value = btn.value()
    if value != last:
        print("PRESSED" if value == 0 else "released")
        last = value
        time.sleep_ms(30)  # ignore contact bounce
    time.sleep_ms(5)