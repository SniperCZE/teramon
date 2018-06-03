#!/usr/bin/python

import sys
import json
import os

teramon_dir = os.path.dirname(os.path.realpath(__file__))
json_data = open(teramon_dir + "/teramon.json").read()
config = json.loads(json_data)

probe_list = ', '.join(config['probes'].keys())

if len(sys.argv) != 3:
    print("Usage: teramon-zabbix.py PROBE MEASUREMENT")
    print("PROBE: {0}".format(probe_list))
    print("MEASUREMENT: hum, temp")
    quit()

probe = sys.argv[1]
measurement = sys.argv[2]

cached_measurement = open(config['measurement_save_path']).read()

if probe in cached_measurement.keys():
    data = cached_measurement[probe]
else:
    data = { 'hum' : 0, 'temp' : 0 }

print(data[measurement])
