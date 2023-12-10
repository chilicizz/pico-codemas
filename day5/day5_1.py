from machine import Pin, PWM
import time

# Set up the buzzer pin as PWM
buzzer = PWM(Pin(13))

# Set PWM frequency to 1000
buzzer.freq(1000)

# Set PWM duty
buzzer.duty_u16(10000)
time.sleep(1)

buzzer.freq(500)
time.sleep(1)

# duty to 0 to turn the buzzer off
buzzer.duty_u16(0)
