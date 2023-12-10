from machine import Pin, PWM
import time

buzzer = PWM(Pin(13))

# Tones
A = 440
As = 466
B = 494
C = 523
Cs = 554
D = 587
Ds - 622
E = 659
F = 698
Fs = 740
G = 784
Gs = 830

# volume (Duty Cycle)
volume = 32768

# Function for playing tones
def playtone(note, vol, delay1, delay2):
    buzzer.duty_u16(vol)
    buzzer.freq(note)
    time.sleep(delay1)
    buzzer.duty_u16(0)
    time.sleep(delay2)
    
# Play the tune
playtone(E,volume,0.1,0.2)
playtone(E,volume,0.1,0.2)
playtone(E,volume,0.1,0.5) #Longer second delay

playtone(E,volume,0.1,0.2)
playtone(E,volume,0.1,0.2)
playtone(E,volume,0.1,0.5) #Longer second delay

playtone(E,volume,0.1,0.2)
playtone(G,volume,0.1,0.2)
playtone(C,volume,0.1,0.2)
playtone(D,volume,0.1,0.2)
playtone(E,volume,0.1,0.2)

# Duty to 0 to turn the buzzer off
buzzer.duty_u16(0)