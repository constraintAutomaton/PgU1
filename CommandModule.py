from CameraModule import Camera
from MovementModule import Movement
import RPi.GPIO as gpio
import os
import re
import threading
#from Queue import Queue as queue

global qCamera
global qMovement

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
            
    def threadMotorWheel(self, mvt,option):
        threadMovement = threading.Thread(target=mvt,kwargs=option)
        threadMovement.start()
    
    def threadCamera(self,action,option):
        threadCamera = threading.Thread(target=action,kwargs=option)
        threadCamera.start()
        
        
    def command(self,command): 
        if command.lower() == 'q':
            self.run = False
            self.kill()
            print('exit')
        elif command.lower() == 'i':
            self.info()
        elif command.lower()[0] == 't' and command.lower()[1] == ' ' : # regardé delay photo semble pas instatané peut-être mettre des thread ?
            
            if 'd' in command.lower() and 'n' in command.lower():
                delay = re.search('t d(.*) n',command.lower()).group(1)
                #self.takePicture(delay=float(delay),nameable=True)
                self.threadCamera(self.takePicture,{delay:float(delay),nameable:True})

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
            elif 'x' in command.lower():
                distance = command.lower()[3:]
                self.forward(distance=float(distance))
            else:
                self.forward()

        elif command.lower()[0] == 'b':
            if 't' in command.lower() and 'x' in command.lower() :
                print('enter only one type of movement')
                
            elif 's' in command.lower() and 'x' in command.lower() :
                print('enter only one type of movement')
                
            elif 't' in command.lower() and 's' in command.lower() :
                print('enter only one type of movement')
                
            elif 't' in command.lower() :
                duration = command.lower()[3:]
                self.backward(duration=float(duration))
            elif 's' in command.lower():
                self.backward(stopable=True)
            elif 'x' in command.lower():
                distance = command.lower()[3:]
                self.backward(distance=float(distance))
            else:
                self.backward()

        elif 'trf' in command.lower():
            if 't' in command.lower() and 'x' in command.lower() :
                print('enter only one type of movement')
                
            elif 's' in command.lower() and 'x' in command.lower() :
                print('enter only one type of movement')
                
            elif 't' in command.lower() and 's' in command.lower() and len(command.lower()) < 3 :
                print('enter only one type of movement')
            elif len(command.lower()) > 3:
                if command.lower()[4] == 't'  :
                    duration = command.lower()[5:]
                    self.turnRF(duration=float(duration))
                elif command.lower()[4] == 's':
                    self.turnRF(stopable=True)
                elif command.lower()[4] == 'x':
                    distance = command.lower()[4:]
                    self.turnRF(distance=float(distance))
            else:
                self.turnRF()
            

                
        elif 'trb' in command.lower():
            if 't' in command.lower() and 'x' in command.lower() :
                print('enter only one type of movement')
                
            elif 's' in command.lower() and 'x' in command.lower() :
                print('enter only one type of movement')
                
            elif 't' in command.lower() and 's' in command.lower() and len(command.lower()) < 3 :
                print('enter only one type of movement')
            elif len(command.lower()) > 3:
                if command.lower()[4] == 't'  :
                    duration = command.lower()[5:]
                    self.turnRB(duration=float(duration))
                elif command.lower()[4] == 's':
                    self.turnRB(stopable=True)
                elif command.lower()[4] == 'x':
                    distance = command.lower()[4:]
                    self.turnRB(distance=float(distance))
            else:
                self.turnRB()
                

        elif 'tlf' in command.lower():
            if 't' in command.lower() and 'x' in command.lower() :
                print('enter only one type of movement')
                
            elif 's' in command.lower() and 'x' in command.lower() :
                print('enter only one type of movement')
                
            elif 't' in command.lower() and 's' in command.lower() and len(command.lower()) < 3 :
                print('enter only one type of movement')
            elif len(command.lower()) > 3:
                if command.lower()[4] == 't'  :
                    duration = command.lower()[5:]
                    self.turnLF(duration=float(duration))
                elif command.lower()[4] == 's':
                    self.turnLF(stopable=True)
                elif command.lower()[4] == 'x':
                    distance = command.lower()[4:]
                    self.turnLF(distance=float(distance))
            else:
                self.turnLF()

        elif 'tlb' in command.lower():
            if 't' in command.lower() and 'x' in command.lower() :
                print('enter only one type of movement')
                
            elif 's' in command.lower() and 'x' in command.lower() :
                print('enter only one type of movement')
                
            elif 't' in command.lower() and 's' in command.lower() and len(command.lower()) < 3 :
                print('enter only one type of movement')
            elif len(command.lower()) > 3:
                if command.lower()[4] == 't'  :
                    duration = command.lower()[5:]
                    self.turnLB(duration=float(duration))
                elif command.lower()[4] == 's':
                    self.turnLB(stopable=True)
                elif command.lower()[4] == 'x':
                    distance = command.lower()[4:]
                    self.turnLB(distance=float(distance))
            else:
                self.turnLB()
        elif 'stop' in command.lower():
            self.stopAllMotor()
            print('motor stopped')
            
                
        
                
            

        
        
    def info(self):
        q = 'q : quitté\n\n'
        t = 'T dt n : take picture after a delay(d) of t(s) and ask for the name of the picture.d and n are optional\n\n'
        v = 'v dt s n: record a video of a duration (d) of t(s) or record a video until told to stop (s parameter).\
the parameter n is option and give the option to provide a name to the video\n\n'
        f = 'f x[] t[] s[] : move foward for a distace of x(mm) or\
for a duration of t(s) or until the user press a key\n\n'
        
        b = 'b x[] t[] s[] : move backward for a distace of x(mm) or\
for a duration of t(s) or until the user press a key\n\n'
         
        trf = 'trf x[] t[] s[] : turn foward whit the right wheel for an angle of x(deg) or\
for a duration of t(s) or until the user press a key\n\n'

        trb = 'trb x[] t[] s[] : turn back  whith the right wheel for an angle of x(deg) or\
for a duration of t(s) or until the user press a key\n\n'
        
        tlf = 'tlf x[] t[] s[] : turn foward whit the left wheel for an angle of x(deg) or\
for a duration of t(s) or until the user press a key\n\n'

        tlb = 'tlb x[] t[] s[] : turn back  whith the left wheel for an angle of x(deg) or\
for a duration of t(s) or until the user press a key\n\n'
        stop = 'stop any movement'
        
        

        info = q+t+v+f+b+trf+trb+tlf+tlb+stop

        print(info)
        
    
        
a = Command()


