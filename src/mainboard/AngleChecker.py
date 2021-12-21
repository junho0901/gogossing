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

    roll_value = abs(imu.roll)

    return roll_value 

print(get_angle())
