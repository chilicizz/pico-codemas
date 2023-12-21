from machine import Pin
import time

# set up tilt sensor pin
tilt = Pin(26, Pin.IN, Pin.PULL_DOWN)

while True:
    time.sleep(0.01)

    if tilt.value() == 1: # if sensor is HIGH
        print("I tilted!") 
