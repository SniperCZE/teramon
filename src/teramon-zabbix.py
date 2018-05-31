#!/usr/bin/python

import sys
import teramon
import json

json_data = open("./teramon.json").read()
konfigurace = json.loads(json_data)

list_cidel = ', '.join(konfigurace['senzory'].keys())

if len(sys.argv) != 3:
    print("Pouziti: teramon-zabbix.py POZICE VELICINA")
    print("POZICE: {0}".format(list_cidel))
    print("VELICINA: hum, temp")
    quit()

tmon = teramon.teramon()

pozice = sys.argv[1]
velicina = sys.argv[2]

if pozice in konfigurace['senzory'].keys():
    data = tmon.mereni(konfigurace['senzory'][pozice]['gpio'])
else:
    data = { 'hum' : 0, 'temp' : 0 }

print(data[velicina])
