# Imports
from machine import Pin
import time

# Set up our button name and GPIO pin number
# Also set the pin as an input and use a pull down
button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

while True: # Loop forever

    time.sleep(0.2) # Short delay
    if button1.value() == 1: #If button 1 is pressed
        print("Button 1 pressed")
    if button2.value() == 1: #If button 1 is pressed
        print("Button 2 pressed")
    if button3.value() == 1: #If button 1 is pressed
        print("Button 3 pressed")