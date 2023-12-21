import onewire, ds18x20, time
from machine import Pin

# Set up the LED pins
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

# set the data pin for the sensor
SensorPin = Pin(26, Pin.IN)

# Tell MicroPython that we're using a DS18B20 sensor and which pin it is on
sensor = ds18x20.DS18X20(onewire.OneWire(SensorPin))

# Look for DS18B20 sensors (each contains a unique rom code)
roms = sensor.scan()

while True:
    time.sleep(5)

    for rom in roms: #For each sensor found (just 1 in our case)
        sensor.convert_temp() # convert the sensor unit to centigrade
        time.sleep(1) # always wait 1 second after converting

        reading = sensor.read_temp(rom) # take a temp reading

        print(reading) 

        if reading <= 18:
            red.value(1)
            amber.value(0)
            green.value(0)

        elif 18 < reading < 22: 
            red.value(0)
            amber.value(1)
            green.value(0)

        elif reading >= 22:
            red.value(0)
            amber.value(0)
            green.value(1)


