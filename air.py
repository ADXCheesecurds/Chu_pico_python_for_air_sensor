import machine
import utime
from machine import I2C
from VL53L0X import VL53L0X
import keyboard

# Configure I2C communication
i2c = I2C(0, sda=machine.Pin(16), scl=machine.Pin(17))
sensor = VL53L0X(i2c)

sensor.measurement_timing_budget = 200000
sensor.range_mm = (50, 300)

while True:
    # Perform a measurement
    distance = sensor.read()

    # Check if the distance is within the specified range
    if 50 <= distance <= 300:
        # Simulate pressing the space bar using the keyboard library
        keyboard.press('space')
    else:
        keyboard.release('space')

    # Delay before the next measurement
    utime.sleep_ms(10)
