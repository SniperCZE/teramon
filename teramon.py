#!/usr/bin/python

import Adafruit_DHT

class teramon:

    PIN_CIDLO_SKLO = 5
    PIN_CIDLO_LAMPA = 6
    PIN_CIDLO_DZUNGLE = 13
    
    def __init__(self):
        pass

    def mereni(self, gpio):
        """
        read_retry(model, gpio pin)
        model: 11, 22
        GPIO pin podle dokumentace Raspberry
        """
        humidity, temperature = Adafruit_DHT.read_retry(11, gpio)
        return { 'hum': humidity, 'temp': temperature }
