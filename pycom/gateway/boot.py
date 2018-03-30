# boot.py -- run on boot-up
from network import WLAN
#from package import log
import machine
import configuration as CONFIG
wlan = WLAN(mode=WLAN.STA)
#wlan.ifconfig(config=('192.168.178.107','255.255.255.0','192.168.178.1','8.8.8.8'))
nets = wlan.scan()

for net in nets:
    if net.ssid == CONFIG.SSID:
        print('Network Found!')
        wlan.connect(net.ssid, auth=(None,CONFIG.WIFIPASSWORD), timeout=5000)
        while not wlan.isconnected():
            machine.idle()
        print('WLAN connection succeeded!')
        break
