import threading
from queue import Queue
import Server_Write as SW
import DistanceChecker as DC
import PressureChecker as PC
import time

global count
count = 5

que = Queue()

def Distance(queue):
    queue.put(DC.get_distance())

def Pressure(queue):
    queue.put(PC.get_pressure())


if __name__ == '__main__':
    try:
        while(1):
            t1 = threading.Thread(target=Distance, args=(que,))
            t2 = threading.Thread(target=Pressure, args=(que,))
            t1.start()
            t1.join()
            dist = que.get()
            t2.start()
            t2.join()
            press = que.get()
            if dist < 10 and press > 1:
                count = 0
                SW.server_write(1)
            else:
                count += 1
                if (count >= 3):
                    SW.server_write(0)
            print("distance : {:.2f} cm".format(dist))
            print("Pressure: %d" % press)
    except KeyboardInterrupt:
        print("\nSTOP")
        print('Finish!')
