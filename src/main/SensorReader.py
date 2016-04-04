################import variables############
import time
import os
import sys
import Adafruit_BMP.BMP085 as BMP085
import Adafruit_DHT
import RPi.GPIO as GPIO 
import mcp3008

############################################



########## initalize pins and sensors###########

dhtSensor = Adafruit_DHT.DHT11
bmpSensor = BMP085.BMP085()

dhtPin = 4
mcpPin = 0


# Initializing GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()


##############################################

############ read sensor ####################

dhtHumi, dhtTemp = Adafruit_DHT.read_retry(dhtSensor, dhtPin)
bmpTemp=bmpSensor.read_temperature()
avgTemp = 0
bmpPressure = 0
mcpMoisture = 0

def getPressure():
    bmpPressure=bmpSensor.read_pressure()
    return bmpPressure;

def getTemp():
    dhtHumi, dhtTemp = Adafruit_DHT.read_retry(dhtSensor, dhtPin)
    bmpTemp=bmpSensor.read_temperature()
    avgTemp = (dhtTemp + bmpTemp)/2
    return avgTemp

def getHumidity():
    dhtHumi, dhtTemp = Adafruit_DHT.read_retry(dhtSensor, dhtPin)
    return dhtHumi

def getMoisture():
    mcpMoisture = mcp3008.readadc(mcpPin)
    return mcpMoisture










