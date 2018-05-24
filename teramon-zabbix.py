#!/usr/bin/python

import sys
import teramon

if len(sys.argv) != 2:
    print("Pouziti: teramon-zabbix.py POZICE VELICINA")
    print("POZICE: SKLO, LAMPA, DZUNGLE")
    print("VELICINA: hum, temp")
    quit()

tmon = teramon.teramon()

pozice = sys.argv[1]

if pozice == "SKLO":
    data = tmon.mereni(teramon.PIN_CIDLO_SKLO)
else if pozice == "LAMPA":
    data = tmon.mereni(teramon.PIN_CIDLO_LAMPA)
else if pozice == "DZUNGLE":
    data = tmon.mereni(teramon.PIN_CIDLO_DZUNGLE)
else:
    data = { 'hum' : 0, 'temp' : 0 }

print(data[sys.argv[2]])
