#!/usr/bin/python

import sys
import time
import RPi.GPIO as GPIO
import os
import json

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

teramon_dir = os.path.dirname(os.path.realpath(__file__))
json_data = open(teramon_dir + "/teramon.json").read()
config = json.loads(json_data)

data = open(config['measurement_save_path']).read()

GPIO.setup(config['gpio_heat'], GPIO.OUT)
GPIO.setup(config['gpio_light'], GPIO.OUT)

actualHour = (int)(time.strftime('%H'))
isDay = (actualHour >= config['day_begin']) and (actualHour <= config['day_end'])

heatOn = False
heatChange = True
primaryProbeDefined = False

for probe in config['probes'].keys():
    if config['probes'][probe]['primary'] == True:
        primaryProbeDefined = True

if isDay:

    if primaryProbeDefined:
        for probe in config['probes'].keys():
            if config['probes'][probe]['primary'] == True:
                if data[probe]['temp'] <= config['probes'][probe]['temp_limits']['day']['low']:
                    heatOn = True
                    heatChange = True
    else :
        for probe in config['probes'].keys():
            if data[probe]['temp'] <= config['probes'][probe]['temp_limits']['day']['low']:
                heatOn = True

        for probe in config['probes'].keys():
            if data[probe]['temp'] >= config['probes'][probe]['temp_limits']['day']['high']:
                heatOn = False

        stillTrue = True
        for probe in config['probes'].keys():
            if (data[probe]['temp'] <= config['probes'][probe]['temp_limits']['day']['high']) and (data[probe]['temp'] >= config['probes'][probe]['temp_limits']['day']['low']) and stillTrue:
                stillTrue = True
            else:
                stillFalse = False

        if stillTrue:
            heatChange = False
else:

    if primaryProbeDefined:
        for probe in config['probes'].keys():
            if config['probes'][probe]['primary'] == True:
                if data[probe]['temp'] <= config['probes'][probe]['temp_limits']['night']['low']:
                    heatOn = True
                    heatChange = True
    else :
        for probe in config['probes'].keys():
            if data[probe]['temp'] <= config['probes'][probe]['temp_limits']['night']['low']:
                heatOn = True

        for probe in config['probes'].keys():
            if data[probe]['temp'] >= config['probes'][probe]['temp_limits']['night']['high']:
                heatOn = False

        stillTrue = True
        for probe in config['probes'].keys():
            if (data[probe]['temp'] <= config['probes'][probe]['temp_limits']['noght']['high']) and (data[probe]['temp'] >= config['probes'][probe]['temp_limits']['night']['low']) and zatimTrue:
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
