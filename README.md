# teramon - setting pro terarium s felsumami

Software pro hlidani teploty a vlhkosti v terariu. Vytvoreno pro Raspberry PI, jako senzory teploty a vlhkosti pouzity moduly DHT11.

* Ovladaci knihovna DHT11: `git clone https://github.com/adafruit/Adafruit_Python_DHT.git`
* Navod na zapojeni cidla: http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/
* Navod na I2C LCD: http://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/

## Použité piny raspberry

```
                  01 -+ +- 02 +5V čidla + relé
      SDA display 03 -+ +- 04 +5V display
      SCL display 05 -+ +- 06 GND display
                  07 -+ +- 08
                  09 -+ +- 10
                  11 -+ +- 12
                  13 -+ +- 14
                  15 -+ +- 16 GPIO Relé světlo
                  17 -+ +- 18 GPIO Relé teplo
                  19 -+ +- 20 GND relé
                  21 -+ +- 22
                  23 -+ +- 24
                  25 -+ +- 26
                  27 -+ +- 28
                  29 -+ +- 30
  DATA čidlo sklo 31 -+ +- 32
 DATA čidlo lampa 33 -+ +- 34
DATA čidlo prales 35 -+ +- 36
                  37 -+ +- 38
                  39 -+ +- 40
```

## Poznámky

* V souboru `RPi_I2C_driver.py` je potřeba nastavit I2C adresu vašeho LCD (zjistíte přes utilitku i2cdetect), k tomu slouží řádek 54. V mém případě je LCD na adrese 0x38
