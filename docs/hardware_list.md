# List of used hardware

* Raspberry PI Zero W - [CZC.cz, 499Kč](https://www.czc.cz/raspberry-pi-zero-wh/234608/produkt)
* Measurement probe DHT11 - [dx.com, cca. 86Kč](http://www.dx.com/p/hengjiaan-dht11-digital-temperature-humidity-sensor-modules-2-pcs-463981#.WwXCABwzU5k)
* LCD display with I2C support - [dx.com, cca. 94Kč](http://www.dx.com/p/i2c-iic-2-6-lcd-1602-yellow-green-display-module-for-arduino-raspberry-pi-avr-arm-379324)

## Použité piny raspberry

```
                   01 -+ +- 02 +5V probes + relays
       SDA display 03 -+ +- 04 +5V display
       SCL display 05 -+ +- 06 GND display
                   07 -+ +- 08
                   09 -+ +- 10
                   11 -+ +- 12
                   13 -+ +- 14 GND probes
                   15 -+ +- 16 GPIO light relay
                   17 -+ +- 18 GPIO heat relay
                   19 -+ +- 20 GND relays
                   21 -+ +- 22
                   23 -+ +- 24
                   25 -+ +- 26
                   27 -+ +- 28
   DATA probe SKLO 29 -+ +- 30
  DATA probe LAMPA 31 -+ +- 32
DATA probe DZUNGLE 33 -+ +- 34
                   35 -+ +- 36
                   37 -+ +- 38
                   39 -+ +- 40
```