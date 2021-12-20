import threading
import Server_Write as SW
import DistanceChecker as DC
import PressureChecker as PC
import time

global count
count = 5

if __name__ == '__main__':
    try:
        while(1):
            distance = DC.get_distance()
            pressure = PC.get_pressure()
            if distance <10 and pressure > 1:
                count = 0
                SW.server_write(1)
            else:
                count += 1
                if (count >= 3):
                    SW.server_write(0)
            print("distance : {:.2f} cm".format(distance))
            print("Pressure: %d" % pressure)
    except KeyboardInterrupt:
        print("\nSTOP")
        print('Finish!')
