#i/usr/bin/python
# -*- coding: utf-8 -*-

import RPi_I2C_driver
import time

LCD_ADDR = 0x27

lcd =RPi_I2C_driver.lcd(LCD_ADDR)

def DisplayController(num):
    lcd.clear()
        
    if num == 1:
        lcd.print("Helmet off")
        time.sleep(1)
    
    elif num == 2:
        lcd.print("Two People")
        time.sleep(1)
    
    elif num == 3:
        lcd.print("Helmet off Two People")
        time.sleep(1)
    
    elif num == 4:
        lcd.print("Ok")
        time.sleep(1)
    
