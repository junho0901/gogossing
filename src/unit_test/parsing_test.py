import sys, os
import unittest
 
sys.path.append("/home/pi/Desktop/gogossing/src/mainboard")
import web_parser as w

def check_parsing(n):
    if n == 0 or n == 1:
        return 0
    else:
        return -1
    
class Testaddone(unittest.TestCase):
    def test_return(self):
        self.assertEqual(check_parsing(w.test_data()), 0)
