#!/usr/bin/python

import sys
import teramon
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
tmon = teramon.teramon()

PIN_RELE_SVETLO = 23
PIN_RELE_TEPLO = 24

GPIO.setup(PIN_RELE_SVETLO, GPIO.OUT)
GPIO.setup(PIN_RELE_TEPLO, GPIO.OUT)

dataSklo = tmon.mereni(tmon.PIN_CIDLO_SKLO)
dataLampa = tmon.mereni(tmon.PIN_CIDLO_LAMPA)
dataDzungle = tmon.mereni(tmon.PIN_CIDLO_DZUNGLE)

aktualniHodina = (int)(time.strftime('%H'))
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

if (stavSvetlo):
    GPIO.output(PIN_RELE_SVETLO, GPIO.HIGH)
else:
    GPIO.output(PIN_RELE_SVETLO, GPIO.LOW)

if (stavTeplo):
    GPIO.output(PIN_RELE_TEPLO, GPIO.HIGH)
else:
    GPIO.output(PIN_RELE_TEPLO, GPIO.LOW)
