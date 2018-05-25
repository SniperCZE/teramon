#!/usr/bin/python

import sys
import teramon
import time
from gpiozero import OutputDevice

tmon = teramon.teramon()

PIN_RELE_SVETLO = 23
PIN_RELE_TEPLO = 24

dataSklo = tmon.mereni(tmon.PIN_CIDLO_SKLO)
dataLampa = tmon.mereni(tmon.PIN_CIDLO_LAMPA)
dataDzungle = tmon.mereni(tmon.PIN_CIDLO_DZUNGLE)

aktualniHodina = time.strftime('%H')
jeDen = (aktualniHodina >= 8) and (aktualniHodina <= 21)

# regulace teplozarivky
stavTeplo = False
if (dataLampa['temp'] < 30) and jeDen:
    stavTeplo = True
if ((dataSklo['temp'] < 21) or (dataDzungle['temp'] < 21)) and jeDen:
    stavTeplo = True
if ((dataSklo['temp'] < 18) or (dataLampa['temp'] < 18) or (dataDzungle['temp'] < 18)) and (jeDen == False):
    stavTeplo = True

# regulace svetla
stavSvetlo = jeDen

releSvetlo = OutputDevice(PIN_RELE_SVETLO)
releTeplo = OutputDevice(PIN_RELE_TEPLO)

if (stavSvetlo):
    releSvetlo.on()
else:
    releSvetlo.off()

if (stavTeplo):
    releTeplo.on()
else:
    releTeplo.off()
