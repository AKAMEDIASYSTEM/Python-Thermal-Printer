# oh boy oh boy!
# It's project HOT_PANTS
from __future__ import print_function
import Adafruit_BBIO.UART as uart
from Adafruit_Thermal import *
import Adafruit_BBIO.ADC as adc
import Adafruit_BBIO.GPIO as gpio
import time
from serial import Serial
import random
import atexit

API_KEY = '718923e89a79ce5e8c3f5e888ea624e3'
wordURL = 'http://words.bighugelabs.com/api/2/718923e89a79ce5e8c3f5e888ea624e3/' # then {word} then '/json'
sensor_pin = 'P9_40'
extreme_lo = ['dark','inky','shadowed','midnight']
mid_lo = ['shady','dim','grey','faint']
mid_hi = ['light','shiny','clear','lustrous']
extreme_hi = ['blinding','superbright','brilliant','vivid']

preamble = ['Now it is hella ','Oh, just a bit ','It is quite ','Gosh it is ']

printer = Adafruit_Thermal("/dev/ttyO2", 19200, timeout=5)
printer.begin()
printer.feed(3)
printer.print("o hai")
rPast = 0

def checkSensor(rPast):
	r = adc.read(sensor_pin)

	if Math.abs(r-rPast) > 0.1:
		if r < 0.25:
			statement = random.choice(preamble) + random.choice(extreme_lo)
			printer.print(statement)
			printer.feed(1)
		elif r < 0.5:
			statement = random.choice(preamble) + random.choice(mid_lo)
			printer.print(statement)
			printer.feed(1)
		elif r < 0.75:
			statement = random.choice(preamble) + random.choice(mid_hi)
			printer.print(statement)
			printer.feed(1)
		else:
			statement = random.choice(preamble) + random.choice(extreme_hi)
			printer.print(statement)
			printer.feed(1)
		printer.print(r)
		printer.feed(2)
		rPast = r

def exit_handler():
    pass
    # print 'exiting'
    # adc.cleanup()
    # uart.cleanup() # not yet supported?

if __name__ == '__main__':
	adc.setup()
	atexit.register(exit_handler)
	while True:
		checkSensor(rPast)
		time.sleep(10)