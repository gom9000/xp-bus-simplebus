#
# xpSimpleBUS-app-echo.py
#           ___ _            _     ___ _   _ ___ 
# __ ___ __/ __(_)_ __  _ __| |___| _ ) | | / __|
# \ \ / '_ \__ \ | '  \| '_ \ / -_) _ \ |_| \__ \
# /_\_\ .__/___/_|_|_|_| .__/_\___|___/\___/|___/
#     |_|              |_|                       
#
# Author.....: Alessandro Fraschetti (mail: gos95@gommagomma.net)
# Target.....: RaspberryPI
# Version....: 1.0 2019/03/31
# Description: echo application
# URL........: 
# License....: This code is under MIT License (https://github.com/gom9000/xp-bus-simplebus/blob/master/LICENSE)
#


import time
import RPi.GPIO as GPIO
from xpSimpleBUS import xpSimpleBUS


GPIO.setwarnings(False)


# config
busop_delay = 0.001
ad_pin_list = [5, 6, 13, 19, 26, 16, 20, 21]
ctrl_pin_list = [17, 27, 22]
out_port_address_list = [1]
in_port_address_list = [0]


try:

    xpSimpleBus = xpSimpleBUS(ad_pin_list, ctrl_pin_list, busop_delay)

    old_data = 0
    data = 0
    while True:
        time.sleep(0.25)
        data = xpSimpleBus.input(in_port_address_list[0])
        if (data != old_data):
            old_data = data
            xpSimpleBus.output(out_port_address_list[0], data)

except KeyboardInterrupt:
  print ("Bye!")
