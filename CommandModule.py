from CameraModule import Camera
from MovementModule import Movement
import RPi.GPIO as gpio
import os
import re

class Command(Camera,Movement):
    def __init__(self,mode=0,name = 'unit001'):
        Camera.__init__(self)
        Movement.__init__(self)
        self.stopAllMotor() # sinon les roues bougent pour une raison inconnus
    
        self.name = name
        self.run = True
        
        if mode == 0:
            self.runCommandWindowMode()
        
    def runCommandWindowMode(self):
        print('Enter "q" for exit\nEnter "i" for command info')
        
        while self.run  :
            command = input('Enter a command: ')
            self.command(command)
            
            

    def command(self,command): # ajouter des try pour les erreurs
        if command.lower() == 'q':
            self.run = False
            self.kill()
            print('exit')
        elif command.lower() == 'i':
            self.info()
        elif command.lower()[0] == 't': # regardé delay photo semble pas instatané peut-être mettre des thread ?
            
            if 'd' in command.lower() and 'n' in command.lower():
                delay = re.search('t d(.*) n',command.lower()).group(1)
                self.takePicture(delay=float(delay),nameable=True)

            elif 'd' in command.lower():
                delay = re.search('t d(.*)',command.lower()).group(1)
                self.takePicture(delay=float(delay))
            elif 'n' in command.lower():
                self.takePicture(nameable=True)
            else:
                self.takePicture()
            print('done')               
            
        elif command.lower()[0] == 'v':
            if 'd' in command.lower() and 'n' in command.lower() :
                duration = re.search('v d(.*) ',command.lower()).group(1)
                self.recordVideo(duration=float(duration),nameable=True)
            
            elif 's' in command.lower():
                self.recordVideo(stopable=True)
            elif 's' in command.lower() and 'n' in command.lower() :
                self.recordVideo(stopable=True,nameable=True)
            print('done')

        elif command.lower()[0] == 'f':
            if 't' in command.lower() and 'x' in command.lower() :
                print('enter only one type of movement')
                
            elif 's' in command.lower() and 'x' in command.lower() :
                print('enter only one type of movement')
                
            elif 't' in command.lower() and 's' in command.lower() :
                print('enter only one type of movement')
                
            elif 't' in command.lower() :
                duration = command.lower()[3:]
                self.forward(duration=float(duration))
            elif 's' in command.lower():
                self.forward(stopable=True)
            

        
        
    def info(self):
        q = 'q : quitté\n\n'
        t = 'T dt n : take picture after a delay(d) of t(s) and ask for the name of the picture.d and n are optional\n\n'
        v = 'v dt s n: record a video of a duration (d) of t(s) or record a video until told to stop (s parameter).\
the parameter n is option and give the option to provide a name to the video\n\n'
        f = 'f x[] t[] s[] : move foward for a distace of x(mm) or\
for a duration of t(s) or until the user press a key\n\n'
        
        bx = 'b x : move backward for a distace of x(mm)\n\n'
        bt = 'b x : move backward for a duration of t(s)\n\n'
        trteta = 'tR teta : turn right for an angle of teta(deg)\n\n'
        trt = 'tR t : turn right for a duration of t(s)\n\n'
        tlteta = 'tL teta : turn left for an angle of teta(deg)\n\n'
        tlt = 'tL t : turn left for a duration of t(s)\n\n'

        info = q+t+v+f+bx+bt+trteta+trt+tlteta+tlt

        print(info)
        
    
        
a = Command()


