from picamera import PiCamera
import os
import shutil
import time
from time import strftime

class Camera():
    def __init__(self):
        self.resolutionPhoto = (1024, 768)
        self.resolutionVideo = (640, 480)
        self.qualityVideo = 23
        self.destinationPhoto = r'/home/pi/Documents/Python_project/PgU1_code/Photo'
        self.destinationVideo = r'/home/pi/Documents/Python_project/PgU1_code/Video'

    def nameFile(self,extension):
        name = input('Entrez le mom du fichier: ') 
        date = strftime('%Y-%m-%d___%H:%M:%S')
        if name == '':
            nameFile = '{}.{}'.format(date, extension)
        else:
            
            nameFile = '{}___{}.{}'.format(name, date, extension)
        return nameFile
        
    def takePicture(self):
        
        nameFile =self.nameFile('jpg')
        with PiCamera() as camera:
           camera.resolution = self.resolutionPhoto
           #camera.start_preview()
           #sleep(2)
           camera.capture(nameFile)
          
        shutil.move(nameFile,self.destinationPhoto)
    
        
        with PiCamera() as camera:
            camera.resolution = self.resolutionVideo
    def recordVideoFixTime(self,timeVideo):
        nameFile = self.nameFile('h264')
        
        with PiCamera() as camera:
         camera.resolution= self.resolutionVideo
         camera.framerate = 60
         camera.start_recording(nameFile)
         #camera.start_preview(fullscreen = False, window = (100,100,640,480))
         camera.wait_recording(timeVideo)
         camera.stop_recording()
         camera.stop_preview()
         
         shutil.move(nameFile,self.destinationVideo)
 
     


        
        