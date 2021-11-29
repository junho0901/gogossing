#IP GPS
import json
import requests

def Get_GPS():
    url = 'http://ip-api.com/json'
    data = requests.get(url)
    res = data.json()
    print(res)

''' GPS Neo-6m Module 사용
import serial 
import pynmea2

def parseGPS(str): 
    if str.find('GGA') > 0: 
        msg = pynmea2.parse(str) 
        print("Timestamp: %s -- Lat: %s %s -- Lon: %s %s -- Altitude: %s %s" % (msg.timestamp,msg.lat,msg.lat_dir,msg.lon,msg.lon_dir,msg.altitude,m sg.altitude_units)) 
        serialPort = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5) 
        while True: 
            str = serialPort.readline() 
            parseGPS(str)
'''

            
