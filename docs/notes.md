# Poznamky k nasazeni

* V souboru `RPi_I2C_driver.py` je potřeba nastavit I2C adresu vašeho LCD (zjistíte přes utilitku i2cdetect), k tomu slouží řádek 54. V mém případě je LCD na adrese 0x38.
* v zabbixu je potreba zvetsit timeout na 30s, protoze cteni cidla se za 3s defaultniho timeoutu nestihne
* zabbix potrebuje pristup k GPIO - je potreba uzivatele, pod kterym zabbix agent bezi, pridat do skupiny gpio