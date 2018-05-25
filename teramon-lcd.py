#!/usr/bin/python

import sys
import RPi_I2C_driver
import time
import teramon

def vypisLcd(pozice, data, lcd):
    """
    Vypise informace o namerene teplote a vlhkosti na LCD
    """
    lcd.lcd_clear()
    lcd.lcd_display_string(pozice, 1)
    lcd.lcd_display_string('T: {0:0.0f} C RH: {1:0.0f}%'.format(data['temp'], data['hum']), 2)

lcd = RPi_I2C_driver.lcd()

CEKANI = 20

tmon = teramon.teramon()

vypisLcd("SKLO", tmon.mereni(tmon.PIN_CIDLO_SKLO), lcd)
time.sleep(CEKANI)
vypisLcd("LAMPA", tmon.mereni(tmon.PIN_CIDLO_LAMPA), lcd)
time.sleep(CEKANI)
vypisLcd("DZUNGLE", tmon.mereni(tmon.PIN_CIDLO_DZUNGLE), lcd)