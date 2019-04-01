#
# xpSimpleBUS.py
#           ___ _            _     ___ _   _ ___ 
# __ ___ __/ __(_)_ __  _ __| |___| _ ) | | / __|
# \ \ / '_ \__ \ | '  \| '_ \ / -_) _ \ |_| \__ \
# /_\_\ .__/___/_|_|_|_| .__/_\___|___/\___/|___/
#     |_|              |_|                       
#
# Author.....: Alessandro Fraschetti (mail: gos95@gommagomma.net)
# Target.....: RaspberryPI
# Version....: 1.0 2019/03/30
# Description: python driver module for xpSimpleBUS hardware
# URL........: 
# License....: This code is under MIT License (https://github.com/gom9000/xp-bus-simplebus/blob/master/LICENSE)
#


import RPi.GPIO as GPIO
import time
import math


# ============================================================================
# xpSimpleBUS
# ============================================================================
class xpSimpleBUS:
    CTRL_ALE_IDX = 0
    CTRL_RD_IDX = 1
    CTRL_WR_IDX = 2


    # ------------------------------------------------------------------------
    # Inits the XPSimpleBUS and sets address-data and control GPIO pins
    # ------------------------------------------------------------------------
    def __init__(self, ad_pins, ctrl_pins, busop_delay):
        self.xp_simplebus_delay = busop_delay
        self.xp_simplebus_wait_for_device = self.xp_simplebus_delay * 2
        self.xp_simplebus_ad_pins = ad_pins
        self.xp_simplebus_ctrl_pins = ctrl_pins

        GPIO.setmode(GPIO.BCM)
        for ii in range(len(self.xp_simplebus_ctrl_pins)):
            GPIO.setup(self.xp_simplebus_ctrl_pins[ii], GPIO.OUT)
            GPIO.output(self.xp_simplebus_ctrl_pins[ii], GPIO.HIGH)

        for ii in range(len(self.xp_simplebus_ad_pins)):
            GPIO.setup(self.xp_simplebus_ad_pins[ii], GPIO.OUT)
            GPIO.output(self.xp_simplebus_ad_pins[ii], GPIO.LOW)


    # ------------------------------------------------------------------------
    # Clean GPIO
    # ------------------------------------------------------------------------
    def __del__(self):
        GPIO.cleanup()


    # ----------------------------------------------------
    # Performs OUTPUT addr, data
    # ----------------------------------------------------
    def output(self, addr, data):
        # writes address
        for ii in range(len(self.xp_simplebus_ad_pins)):
            GPIO.setup(self.xp_simplebus_ad_pins[ii], GPIO.OUT)
        for ii in range(len(self.xp_simplebus_ad_pins)):
            GPIO.output(self.xp_simplebus_ad_pins[ii], addr&int(math.pow(2, ii)))
        time.sleep(self.xp_simplebus_delay)

        # sets /ALE
        GPIO.output(self.xp_simplebus_ctrl_pins[self.CTRL_ALE_IDX], GPIO.LOW)
        time.sleep(self.xp_simplebus_delay)

        # sets /WR
        GPIO.output(self.xp_simplebus_ctrl_pins[self.CTRL_WR_IDX], GPIO.LOW)
        time.sleep(self.xp_simplebus_delay)

        # writes data
        for ii in range(len(self.xp_simplebus_ad_pins)):
            GPIO.setup(self.xp_simplebus_ad_pins[ii], GPIO.OUT)
        for ii in range(len(self.xp_simplebus_ad_pins)):
            GPIO.output(self.xp_simplebus_ad_pins[ii], data&int(math.pow(2, ii)))
        time.sleep(self.xp_simplebus_delay)

        # unsets /WR
        GPIO.output(self.xp_simplebus_ctrl_pins[self.CTRL_WR_IDX], GPIO.HIGH)
        time.sleep(self.xp_simplebus_delay)

        # waits a bit
        time.sleep(self.xp_simplebus_wait_for_device)

        # unsets /ALE
        GPIO.output(self.xp_simplebus_ctrl_pins[self.CTRL_ALE_IDX], GPIO.HIGH)
        time.sleep(self.xp_simplebus_delay)


    # ----------------------------------------------------
    # Performs INPUT addr, data
    # ----------------------------------------------------
    def input(self, addr):
        din = 0
        # writes address
        for ii in range(len(self.xp_simplebus_ad_pins)):
            GPIO.setup(self.xp_simplebus_ad_pins[ii], GPIO.OUT)
        for ii in range(len(self.xp_simplebus_ad_pins)):
            GPIO.output(self.xp_simplebus_ad_pins[ii], addr&int(math.pow(2, ii)))
        time.sleep(self.xp_simplebus_delay)

        # sets /ALE
        GPIO.output(self.xp_simplebus_ctrl_pins[self.CTRL_ALE_IDX], GPIO.LOW)
        time.sleep(self.xp_simplebus_delay)

        # sets /RD
        GPIO.output(self.xp_simplebus_ctrl_pins[self.CTRL_RD_IDX], GPIO.LOW)
        time.sleep(self.xp_simplebus_delay)

        # wait a bit
        time.sleep(self.xp_simplebus_wait_for_device)

        # reads data
        for ii in range(len(self.xp_simplebus_ad_pins)):
            GPIO.setup(self.xp_simplebus_ad_pins[ii], GPIO.IN)
        for ii in range(len(self.xp_simplebus_ad_pins)):
            din = (din<<1)|GPIO.input(self.xp_simplebus_ad_pins[len(self.xp_simplebus_ad_pins)-ii-1])
        time.sleep(self.xp_simplebus_delay)

        # unset /RD
        GPIO.output(self.xp_simplebus_ctrl_pins[self.CTRL_RD_IDX], GPIO.HIGH)
        time.sleep(self.xp_simplebus_delay)

        # waits a bit
        time.sleep(self.xp_simplebus_wait_for_device)

        # unsets /ALE
        GPIO.output(self.xp_simplebus_ctrl_pins[self.CTRL_ALE_IDX], GPIO.HIGH)
        time.sleep(self.xp_simplebus_delay)

        for ii in range(len(self.xp_simplebus_ad_pins)):
            GPIO.setup(self.xp_simplebus_ad_pins[ii], GPIO.OUT)

        return din
