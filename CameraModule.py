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
        self.extensionPhoto = 'jpg'
        self.extensionVideo = 'h264'

    def nameFile(self,extension,nameable):
        date = strftime('%Y-%m-%d___%H:%M:%S')
        if nameable == False:
            nameFile = '{}.{}'.format(date, extension)
        else:
            name = input('Entrez le nom du fichier: ') 
            
            nameFile = '{}___{}.{}'.format(name, date, extension)
        return nameFile
        
    def takePicture(self,delay=0.1,nameable=False,stopable = False,duration=0):
        #duration and stopable is useless it's just for the command in the actionThread
        nameFile = self.nameFile(self.extensionPhoto,nameable)
        with PiCamera() as camera:
           camera.resolution = self.resolutionPhoto
           time.sleep(delay)
           camera.capture(nameFile)
          
        shutil.move(nameFile,self.destinationPhoto)
        
    
    def recordVideo(self,duration=0,nameable=False,stopable = False,delay=0):
        #same photo
        nameFile = self.nameFile(self.extensionVideo,nameable)
        if stopable:
            with PiCamera() as camera:
                camera.resolution= self.resolutionVideo
                camera.framerate = 60
                while stopable:
                    camera.start_recording(nameFile)
                    command = input('press enter to stop: ')
                    stopable = False
                    #camera.start_preview(fullscreen = False, window = (100,100,640,480))
                camera.stop_recording()
                #camera.stop_preview()
                
                
        else:
            with PiCamera() as camera:
             camera.resolution= self.resolutionVideo
             camera.framerate = 60
             camera.start_recording(nameFile)
             #camera.start_preview(fullscreen = False, window = (100,100,640,480))
             camera.wait_recording(duration)
             camera.stop_recording()
             #camera.stop_preview()
         
        shutil.move(nameFile,self.destinationVideo)


     


        
        
