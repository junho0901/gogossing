#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
BUZ = 12


def setPinSound():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUZ,GPIO.OUT)
    GPIO.output(BUZ,GPIO.LOW)

def set_sound(check):
    if check ==ON:
         GPIO.output(BUZ, GPIO.HIGH)
         print("BUZZER ON")
         time.sleep(2)
    else:
        GPIO.output(BUZ,GPIO.LOW)
        print("BUZZER OFF")
        time.sleep(2)
        
