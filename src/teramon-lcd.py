#!/usr/bin/python

import sys
import RPi_I2C_driver
import time
import teramon
import daemon

def vypisLcd(pozice, data, lcd):
    """
    Vypise informace o namerene teplote a vlhkosti na LCD
    """
    lcd.lcd_clear()
    hodina = (int)(time.strftime('%H'))
    minuta = (int)(time.strftime('%M'))
    if (hodina >= 8) and (hodina <= 22):
        lcd.backlight(1)
    else:
        lcd.backlight(0)
    lcd.lcd_display_string(pozice, 1)
    lcd.lcd_display_string_pos("{0:0.0f}:{1:0.0f}".format(hodina, minuta), 1, 11)
    lcd.lcd_display_string('T: {0:0.0f}'.format(data['temp']), 2)
    lcd.lcd_display_string_pos(chr(223), 2, 5)
    lcd.lcd_display_string_pos('C  RH: {0:0.0f}%'.format(data['hum']), 2, 6)

def ovladaniLcd(tmon, lcd, cekani=30):
    vypisLcd("SKLO", tmon.mereni(tmon.PIN_CIDLO_SKLO), lcd)
    time.sleep(cekani)
    vypisLcd("LAMPA", tmon.mereni(tmon.PIN_CIDLO_LAMPA), lcd)
    time.sleep(cekani)
    vypisLcd("DZUNGLE", tmon.mereni(tmon.PIN_CIDLO_DZUNGLE), lcd)
    time.sleep(cekani)

CEKANI = 30

lcd = RPi_I2C_driver.lcd()
tmon = teramon.teramon()

with daemon.DaemonContext():
    ovladaniLcd(tmon, lcd, CEKANI)
