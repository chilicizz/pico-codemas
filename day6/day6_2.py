from machine import ADC, Pin
import time

# set up LEDs
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

# Define pin for our sensor
lightsensor = ADC(Pin(26))

while True:
    # Read sensor value and store it in a variable called light
    light =  lightsensor.read_u16()

    # convert to percentage
    lightpercent = round(light/65535 * 100, 1)

    print(lightpercent)
    
    time.sleep(1)
    
    if lightpercent <= 30:
        red.value(1)
        amber.value(0)
        green.value(0)
    elif 30 < lightpercent < 60:
        red.value(0)
        amber.value(1)
        green.value(0)
    elif lightpercent >= 60:
        red.value(0)
        amber.value(0)
        green.value(1)
        
        
