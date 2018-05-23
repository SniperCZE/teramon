# teramon

Software pro hlidani teploty a vlhkosti v terariu. Vytvoreno pro Raspberry PI, jako senzory teploty a vlhkosti pouzity moduly DHT11.

* Ovladaci knihovna DHT11: `git clone https://github.com/adafruit/Adafruit_Python_DHT.git`
* Navod na zapojeni cidla: http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/
* Navod na I2C LCD: http://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/

Poznámky:
* V souboru `RPi_I2C_driver.py` je potřeba nastavit I2C adresu vašeho LCD (zjistíte přes utilitku i2cdetect), k tomu slouží řádek 54. V mém případě je LCD na adrese 0x38
