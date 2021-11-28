#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

A_BUZ_PIN = 21

def main(args):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(A_BUZ_PIN,GPIO.OUT)
    GPIO.output(A_BUZ_PIN,GPIO.LOW)
    
    try:
        while True:
            GPIO.output(A_BUZ_PIN, GPIO.HIGH)
            print("BUZZER ON")
            time.sleep(2)
            
            GPIO.output(A_BUZ_PIN,GPIO.LOW)
            print("BUZZER OFF")
            time.sleep(2)
            
    except KeyboardInterrupt:
        GPIO.cleanup()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
