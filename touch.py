import machine
import bu
import adafruit_mpr121
import utime
import keyboard
from machine import I2C

# Initialize I2C bus
i2c = I2C(0, sda=machine.Pin(16), scl=machine.Pin(17))

# Initialize MPR121 sensors
mpr121_1 = adafruit_mpr121.MPR121(i2c, address=0x5A)
mpr121_2 = adafruit_mpr121.MPR121(i2c, address=0x5B)
mpr121_3 = adafruit_mpr121.MPR121(i2c, address=0x5C)

mpr121_sensors = [mpr121_1, mpr121_2, mpr121_3]

# Main loop
while True:
    # Iterate over each MPR121 sensor
    for index, mpr121_sensor in enumerate(mpr121_sensors):
        # Check each key on the sensor
        for key_num in range(12):
            # Check if the key is touched
            if mpr121_sensor.is_touched(12):
                key_index = index * 12 + key_num
                print(f"Mpr121-{index + 1}, Key {key_num} touched")

                # Perform action based on the touched key
                # Example: Send a corresponding keyboard input
                keyboard.press_and_release(f"Mpr121-{index + 1}_Key_{key_num}")

    # Add a small delay to avoid excessive polling
    time.sleep(0.1)
