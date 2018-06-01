# Teramon software for heat and light measurements and controls for terrarias

Software pro hlidani teploty a vlhkosti v terariu. Vytvoreno pro Raspberry PI, jako senzory teploty a vlhkosti pouzity moduly DHT11.

* Ovladaci knihovna DHT11: `git clone https://github.com/adafruit/Adafruit_Python_DHT.git`
* Navod na zapojeni cidla: [circuitbasic.com](http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/)
* Navod na I2C LCD: [circuitbasic.com](http://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/)

## Required python modules

* daemon (`apt-get install python-daemon`)

## List of files

* teramon-lcd.py - Shows measured values on LCD thru I2C
* teramon-relay.py - control of light and heat based on time and measured temperatures
* teramon-zabbix.py - Interface between teramon and zabbix monitoring software
* teramon.json - Teramon config
