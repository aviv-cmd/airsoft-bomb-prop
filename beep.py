from machine import Pin
import time

buzzer = Pin(2, Pin.OUT)

for i in range(5):
    buzzer.value(1)
    time.sleep(0.15)
    buzzer.value(0)
    time.sleep(0.15)