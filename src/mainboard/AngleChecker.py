import os
import sys
import time
import smbus

from imusensor.MPU9250 import MPU9250

address = 0x68
bus = smbus.SMBus(1)
imu = MPU9250.MPU9250(bus, address)
imu.begin()


def get_angle():
    imu.readSensor()
    imu.computeOrientation()

    print(imu.roll)
    print(abs(imu.roll))
    if abs(imu.roll) > 55.0:  //Error if rolling degree exceeds 55
        print("Error")
     
    time.sleep(0.5)
