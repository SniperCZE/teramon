#!/usr/bin/python

import sys
import teramon
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
tmon = teramon.teramon()

json_data = open("./teramon.json").read()
config = json.loads(json_data)

GPIO.setup(config['gpio_heat'], GPIO.OUT)
GPIO.setup(config['gpio_light'], GPIO.OUT)
data = {}

for probe, settings in config['probes'].iteritems():
    data[probe] = tmon.measurement(settings['gpio'])

actualHour = (int)(time.strftime('%H'))
isDay = (actualHour >= config['day_begin']) and (actualHour <= config['day_end'])

heatOn = False
heatChange = True
primaryProbeDefined = False

for probe, settings in config['probes'].iteritems():
    if settings['primary'] == True:
        primaryProbeDefined = True

if isDay:

    if primaryProbeDefined:
        for probe, settings in config['probes'].iteritems():
            if settings['primary'] == True:
                if data[probe]['temp'] <= settings['temp_limits']['day']['low']:
                    heatOn = True
                    heatChange = True
    else :
        for probe, settings in config['probes'].iteritems():
            if data[probe]['temp'] <= settings['temp_limits']['day']['low']:
                heatOn = True

        for probe, settings in config['probes'].iteritems():
            if data[probe]['temp'] >= settings['temp_limits']['day']['high']:
                heatOn = False

        stillTrue = True
        for probe, settings in config['probes'].iteritems():
            if (data[probe]['temp'] <= settings['temp_limits']['day']['high']) and (data[probe]['temp'] >= settings['temp_limits']['day']['low']) and stillTrue:
                stillTrue = True
            else:
                stillFalse = False

        if stillTrue:
            heatChange = False
else:

    if primaryProbeDefined:
        for probe, settings in config['probes'].iteritems():
            if settings['primary'] == True:
                if data[probe]['temp'] <= settings['temp_limits']['night']['low']:
                    heatOn = True
                    heatChange = True
    else :
        for probe, settings in config['probes'].iteritems():
            if data[probe]['temp'] <= settings['temp_limits']['night']['low']:
                heatOn = True

        for probe, settings in config['probes'].iteritems():
            if data[probe]['temp'] >= settins['temp_limits']['night']['high']:
                heatOn = False

        stillTrue = True
        for probe, settings in config['probes'].iteritems():
            if (data[probe]['temp'] <= settings['temp_limits']['noght']['high']) and (data[probe]['temp'] >= settings['temp_limits']['night']['low']) and zatimTrue:
                stillTrue = True
            else:
                stillTrue = False

        if stillTrue:
            heatChange = False
    

lightOn = isDay

if (lightOn):
    GPIO.output(config['gpio_light'], GPIO.HIGH)
else:
    GPIO.output(config['gpio_light'], GPIO.LOW)

if heatChange:
    if (heatOn):
        GPIO.output(config['gpio_heat'], GPIO.HIGH)
    else:
        GPIO.output(config['gpio_heat'], GPIO.LOW)
