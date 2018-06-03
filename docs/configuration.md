# Teramon configuration

Teramon uses `teramon.json` file for storing all configuration values.

## Example of teramon.json

```json
{
    "lcd_address" : 38,
    "lcd_waiting" : 30,
    "probes" : {
        "SKLO" : { 
            "gpio" : 5,
            "primary" : false,
            "temp_limits" : {
                "day" : {
                    "low" : 22,
                    "high" : 25
                },
                "night" : {
                    "low" : 18,
                    "high" : 22
                }
            }
        },
        "DZUNGLE" : { 
            "gpio" : 13,
            "primary" : false,
            "temp_limits" : {
                "day" : {
                    "low" : 22,
                    "high" : 25
                },
                "night" : {
                    "low" : 18,
                    "high" : 22
                }
            }
        },
        "LAMPA" : { 
            "gpio" : 6,
            "primary" : true,
            "temp_limits" : {
                "day" : {
                    "low" : 33,
                    "high" : 35
                },
                "night" : {
                    "low" : 18,
                    "high" : 22
                }
            }
        }
    },
    "day_begin" : 8,
    "day_end" : 22,
    "gpio_light" : 23,
    "gpio_heat" : 24,
    "dht_model" : 11,
    "daemon_sleep" : 60,
    "measurement_save_path" : "/tmp/teramon.json"
}
```

### Field description

* *lcd_address* - I2C address of LCD. Can be checked via `i2cdetect` utility
* *lcd_waiting* - timeframe in seconds, how long is info from one probe dislayed
* *probes* - object with definition of existing probes. It contains named objects of each probe. Probe name is used for LCD description and in zabbix checks.
  * *gpio* - GPIO port where probe is connected
  * *primary* - boolean flag probe is primary. Primary probes directly controls heat on/off indepented to non-primary probes. Teramon turns heat on if any of primary probes reports temperature lower or equal of low value for day or night.
    * *temp_limits* - Object with temperature limits for probe
      * *day* - temperature limits for day
        * *low* - temperature when heat turns on
        * *high* - temperature when heat turns off
      * *night* - temperature limits for nights. Same parameters as in day
* *day_begin* - first hour of the day
* *day_end* - last hour of the day
* *gpio_light* - GPIO port where control of light relay is connected
* *gpio_heat* - GPIO port where control of heat relay is connected
* *dht_model* - model of DHT probe for measurement of temperature and humidity. Allowed values are `11` and `22`
* *daemon_sleep* - interval between measurement of humidity and temperature
* *measurement_save_path* - path for saving measurement results