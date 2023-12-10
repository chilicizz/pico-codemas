from machine import ADC, Pin, PWM
import time

# Set up the potentiometer on ADS pin 27
potentiometer = ADC(Pin(27))

#Set up our LED names and GPIO pin numbers
# PMW means Pulse Width Modulation determines how long the pulse is ON/OFF
led = PWM(Pin(18))

# Set the PMW frequency
# Sets how often to switch the power between on and off for the LED
led.freq(1000)

reading = 0

while True:
    reading = potentiometer.read_u16()
    
    print(reading)
    
    led.duty_u16(reading)
    
    time.sleep(0.001)