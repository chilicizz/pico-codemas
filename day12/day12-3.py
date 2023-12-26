# Imports
import time
from machine import Pin
from neopixel import NeoPixel

# Define the strip pin number (28) and number of LEDs (15)
strip = NeoPixel(Pin(28), 15)

# Colour variables
red = 255,0,0
green = 0,255,0
blue = 0,0,255
yellow = 255,255,0
pink = 255,20,147

# iterate over 15 leds
for i in range(15):
    
    # Set each LED in the range to pink
    strip[i] = (pink)

# Send the data to the strip
strip.write()
