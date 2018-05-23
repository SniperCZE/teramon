#!/usr/bin/python3

import sys
import Adafruit_DHT

while True:

    # read_retry(model, gpio pin)
    # model: 11, 22
    # GPIO pin podle dokumentace Raspberry
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
