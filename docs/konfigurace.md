# Konfigurace Teramonu

Teramon se konfiguruje přes soubor `teramon.json`. V něm je možno nastavit adresy jednotlivých zařízení, čidla, teploty pro spínání a rozsah hodin považovaných za den.

## Ukázkový teramon.json

```json
{
    "lcd_adresa" : 38,
    "lcd_cekani" : 30,
    "senzory" : {
        "SKLO" : { 
            "gpio" : 5,
            "limity_teploty" : {
                "den" : {
                    "low" : 22,
                    "high" : 25
                },
                "noc" : {
                    "low" : 18,
                    "high" : 22
                },
                "primarni" : false
            }
        },
        "DZUNGLE" : { 
            "gpio" : 13,
            "limity_teploty" : {
                "den" : {
                    "low" : 22,
                    "high" : 25
                },
                "noc" : {
                    "low" : 18,
                    "high" : 22
                },
                "primarni" : false
            }
        },
        "LAMPA" : { 
            "gpio" : 6,
            "limity_teploty" : {
                "den" : {
                    "low" : 33,
                    "high" : 35
                },
                "noc" : {
                    "low" : 18,
                    "high" : 22
                },
                "primarni" : true
            }
        }
    },
    "den_zacatek" : 8,
    "den_konec" : 22,
    "gpio_svetlo" : 23,
    "gpio_teplo" : 24,
    "dht_model" : 11
}
```

### Popis polí v konfiguraci

* *lcd_adresa* - I2C adresa LCD, zjistitelná přes utilitku `i2cdetect`
* *lcd_cekani* - doba ve vteřinách, po jakou je zobrazeno na LCD konkrétní čidlo
* *senzory* - objekt obsahující definici jednotlivých čidel. Obsahuje pojmenované objekty jednotlivých čidel. Jméno čidla se používá pro zobrazení na LCD a v dotazech zabbixu
  * *gpio* - GPIO port daného čidla
    * *limity_teploty* - Objekt obsahující hraniční teploty pro spínání čidla
      * *den* - objekt pro hodnoty během dne
        * *low* - teplota, při které se má topení zapnout
        * *high* - teplota, při které se má topení vypnout
      * *noc* - objekt pro hodnoty během noci. Parametry jsou shodné jako v denním objektu
      * *primarni* - boolean příznak, zda je čidlo primární. Primární čidla ovlivňují spínání topení nezávysle na ostatních - pokud je teplota na primárním čidle (libovolném) menší nebo rovna low hodnotě pro danou část dne, topíme bez ohledu na zbytek čidel.
* *den_zacatek* - první hodina denního režimu (začátek dne)
* *den_konec* - poslední hodina denního režimu (konec dne)
* *gpio_svetlo* - GPIO port, na kterém se nachází spínání relé pro ovládání světla
* *gpio_teplo* - GPIO port, na kterém se nachází spínání relé pro ovládání topení
* *dht_model* - model DHT čidla pro teplotu a vlhkost. Možné varianty jsou `11` a `22`
