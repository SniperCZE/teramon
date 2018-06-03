#!/usr/bin/python

import sys
import RPi_I2C_driver
import time
import json
import os

class teramonLcd:

    config = {}
    lcd = {}

    def __init__(self):
        teramon_dir = os.path.dirname(os.path.realpath(__file__))
        json_data = open(teramon_dir + "/teramon.json").read()
        self.config = json.loads(json_data)
        lcd_address = int(self.config['lcd_address'], 16)
        self.lcd = RPi_I2C_driver.lcd(lcd_address)

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
            cached_measurement = open(self.config['measurement_save_path']).read()
            cached_measurement_data = json.loads(cached_measurement)
            for probe in self.config['probes'].keys():
                self.showLcd(str(probe), cached_measurement_data[probe])
                time.sleep(self.config['lcd_waiting'])

if __name__ == "__main__":
    tmonLcd = teramonLcd()
    tmonLcd.controlLcd()
