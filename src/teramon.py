#!/usr/bin/python

import Adafruit_DHT
import json
import time
import daemon
import os

class teramon:

    dht_model = 11
    sleep = 30
    save_path = "/tmp/teramon.json"
    config = {}

    def __init__(self):
        teramon_dir = os.path.dirname(os.path.realpath(__file__))
        json_data = open(teramon_dir + "/teramon.json").read()
        self.config = json.loads(json_data)
        self.dht_model = self.config['dht_model']
        self.sleep = self.config['daemon_sleep']
        self.save_path = self.config['measurement_save_path']

    def measurement(self, gpio):
        humidity, temperature = Adafruit_DHT.read_retry(self.dht_model, gpio)
        return { 'hum': humidity, 'temp': temperature }

    def runTeramonDaemon(self):
        data = {}
        while True:
            for probe in self.config['probes'].keys():
                data[str(probe)] = self.measurement(self.config['probes'][probe]['gpio'])
            with open(self.save_path, 'w') as outfile:
                json.dump(data, outfile)
            time.sleep(self.sleep)

if __name__ == "__main__":
    tmon = teramon()
    with daemon.DaemonContext():
        tmon.runTeramonDaemon()