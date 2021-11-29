# -----------------------------------
# Control Ultrasonic Sensor
# -----------------------------------

# Package loading
import RPi.GPIO as GPIO
import time

# Sensor connect pin
E_PIN = 27  #BCM
T_PIN = 17

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
#def dist(t):
#    return (t*340/2)

# Execution function -----------------
def get_distance():
    GPIO.output(T_PIN, GPIO.LOW)
    time.sleep(.5)
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
def main(args):
    # Initialize
    init()

    i = 0
    try:
        while True:
            dist = get_distance()
            print("distance : {:.2f}m".format(dist))
            if dist <= 1.5:
                print(" waring 1.5 meters ")
            elif dist >= 1.5:
                print("safe  ")
    except KeyboardInterrupt:
        fin()
        print("\nSTOP")

    # resource return ---------------
    GPIO.cleanup()
    print('Finish!')
    return(0)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
