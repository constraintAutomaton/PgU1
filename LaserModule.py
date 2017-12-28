# coding: utf-8
import serial

ser = serial.Serial('/dev/ttyACM0',baudrate = 9600, timeout = 1)
ser.write(b'l')
