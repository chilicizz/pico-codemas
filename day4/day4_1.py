from machine import ADC, Pin
import time

# Set up the potentiometer on ADS pin 27
potentiometer = ADC(Pin(27))

while True:
    print(potentiometer.read_u16()) #read the value
    time.sleep(1) # wait one second