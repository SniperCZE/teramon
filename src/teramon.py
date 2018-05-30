#!/usr/bin/python

import Adafruit_DHT
import json

class teramon:

    dht_model = 11

    def __init__(self):
        json_data = open("./teramon.json").read()
        konfigurace = json.loads(json_data)
        self.dht_model = konfigurace['dht_model']

    def mereni(self, gpio):
        humidity, temperature = Adafruit_DHT.read_retry(self.dht_model, gpio)
        return { 'hum': humidity, 'temp': temperature }
