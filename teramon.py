#!/usr/bin/python

import sys
import Adafruit_DHT
import RPi_I2C_driver
from time import *

lcd = RPi_I2C_driver.lcd()

while True:

    # read_retry(model, gpio pin)
    # model: 11, 22
    # GPIO pin podle dokumentace Raspberry
    humidity, temperature = Adafruit_DHT.read_retry(11, 18)
    lcd.lcd_clear()
    lcd.lcd_display_string('Temp: {0:0.1f} C'.format(temperature), 1)
    lcd.lcd_display_string('Humidity: {0:0.1f} %'.format(humidity), 2)

    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
