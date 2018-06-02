#!/usr/bin/python

import sys
import RPi_I2C_driver
import time
import daemon
import json

class teramonLcd:

    config = {}
    lcd = {}

    def __init__(self, config):
        self.config = config
        self.lcd = RPi_I2C_driver.lcd(config['lcd_address'])

    def showLcd(self, probe, data):
        self.lcd.lcd_clear()
        hour = (int)(time.strftime('%H'))
        minute = (int)(time.strftime('%M'))
        if (hour >= self.config['day_begin']) and (hour <= self.config['day_end']):
            self.lcd.backlight(1)
        else:
            self.lcd.backlight(0)
        self.lcd.lcd_display_string(probe, 1)
        self.lcd.lcd_display_string_pos("{0:0.0f}:{1:0.0f}".format(hour, minute), 1, 11)
        self.lcd.lcd_display_string('T: {0:0.0f}'.format(data['temp']), 2)
        self.lcd.lcd_display_string_pos(chr(223), 2, 5)
        self.lcd.lcd_display_string_pos('C  RH: {0:0.0f}%'.format(data['hum']), 2, 6)

    def controlLcd(self):
        while True:
            cached_measurement = open(config['measurement_save_path']).read()
            for probe, settings in self.config['probes'].iteritems():
                showLcd(probe, cached_measurement[probe], self.lcd)
                time.sleep(self.config['lcd_waiting'])

if __name__ == "__main__":
    json_data = open("./teramon.json").read()
    config = json.loads(json_data)

    tmonLcd = teramonLcd.teramonLcd(config)

    with daemon.DaemonContext():
        tmonLcd.controlLcd()
