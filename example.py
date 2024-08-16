from machine import Pin, I2C
from time import sleep
import ads1115_driver

i2c = I2C(1, scl=Pin(15), sda=Pin(14))
adc = ads1115_driver.ADS1115(i2c)

while True:
    print(adc.read_voltage(3), "V")
    sleep(1)