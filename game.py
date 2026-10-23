import machine
import neopixel
import time

led = neopixel.NeoPixel(machine.Pin(8), 1)
button = machine.Pin(9, machine.Pin.IN, machine.Pin.PULL_UP)      # BOOT button
ext_button = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_UP)  # wires: pin 3 to GND
buzzer = machine.Pin(2, machine.Pin.OUT)
buzzer.value(0)

TOTAL_SECONDS = 40
DEFUSE_SECONDS = 10

def show(color):
    led[0] = color
    led.write()

def pressed():
    # True if BOOT is pressed or the wires on pin 3 touch GND
    return button.value() == 0 or ext_button.value() == 0

def wait_for_press():
    while pressed():
        time.sleep(0.02)
    show((0, 0, 20))
    while not pressed():
        time.sleep(0.02)
    while pressed():
        time.sleep(0.02)

def play():
    start = time.ticks_ms()
    next_flash = 0
    next_hold_beep = 0
    hold_start = None
    while True:
        now = time.ticks_ms()
        elapsed = time.ticks_diff(now, start) / 1000
        if elapsed >= TOTAL_SECONDS:
            return "BOOM"
        if pressed():
            if hold_start is None:
                hold_start = now
            held = time.ticks_diff(now, hold_start) / 1000
            show((0, 20, 0))
            if time.ticks_diff(now, next_hold_beep) >= 0:
                buzzer.value(1)
                time.sleep(0.05)
                buzzer.value(0)
                next_hold_beep = time.ticks_add(now, 500)
            if held >= DEFUSE_SECONDS:
                return "DEFUSED"
        else:
            hold_start = None
            remaining = TOTAL_SECONDS - elapsed
            if time.ticks_diff(now, next_flash) >= 0:
                show((20, 0, 0))
                buzzer.value(1)
                time.sleep(0.05)
                show((0, 0, 0))
                buzzer.value(0)
                wait_ms = int((0.1 + remaining / TOTAL_SECONDS * 0.9) * 1000)
                next_flash = time.ticks_add(now, wait_ms)
        time.sleep(0.01)

while True:
    print("Press BOOT or touch the wires to arm")
    wait_for_press()
    result = play()
    print(result)
    if result == "DEFUSED":
        show((0, 20, 0))
        buzzer.value(1)
        time.sleep(0.2)
        buzzer.value(0)
        time.sleep(2.8)
    else:
        show((20, 0, 0))
        buzzer.value(1)
        time.sleep(2)
        buzzer.value(0)
        time.sleep(1)