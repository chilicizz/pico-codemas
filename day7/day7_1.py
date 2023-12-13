# motion sensor
from machine import Pin
import time

# set up PIR pin with Pull Down
pir = Pin(26, Pin.IN, Pin.PULL_DOWN)

print("Warming up...")
time.sleep(10) # Delay to allow the sensor to settle
print("Sensor ready!")

while True:
    time.sleep(0.01)
    if pir.value() == 1: # If movement is detected
        print("I SEE YOU!")
        time.sleep(5)
        print("Sensor active") # let us know that it is active again