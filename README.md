# teramon - setting pro terarium s felsumami

Software pro hlidani teploty a vlhkosti v terariu. Vytvoreno pro Raspberry PI, jako senzory teploty a vlhkosti pouzity moduly DHT11.

* Ovladaci knihovna DHT11: `git clone https://github.com/adafruit/Adafruit_Python_DHT.git`
* Navod na zapojeni cidla: http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/
* Navod na I2C LCD: http://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/

## Seznam souboru

* teramon-lcd.py - zobrazuje namerene hodnoty na LCD display pres I2C
* teramon-rele.py - ovladani osvetleni a topeni na zaklade casu a namerene teploty
* teramon-zabbix.py - integrace teramonu do monitorovaciho systemu zabbix

## Použité piny raspberry

```
                   01 -+ +- 02 +5V čidla + relé
       SDA display 03 -+ +- 04 +5V display
       SCL display 05 -+ +- 06 GND display
                   07 -+ +- 08
                   09 -+ +- 10
                   11 -+ +- 12
                   13 -+ +- 14 GND čidla
                   15 -+ +- 16 GPIO Relé světlo
                   17 -+ +- 18 GPIO Relé teplo
                   19 -+ +- 20 GND relé
                   21 -+ +- 22
                   23 -+ +- 24
                   25 -+ +- 26
                   27 -+ +- 28
   DATA čidlo sklo 29 -+ +- 30
  DATA čidlo lampa 31 -+ +- 32
DATA čidlo dzungle 33 -+ +- 34
                   35 -+ +- 36
                   37 -+ +- 38
                   39 -+ +- 40
```

## Poznámky

* V souboru `RPi_I2C_driver.py` je potřeba nastavit I2C adresu vašeho LCD (zjistíte přes utilitku i2cdetect), k tomu slouží řádek 54. V mém případě je LCD na adrese 0x38.
* v zabbixu je potreba zvetsit timeout na 30s, protoze cteni cidla se za 3s defaultniho timeoutu nestihne
* zabbix potrebuje pristup k GPIO - je potreba uzivatele, pod kterym zabbix agent bezi, pridat do skupiny gpio