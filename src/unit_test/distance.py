# -----------------------------------
# Control Ultrasonic Sensor
# -----------------------------------

# Package loading
import RPi.GPIO as GPIO
import time

# Sensor connect pin
E_PIN = 24  #BCM
T_PIN = 23

# Define function --------------------

# Initialize function ----------------
def init():
    # (1) init name type
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # (2) pin info setting
    GPIO.setup(T_PIN, GPIO.OUT)
    GPIO.setup(E_PIN, GPIO.IN)

    # (3) initial value
    GPIO.output(T_PIN, GPIO.LOW)

# Calculate distance -----------------
def dist(t):
    return (t*340/2)

# Execution function -----------------
def get_distance():
    GPIO.output(T_PIN, GPIO.LOW)
    time.sleep(.00001)
    GPIO.output(T_PIN, GPIO.HIGH)
    time.sleep(.00001)  # 10 us
    GPIO.output(T_PIN, GPIO.LOW)

    while GPIO.input(E_PIN) == GPIO.LOW:
        pulse_begin = time.time()
    while GPIO.input(E_PIN) == GPIO.HIGH:
        pulse_end = time.time()
    duration = float(pulse_end - pulse_begin)
    distance = dist(duration)
    return distance

# Entry point function --------------



def test_ultrasonic():
    init()
    count = 0
    for i in range(5):
        test = get_distance()
        time.sleep(0.1)
        print("distance : {:.2f}m".format(test))
        if test > 0.0 or test < 13.0:
            count = count + 1
    GPIO.cleanup()        
    return count

# resource return ---------------


