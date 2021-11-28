import os
import sys
import time
import smbus

from imusensor.MPU9250 import MPU9250

address = 0x68
bus = smbus.SMBus(1)
imu = MPU9250.MPU9250(bus, address)
imu.begin()


while True:
    imu.readSensor()
    imu.computeOrientation()

    #print("roll: {0} ; pitch : {1} ; yaw : {2}".format(imu.roll, imu.pitch, imu.yaw))
    # rolling degree: imu.roll
    # pitching degree: imu.pitch
    # yawing degree: imu.yaw
    
    print(imu.roll)
    print(abs(imu.roll))
    if abs(imu.roll) > 55.0:
        print("Error")
        
    time.sleep(0.5)
