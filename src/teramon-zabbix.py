#!/usr/bin/python

import sys
import teramon
import json

json_data = open("./teramon.json").read()
config = json.loads(json_data)

probe_list = ', '.join(config['probes'].keys())

if len(sys.argv) != 3:
    print("Usage: teramon-zabbix.py PROBE MEASUREMENT")
    print("PROBE: {0}".format(probe_list))
    print("MEASUREMENT: hum, temp")
    quit()

tmon = teramon.teramon()

probe = sys.argv[1]
measurement = sys.argv[2]

if probe in config['probes'].keys():
    data = tmon.measurement(config['probes'][probe]['gpio'])
else:
    data = { 'hum' : 0, 'temp' : 0 }

print(data[measurement])
