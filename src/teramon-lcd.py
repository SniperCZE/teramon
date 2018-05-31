#!/usr/bin/python

import sys
import RPi_I2C_driver
import time
import teramon
import daemon
import json

class teramonLcd:

    konfigurace = {}
    lcd = {}
    tmon = {}

    def __init__(self, konfigurace):
        self.konfigurace = konfigurace
        self.lcd = RPi_I2C_driver.lcd(konfigurace['lcd_adresa'])
        self.tmon = teramon.teramon()

    def vypisLcd(self, pozice, data):
        """
        Vypise informace o namerene teplote a vlhkosti na LCD
        """
        self.lcd.lcd_clear()
        hodina = (int)(time.strftime('%H'))
        minuta = (int)(time.strftime('%M'))
        if (hodina >= self.konfigurace['den_zacatek']) and (hodina <= self.konfigurace['den_konec']):
            self.lcd.backlight(1)
        else:
            self.lcd.backlight(0)
        self.lcd.lcd_display_string(pozice, 1)
        self.lcd.lcd_display_string_pos("{0:0.0f}:{1:0.0f}".format(hodina, minuta), 1, 11)
        self.lcd.lcd_display_string('T: {0:0.0f}'.format(data['temp']), 2)
        self.lcd.lcd_display_string_pos(chr(223), 2, 5)
        self.lcd.lcd_display_string_pos('C  RH: {0:0.0f}%'.format(data['hum']), 2, 6)

    def ovladaniLcd(self):
        while True:
            for cidlo, nastaveni in self.konfigurace['senzory'].iteritems():
                vypisLcd(cidlo, tmon.mereni(nastaveni['gpio']), self.lcd)
                time.sleep(self.konfigurace['lcd_cekani'])

json_data = open("./teramon.json").read()
konfigurace = json.loads(json_data)

tmonLcd = teramonLcd.teramonLcd(konfigurace)

with daemon.DaemonContext():
    tmonLcd.ovladaniLcd()
