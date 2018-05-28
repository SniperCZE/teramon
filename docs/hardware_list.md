# Seznam pouziteho hardware

* Raspberry PI Zero W - [CZC.cz, 499Kč](https://www.czc.cz/raspberry-pi-zero-wh/234608/produkt)
* Modul měření teploty a vlhkosti DHT11 - [dx.com, cca. 86Kč](http://www.dx.com/p/hengjiaan-dht11-digital-temperature-humidity-sensor-modules-2-pcs-463981#.WwXCABwzU5k)
* LCD display s podporou I2C - [dx.com, cca. 94Kč](http://www.dx.com/p/i2c-iic-2-6-lcd-1602-yellow-green-display-module-for-arduino-raspberry-pi-avr-arm-379324)

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