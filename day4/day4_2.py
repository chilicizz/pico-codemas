from machine import ADC, Pin
import time

# Set up the potentiometer on ADS pin 27
potentiometer = ADC(Pin(27))

#Set up our LED names and GPIO pin numbers
led = Pin(18, Pin.OUT)

mydelay = 0

while True:
    #update our variable with the reading divided by 65000
    mydelay = potentiometer.read_u16() / 65000
    
    led.value(1)
    time.sleep(mydelay)
    
    led.value(0)
    time.sleep(mydelay)