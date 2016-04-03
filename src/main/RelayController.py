import RPi.GPIO as GPIO
import os
import sys
import time
import xlrd


projPath = '/root/autowateringplant/src'
resPath = '/resources'
logPath = '/logs'
logName = '/RelayController.log'
fileName = '/Readings.xls'


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


relayPin= 23

GPIO.setup(23, GPIO.OUT)
GPIO.output(23, GPIO.HIGH)





def needWater():
    
    

if(needWater()):
    GPIO.output(23, GPIO.LOW)
    

#GPIO.output(23, GPIO.LOW)
#time.sleep(5)

#


GPIO.cleanup()

