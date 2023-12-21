from machine import Pin
import time

tilt = Pin(26, Pin.IN, Pin.PULL_DOWN)

tiltcounter = 0

state = 0

while True:
    time.sleep(0.1)

    if state == 0 and tilt.value() == 1:
        tiltcount = tiltcount + 1
        state = 1
        print("tilts =", tiltcount)

    if state == 1 and tilt.value() == 0:
        state = 0
