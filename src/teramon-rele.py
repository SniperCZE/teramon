#!/usr/bin/python

import sys
import teramon
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
tmon = teramon.teramon()

json_data = open("./teramon.json").read()
konfigurace = json.loads(json_data)

GPIO.setup(konfigurace['gpio_teplo'], GPIO.OUT)
GPIO.setup(konfigurace['gpio_svetlo'], GPIO.OUT)
data = {}

for cidlo, nastaveni in konfigurace['senzory'].iteritems():
    data[cidlo] = tmon.mereni(nastaveni['gpio'])

aktualniHodina = (int)(time.strftime('%H'))
jeDen = (aktualniHodina >= konfigurace['den_zacatek']) and (aktualniHodina <= konfigurace['den_konec'])

# regulace teplozarivky
stavTeplo = False
zmenitTeplo = True
existujePrimarniCidlo = False

# Schema topeni:
# * cidlo pod lampou hlasi teplotu pod LOW limit pro danou dobu - topime bez ohledu na zbytek cidel
# * alespon jedno cidlo hlasi teplotu pod LOW limit pro danou dobu A ZAROVEN
# * zadne cidlo nehlasi teplotu nad HIGH limit pro danou dobu - topime
# * stav topeni nezmenime, pokud vsechny cidla maji teplotu v rozmezi LOW - HIGH

for cidlo, nastaveni in konfigurace['senzory'].iteritems():
    if nastaveni['primarni'] == True:
        existujePrimarniCidlo = True

if jeDen:

    if existujePrimarniCidlo:
        # nejprve projdeme primarni cidla. Pokud nejake namerilo teplotu <= LOW, topíme.
        for cidlo, nastaveni in konfigurace['senzory'].iteritems():
            if nastaveni['primarni'] == True:
                if data[cidlo]['temp'] <= nastaveni['limity_teploty']['den']['low']:
                    stavTeplo = True
                    zmenTeplo = True
    else :
        for cidlo, nastaveni in konfigurace['senzory'].iteritems():
            if data[cidlo]['temp'] <= nastaveni['limity_teploty']['den']['low']:
                stavTeplo = True

        for cidlo, nastaveni in konfigurace['senzory'].iteritems():
            if data[cidlo]['temp'] >= nastaveni['limity_teploty']['den']['high']:
                stavTeplo = False

        zatimTrue = True
        for cidlo, nastaveni in konfigurace['senzory'].iteritems():
            if (data[cidlo]['temp'] <= nastaveni['limit_teploty']['den']['high']) and (data[cidlo]['temp'] >= nastaveni['limit_teploty']['den']['low']) and zatimTrue:
                zatimTrue = True
            else:
                zatimTrue = False

        if zatimTrue:
            zmenitTeplo = False
else:

    if existujePrimarniCidlo:
        # nejprve projdeme primarni cidla. Pokud nejake namerilo teplotu <= LOW, topíme.
        for cidlo, nastaveni in konfigurace['senzory'].iteritems():
            if nastaveni['primarni'] == True:
                if data[cidlo]['temp'] <= nastaveni['limity_teploty']['noc']['low']:
                    stavTeplo = True
                    zmenTeplo = True
    else :
        for cidlo, nastaveni in konfigurace['senzory'].iteritems():
            if data[cidlo]['temp'] <= nastaveni['limity_teploty']['noc']['low']:
                stavTeplo = True

        for cidlo, nastaveni in konfigurace['senzory'].iteritems():
            if data[cidlo]['temp'] >= nastaveni['limity_teploty']['noc']['high']:
                stavTeplo = False

        zatimTrue = True
        for cidlo, nastaveni in konfigurace['senzory'].iteritems():
            if (data[cidlo]['temp'] <= nastaveni['limit_teploty']['noc']['high']) and (data[cidlo]['temp'] >= nastaveni['limit_teploty']['noc']['low']) and zatimTrue:
                zatimTrue = True
            else:
                zatimTrue = False

        if zatimTrue:
            zmenitTeplo = False
    

# regulace svetla
stavSvetlo = jeDen

if (stavSvetlo):
    GPIO.output(konfigurace['gpio_svetlo'], GPIO.HIGH)
else:
    GPIO.output(konfigurace['gpio_svetlo'], GPIO.LOW)

if zmenitTeplo:
    if (stavTeplo):
        GPIO.output(konfigurace['gpio_teplo'], GPIO.HIGH)
    else:
        GPIO.output(konfigurace['gpio_teplo'], GPIO.LOW)
