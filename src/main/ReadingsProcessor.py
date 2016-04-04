#!/usr/bin/python

from xlutils.copy import copy
import xlrd
import xlwt
import os
import logging
import SensorReader as SR
import datetime


projPath = '/root/autowateringplant/src'
resPath = '/resources'
logPath = '/logs'
logName = '/ReadingsProcessor.log'
fileName = '/Readings.xls'

logging.basicConfig(filename = projPath + logPath + logName + '{:%Y%m%d%H%M%S}'.format(datetime.datetime.now()), level=logging.DEBUG)

def createFile():
    book = xlwt.Workbook()
    sheet_readings = book.add_sheet('Readings')
    sheet_readings.write(0, 0, 'ID')
    sheet_readings.write(0, 1, 'Timestamp')
    sheet_readings.write(0, 2, 'Temperature')
    sheet_readings.write(0, 3, 'Pressure')
    sheet_readings.write(0, 4, 'Humidity')
    sheet_readings.write(0, 5, 'Moisture')

    #Adding readings column for plant 2
    sheet_readings.write(0, 6, 'Moisture 2')
    
    book.save(projPath + resPath + fileName)
    logging.info("Created new Readings File.")

def writeReadings():

    logging.info("Opening existing Readings file...")
    
    reader_book = xlrd.open_workbook(projPath + resPath + fileName, formatting_info=True)
    reader_sheet = reader_book.sheet_by_index(0)
    row = reader_sheet.nrows
    writer_book = copy(reader_book)
    sheet = writer_book.get_sheet(0)

    logging.info("Writing Readings...")
    
    sheet.write(row, 0, row)
    sheet.write(row, 1, '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
    sheet.write(row, 2, str(SR.getTemp()) + ' *C')
    sheet.write(row, 3, str(SR.getPressure()) + ' Pa')
    sheet.write(row, 4, str(SR.getHumidity()) + ' %')
    sheet.write(row, 5, str(SR.getMoisture()))
    #Setting up a 6th coloum for the second plant
    sheet.write(row, 6, str(SR.getMoisture2()))

    logging.info("Finished writing readings. Saving file and exiting...")

    writer_book.save(projPath + resPath + fileName)


if __name__ == '__main__':
    if(os.path.isfile(projPath + resPath + fileName)):
        writeReadings()
    else:
        logging.info("Readings file does not exist. Creating new readings file at : {}".format(projPath + resPath + fileName))
        createFile()
        writeReadings()


