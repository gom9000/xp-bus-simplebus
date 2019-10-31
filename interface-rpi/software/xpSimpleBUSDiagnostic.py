#
# xpSimpleBUSDiagnostic.py
#           ___ _            _     ___ _   _ ___ 
# __ ___ __/ __(_)_ __  _ __| |___| _ ) | | / __|
# \ \ / '_ \__ \ | '  \| '_ \ / -_) _ \ |_| \__ \
# /_\_\ .__/___/_|_|_|_| .__/_\___|___/\___/|___/
#     |_|              |_|                       
#
# Author.....: Alessandro Fraschetti (mail: gos95@gommagomma.net)
# Target.....: RaspberryPI
# Version....: 1.0 2019/03/31
# Description: xpSimpleBUS Hardware Diagnostic Tool
# URL........: 
# License....: This code is under MIT License (https://github.com/gom9000/xp-simplebus/blob/master/LICENSE)
#


import RPi.GPIO as GPIO
from xpSimpleBUS import xpSimpleBUS


# config
busop_delay = 0.000001
ad_pin_list = [5, 6, 13, 19, 26, 16, 20, 21]
ctrl_pin_list = [17, 27, 22]
out_port_address_list = [1,3]
in_port_address_list = [0,2]
data_out = 85 # 01010101


# diagnostic
#print ("------------------------------------")
print ("-----------------------------------------------------")
print ("xpSimpleBUS Hardware Diagnostic Tool")
print ("-----------------------------------------------------")

print ("Iinitialize SimpleBUS: ")
xpSimpleBus = xpSimpleBUS(ad_pin_list, ctrl_pin_list, busop_delay)
#print ("\tDelay time between bus operations: %.2f"% busop_delay)
print ("\tFrequency of bus operations: %.2fHz"% (1/busop_delay))

print ("\tAddress/Data lines: ")
for ii in range(len(ad_pin_list)):
   print ("\t\tAD%d line on GPIO%d"% (ii, ad_pin_list[ii])) 

print ("\tControl lines: ")
print ("\t\tCTRL /ALE line on GPIO%d"% ctrl_pin_list[0]) 
print ("\t\tCTRL /RD line on GPIO%d"% ctrl_pin_list[1]) 
print ("\t\tCTRL /WR line on GPIO%d"% ctrl_pin_list[2]) 

print ("\tInput Ports: ")
for ii in range(len(in_port_address_list)):
    print ("\t\tINPORT%d at address: %s"% (ii, hex(in_port_address_list[ii])))

print ("\tOutput Ports: ")
for ii in range(len(out_port_address_list)):
    print ("\t\tOUTPORT%d at address: %s"% (ii, hex(out_port_address_list[ii])))

print ("Test Ports I/O: ")
print ("\tRead Input Ports: ")
for ii in range(len(in_port_address_list)):
    data = xpSimpleBus.input(in_port_address_list[ii])
    print ("\t\tINPORT%d value: %s"% (ii, hex(data)))

print ("\tWrite Output Ports (with value: %s): "% hex(data_out))
for ii in range(len(out_port_address_list)):
    xpSimpleBus.output(out_port_address_list[ii], data_out)
    print ("\t\tOUTPORT%d value: %s"% (ii, hex(data_out)))

print ("Test RAM I/O: ")
data_out = 255
print ("\tWrite and Read RAM locations with data: %s"% hex(data_out))
for ii in range(1, 32, 2):
    for jj in range(ii*8, ii*8+8):
        xpSimpleBus.output(jj, data_out);
        if data_out != xpSimpleBus.input(jj):
            print ("\t\tError verifying data at address: %s"% hex(jj))

data_out = 0
print ("\tWrite and Read RAM locations with data: %s"% hex(data_out))
for ii in range(1, 32, 2):
    for jj in range(ii*8, ii*8+8):
        xpSimpleBus.output(jj, data_out);
        if data_out != xpSimpleBus.input(jj):
            print ("\t\tError verifying data at address: %s"% hex(jj))

print ("-----------------------------------------------------")
