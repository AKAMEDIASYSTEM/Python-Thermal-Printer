# oh boy oh boy!
# It's project HOT_PANTS
from __future__ import print_function
import Adafruit_BBIO.UART as uart
from Adafruit_Thermal import *
import Adafruit_BBIO.ADC as adc
import Adafruit_BBIO.GPIO as gpio
import time
from serial import Serial
import atexit

sensor_pin = 'P9_40'


printer = Adafruit_Thermal("/dev/ttyO2", 19200, timeout=5)
printer.begin()
printer.feed(3)
printer.print("o hai")

def checkSensor():
	r = adc.read(sensor_pin)
	printer.print(r)
	printer.feed(3)

def exit_handler():
    pass
    # print 'exiting'
    # adc.cleanup()
    # uart.cleanup() # not yet supported?

if __name__ == '__main__':
	adc.setup()
	atexit.register(exit_handler)
	while True:
		checkSensor()
		time.sleep(30)