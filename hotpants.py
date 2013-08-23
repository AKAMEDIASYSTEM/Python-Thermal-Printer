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
extreme_lo = ['dark','inky','shadowed','midnight''black','sinister','dour','glowering','glum','moody','morose','saturnine','sour','sullen','benighted','obscure','blue','dingy','disconsolate','dismal','gloomy','grim','sorry','drab','drear','dreary','colored','coloured','dark-skinned','non-white','depressing','dispiriting']
mid_lo = ['shady','dim','grey','faint','weak','dim','shadowy','vague','wispy','feeble','light','swooning','light-headed','lightheaded','fainthearted','timid','faint-hearted','cloudy','muddy','murky','turbid']
mid_hi = ['light','shiny','clear','lustrous','diaphanous','filmy','gauze-like','gossamer','see-through','sheer','transparent','vaporous','vapourous','cobwebby']
extreme_hi = ['blinding','superbright','brilliant','vivid','brilliant','vivid','smart','burnished','lustrous','shining','shiny','undimmed','promising','sunny','sunshiny']

preamble = ['Now it is hella ','Oh, just a bit ','It is quite ','Gosh it is ','Well looky here, it is ','Suddenly: ','Call the police, it is ']

printer = Adafruit_Thermal("/dev/ttyO2", 19200, timeout=5)
printer.begin()
printer.upsideDownOn()
printer.feed(3)
printer.print("o hai")
rPast = 0

def checkSensor():
	global rPast
	r = adc.read(sensor_pin)

	if abs(r-rPast) > 0.1:
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
	uart.setup("UART2")
	atexit.register(exit_handler)
	while True:
		checkSensor()
		time.sleep(0.5)