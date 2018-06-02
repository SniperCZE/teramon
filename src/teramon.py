#!/usr/bin/python

import Adafruit_DHT
import json
import time
import daemon

class teramon:

    dht_model = 11
    sleep = 30
    save_path = "/tmp/teramon.json"
    config = {}

    def __init__(self):
        json_data = open("./teramon.json").read()
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
            for probe, settings in self.config['probes']
                data[probe] = self.measurement(settings['gpio'])
            with open(self.save_path, 'w') as outfile:
                json.dump(data, outfile)
            time.sleep(self.sleep)

if __name__ == "__main__":
    tmon = teramon.teramon()
    with daemon.DaemonContext():
        tmon.runTeramonDaemon()