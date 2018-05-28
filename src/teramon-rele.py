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

LIMIT_SKLO_LOW_DEN = 22
LIMIT_SKLO_HIGH_DEN = 25
LIMIT_DZUNGLE_LOW_DEN = 22
LIMIT_DZUNGLE_HIGH_DEN = 25
LIMIT_LAMPA_LOW_DEN = 33
LIMIT_LAMPA_HIGH_DEN = 37

LIMIT_SKLO_LOW_NOC = 18
LIMIT_SKLO_HIGH_NOC = 22
LIMIT_DZUNGLE_LOW_NOC = 18
LIMIT_DZUNGLE_HIGH_NOC = 22
LIMIT_LAMPA_LOW_NOC = 18
LIMIT_LAMPA_HIGH_NOC = 22


GPIO.setup(PIN_RELE_SVETLO, GPIO.OUT)
GPIO.setup(PIN_RELE_TEPLO, GPIO.OUT)

dataSklo = tmon.mereni(tmon.PIN_CIDLO_SKLO)
dataLampa = tmon.mereni(tmon.PIN_CIDLO_LAMPA)
dataDzungle = tmon.mereni(tmon.PIN_CIDLO_DZUNGLE)

aktualniHodina = (int)(time.strftime('%H'))
jeDen = (aktualniHodina >= 8) and (aktualniHodina <= 21)

# regulace teplozarivky
stavTeplo = False
zmenitTeplo = True

# Schema topeni:
# * cidlo pod lampou hlasi teplotu pod LOW limit pro danou dobu - topime bez ohledu na zbytek cidel
# * alespon jedno cidlo hlasi teplotu pod LOW limit pro danou dobu A ZAROVEN
# * zadne cidlo nehlasi teplotu nad HIGH limit pro danou dobu - topime
# * stav topeni nezmenime, pokud vsechny cidla maji teplotu v rozmezi LOW - HIGH

if jeDen:
    if dataLampa['temp'] < LIMIT_LAMPA_LOW_DEN:
        stavTeplo = True
        zmenTeplo = True
    else :
        if (dataSklo['temp'] < LIMIT_SKLO_LOW_DEN) or () or (dataDzungle['temp'] < LIMIT_DZUNGLE_LOW_DEN):
            stavTeplo = True

        if (dataSklo['temp'] > LIMIT_SKLO_HIGH_DEN) or (dataLampa['temp'] > LIMIT_LAMPA_HIGH_DEN) or (dataDzungle['temp'] > LIMIT_DZUNGLE_HIGH_DEN):
            stavTeplo = False

        if ((dataSklo['temp'] <= LIMIT_SKLO_HIGH_DEN) and (dataSklo['temp'] >= LIMIT_SKLO_LOW_DEN)) and ((dataLampa['temp'] <= LIMIT_LAMPA_HIGH_DEN) and (dataLampa['temp'] >= LIMIT_LAMPA_HIGH_DEN)) and ((dataDzungle['temp'] <= LIMIT_DZUNGLE_HIGH_DEN) and (dataDzungle['temp'] >= LIMIT_DZUNGLE_HIGH_DEN)):
            zmenitTeplo = False
else:
    if dataLampa['temp'] < LIMIT_LAMPA_LOW_NOC:
        stavTeplo = True
        zmenTeplo = True
    else:
        if (dataSklo['temp'] < LIMIT_SKLO_LOW_NOC) or () or (dataDzungle['temp'] < LIMIT_DZUNGLE_LOW_NOC):
            stavTeplo = True

        if (dataSklo['temp'] > LIMIT_SKLO_HIGH_NOC) or (dataLampa['temp'] > LIMIT_LAMPA_HIGH_NOC) or (dataDzungle['temp'] > LIMIT_DZUNGLE_HIGH_NOC):
            stavTeplo = False

        if ((dataSklo['temp'] <= LIMIT_SKLO_HIGH_NOC) and (dataSklo['temp'] >= LIMIT_SKLO_LOW_NOC)) and ((dataLampa['temp'] <= LIMIT_LAMPA_HIGH_NOC) and (dataLampa['temp'] >= LIMIT_LAMPA_HIGH_NOC)) and ((dataDzungle['temp'] <= LIMIT_DZUNGLE_HIGH_NOC) and (dataDzungle['temp'] >= LIMIT_DZUNGLE_HIGH_NOC)):
            zmenitTeplo = False
    

# regulace svetla
stavSvetlo = jeDen

if (stavSvetlo):
    GPIO.output(PIN_RELE_SVETLO, GPIO.HIGH)
else:
    GPIO.output(PIN_RELE_SVETLO, GPIO.LOW)

if zmenitTeplo:
    if (stavTeplo):
        GPIO.output(PIN_RELE_TEPLO, GPIO.HIGH)
    else:
        GPIO.output(PIN_RELE_TEPLO, GPIO.LOW)