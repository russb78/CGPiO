import spidev # required for the MCP3008 ADC to function
import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BCM) # pin names (not actual pin numbers)

spi = spidev.SpiDev()
spi.open(0,0)

#set the sharp sensor pin numbers
left = 0
front = 1
right = 2
rear = 3

def readadc(adcnum):
    """Controls the MCP3008 chip to assign 8 analog pins from 0 to 7"""
    if ((adcnum > 7) or (adcnum < 0)):
        return -1
    r = spi.xfer2([1,(8+adcnum)<<4,0])
    adcout = ((r[1]&3) << 8) + r[2]
    return adcout

def read_sensors():
    """Reads each of the Sharp sensors are returns a list of analog readings 
    (0-1024) in order: left, front, right, rear"""
    reading = []
    for i in [left, front, right, rear]:
        reading.append(readadc(i))
    return reading

