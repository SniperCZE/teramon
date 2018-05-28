# teramon - setting pro terarium s felsumami

Software pro hlidani teploty a vlhkosti v terariu. Vytvoreno pro Raspberry PI, jako senzory teploty a vlhkosti pouzity moduly DHT11.

* Ovladaci knihovna DHT11: `git clone https://github.com/adafruit/Adafruit_Python_DHT.git`
* Navod na zapojeni cidla: [circuitbasic.com](http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/)
* Navod na I2C LCD: [circuitbasic.com](http://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/)

## Potrebne moduly v pythonu

* daemon (`apt-get install python-daemon`)

## Seznam souboru

* teramon-lcd.py - zobrazuje namerene hodnoty na LCD display pres I2C. Bezi jako daemon pres systemd
* teramon-rele.py - ovladani osvetleni a topeni na zaklade casu a namerene teploty
* teramon-zabbix.py - integrace teramonu do monitorovaciho systemu zabbix
