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
    hodina = (int)(time.strftime('%H'))
    minuta = (int)(time.strftime('%M'))
    if (hodina >= 8) and (hodina <= 22):
        lcd.backlight(1)
    else:
        lcd.backlight(0)
    lcd.lcd_display_string(pozice, 1)
    lcd.lcd_display_string_pos("{0:0.0f}:{1:0.0f}".format(hodina, minuta), 1, 11)
    lcd.lcd_display_string('T: {0:0.0f}', 2)
    lcd.lcd_display_string_pos(chr(2230), 2, 5)
    lcd.lcd_display_string_pos('C RH: {1:0.0f}%'.format(data['temp'], data['hum']), 2, 6)

lcd = RPi_I2C_driver.lcd()

CEKANI = 30

tmon = teramon.teramon()

vypisLcd("SKLO", tmon.mereni(tmon.PIN_CIDLO_SKLO), lcd)
time.sleep(CEKANI)
vypisLcd("LAMPA", tmon.mereni(tmon.PIN_CIDLO_LAMPA), lcd)
time.sleep(CEKANI)
vypisLcd("DZUNGLE", tmon.mereni(tmon.PIN_CIDLO_DZUNGLE), lcd)