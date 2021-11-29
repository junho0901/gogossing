import spidev

import time

#Define Variables
pad_channel0 = 0
pad_channel1 = 2
pad_channel2 = 4
pad_channel3 = 6

#Create SPI
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz=1000000

 
def get_strength(adcnum):
# read SPI data from the MCP3008, 8 channels in total

    if adcnum > 7 or adcnum < 0:
        return -1

    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]

    return data

try:
    while True:
        pad_value0 = get_strength(pad_channel0)
        pad_value1 = get_strength(pad_channel1)
        pad_value2 = get_strength(pad_channel2)
        pad_value3 = get_strength(pad_channel3)

        print("---------------------------------------")
        print("Pressure Pad Value0: %d \n" % pad_value0)
        print("Pressure Pad Value1: %d \n" % pad_value1)
        print("Pressure Pad Value2: %d \n" % pad_value2)
        print("Pressure Pad Value3: %d \n" % pad_value3)

        time.sleep(0.5)

except KeyboardInterrupt:
    pass
