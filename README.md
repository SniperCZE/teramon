# Teramon software for heat and light measurements and controls for terrarias

Automatization of temperature and light control for terrarium. Using Raspberry PI and DHT11 probes for temperature and humidity.

* DHT probe control library: `git clone https://github.com/adafruit/Adafruit_Python_DHT.git`
* How to connect probe: [circuitbasic.com](http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/)
* How to connect I2C LCD: [circuitbasic.com](http://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/)

## Required python modules

* daemon (`apt-get install python-daemon`)

## List of files

* teramon-lcd.py - Shows measured values on LCD thru I2C
* teramon-relay.py - control of light and heat based on time and measured temperatures
* teramon-zabbix.py - Interface between teramon and zabbix monitoring software
* teramon.json - Teramon config
