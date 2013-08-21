# oh boy oh boy!
# It's project HOT_PANTS
from __future__ import print_function
import Adafruit_BBIO.UART as uart
from Adafruit_Thermal import *
import Adafruit_BBIO.ADC as adc
import Adafruit_BBIO.GPIO as gpio
import time
from serial import Serial

printer = Adafruit_Thermal("/dev/ttyO2", 19200, timeout=5)
printer.print("o hai")
