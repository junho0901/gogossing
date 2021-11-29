#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
BUZ = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZ,GPIO.OUT)
GPIO.output(BUZ,GPIO.LOW)

def sound_on():    
    GPIO.output(BUZ, GPIO.HIGH)
    print("BUZZER ON")

def sound_off():
    GPIO.output(BUZ,GPIO.LOW)
    print("BUZZER OFF")
