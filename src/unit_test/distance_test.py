import sys, os
import unittest
 
sys.path.append("/home/pi/Desktop/gogossing/src/example")
import distance as d

def test_sensor(n):
    if n == 5:
        return 0
    else:
        return -1
    
class Testaddone(unittest.TestCase):
    def test_return(self):
        self.assertEqual(test_sensor(d.test_ultrasonic()), 0)
       
