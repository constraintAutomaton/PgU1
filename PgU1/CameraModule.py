from picamera import PiCamera
import os
import shutil
import time
import socket
from time import strftime


class Camera():
    """
    the class that handle all the thing relate to the camera such as taking picture, v
    ideo and streaming video.
    
    """
    def __init__(self):
        self.resolutionPhoto = (1024, 768)
        self.resolutionVideo = (640, 480)
        self.qualityVideo = 23
        self.destinationPhoto = r'Photo'
        self.destinationVideo = r'Video'
        self.extensionPhoto = 'jpg'
        self.extensionVideo = 'h264'

    def nameFile(self,extension,nameable):
        """
         return the name of the video or photo file with is extension
        """
        date = strftime('%Y-%m-%d___%H:%M:%S')
        if nameable == False:
            nameFile = '{}.{}'.format(date, extension)
        else:
            name = input('Entrez le nom du fichier: ') 
            
            nameFile = '{}___{}.{}'.format(name, date, extension)
        return nameFile
        
    def takePicture(self,delay=0.1,nameable=False,stopable = False,duration=0):
        """
         take a picture after a certain amounth of time to prepare the camera or by user request.
         the picture is name using the current time by default but the user can choose a custom name.
         soon will add stopable that will take picture in burst define by the user.
        """
        nameFile = self.nameFile(self.extensionPhoto,nameable)
        with PiCamera() as camera:
           camera.resolution = self.resolutionPhoto
           camera.vflip = True
           time.sleep(delay)
           camera.capture(nameFile)
           
        shutil.move(nameFile,r'{}/{}'.format(self.destinationPhoto,nameFile))
        
        
    
    def recordVideo(self,duration=0,nameable=False,stopable = False,delay=0):
        """
        record a video.The camera can either record the video an certain amounth of time
        or can recorded until the user ask to stop.the later option is not working at the moment 
        """
        nameFile = self.nameFile(self.extensionVideo,nameable)
        if stopable:
            with PiCamera() as camera:
                camera.resolution= self.resolutionVideo
                camera.framerate = 60
                camera.vflip = True
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
             camera.vflip = True
             camera.start_recording(nameFile)
             #camera.start_preview(fullscreen = False, window = (100,100,640,480))
             camera.wait_recording(duration)
             camera.stop_recording()
             #camera.stop_preview()
         
        shutil.move(nameFile,r'{}/{}'.format(self.destinationVideo,nameFile))

a = Camera()
a.takePicture()
            
        
        
    


     


        
        
