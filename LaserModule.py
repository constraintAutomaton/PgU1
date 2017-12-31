# coding: utf-8
import serial
import time


class Laser():
    def __init__(self,port = '/dev/ttyACM0', baudrate = 9600, timeout = 1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        
        self.ser = serial.Serial(self.port,baudrate=self.baudrate,timeout=self.timeout)
        time.sleep(5)
        
    def laserOn(self):
        self.ser.write(b'l')
        
    def laserOff(self):
        self.ser.write(b'g')
        
