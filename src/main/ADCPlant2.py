################import variables############
import time
import os
import sys
import Adafruit_BMP.BMP085 as BMP085
import Adafruit_DHT
import RPi.GPIO as GPIO 
import mcp3008

########## initalize pins and sensors###########
mcpPin2 = 0

plant2=0

plant2=mcp3008.readadc(mcpPin2)

print plant2

