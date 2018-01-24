# coding: utf-8
from CameraModule import Camera
from MovementModule import Movement
import RPi.GPIO as gpio
import os
import re
import threading
from queue import Queue
import paramiko


class Command(Camera,Movement):
    def __init__(self,mode=0,name = 'unit001'):
        Camera.__init__(self)
        Movement.__init__(self)
        self.stopAllMotor() # sinon les roues bougent pour une raison inconnus
    
        self.name = name
        self.run = True
        self.qCamera = Queue()
        self.qMovement = Queue()
        self.threadMovement = None
        self.threadCamera = None
        
        if mode == 0:
            self.runCommandWindowMode()
        
    def runCommandWindowMode(self):
        print('Enter "q" for exit\nEnter "i" for command info')
        
        while self.run  :
            command = input('Enter a command: ')
            self.command(command)
            
            
    def actionThreadMovement(self, mvt=None,duration=0,stopable=False,distance=0,angle=0):
        self.qMovement.join()
        self.qMovement.put(lambda: mvt(duration=duration,stopable=stopable,distance=distance,angle=angle)) # pour mettre une fonction dans le queue
        callFuction = self.qMovement.get()
        callFuction()
        self.qMovement.task_done()
        
    
    def actionThreadCamera(self,action,delay=0.5,nameable=False,duration=0,stopable = False):
        self.qCamera.join()
        self.qCamera.put(lambda: action(delay=delay,nameable=nameable,duration=duration,stopable=stopable))
        callFuction = self.qCamera.get()
        callFuction()
        self.qCamera.task_done()
        
    def command(self,command):
        if command.lower() == 'q':
            self.run = False
            self.kill()
            print('exit')
        elif command.lower() == 'i':
            self.info()
            
        elif command.lower() =='test':
            self.test_connection()
            
        elif command.lower()[0] == 'f':
            if 't' in command.lower() and 'x' in command.lower() :
                print('enter only one type of movement')
                
            elif 's' in command.lower() and 'x' in command.lower() :
                print('enter only one type of movement')
                
            elif 't' in command.lower() and 's' in command.lower() :
                print('enter only one type of movement')
                
            elif 't' in command.lower() :
                duration = command.lower()[3:]
                #self.forward(duration=float(duration))
                self.threadMovement = threading.Thread(target=self.actionThreadMovement,kwargs={'mvt':self.forward,'duration':float(duration)})
            elif 's' in command.lower(): # THREAD
                self.forward(stopable=True)
            elif 'x' in command.lower():
                distance = command.lower()[3:]
                #self.forward(distance=float(distance))
                self.threadMovement = threading.Thread(target=self.actionThreadMovement,kwargs={'mvt':self.forward,'distance':float(distance)})
            else:
               self.threadMovement = threading.Thread(target=self.actionThreadMovement,kwargs={'mvt':self.forward})
            self.threadMovement.start()
              

        elif command.lower()[0] == 'b':
            if 't' in command.lower() and 'x' in command.lower() :
                print('enter only one type of movement')
                
            elif 's' in command.lower() and 'x' in command.lower() :
                print('enter only one type of movement')
                
            elif 't' in command.lower() and 's' in command.lower() :
                print('enter only one type of movement')
                
            elif 't' in command.lower() :
                duration = command.lower()[3:]
                #self.backward(duration=float(duration))
                self.threadMovement = threading.Thread(target=self.actionThreadMovement,kwargs={'mvt':self.backward,'duration':float(duration)})

            elif 's' in command.lower(): # THREAD
                self.backward(stopable=True)
            elif 'x' in command.lower():
                distance = command.lower()[3:]
                #self.backward(distance=float(distance))
                self.threadMovement = threading.Thread(target=self.actionThreadMovement,kwargs={'mvt':self.backward,'distance':float(distance)})
            else:
                self.threadMovement = threading.Thread(target=self.actionThreadMovement,kwargs={'mvt':self.backward})
            self.threadMovement.start()
                

        elif 'trf' in command.lower() :
            
            if 't' in command.lower() and 'x' in command.lower() :
                print('enter only one type of movement')
                
            elif 's' in command.lower() and 'x' in command.lower() :
                print('enter only one type of movement')
                
            elif 't' in command.lower() and 's' in command.lower() and len(command.lower()) < 3 :
                print('enter only one type of movement')
            elif len(command.lower()) > 3:
                if command.lower()[4] == 't'  :
                    duration = command.lower()[5:]
                    #self.turnRF(duration=float(duration))
                    self.actionThreadMovement(self.turnRF,{'duration':float(duration)})
                    self.threadMovement = threading.Thread(target=self.actionThreadMovement,kwargs={'mvt':self.turnRF,'duration':float(duration)})
                elif command.lower()[4] == 's': # THREAD
                    self.turnRF(stopable=True)
                elif command.lower()[4] == 'x':
                    angle = command.lower()[4:]
                    #self.turnRF(distance=float(angle))
                    self.threadMovement = threading.Thread(target=self.actionThreadMovement,kwargs={'mvt':self.turnRF,'angle':float(angle)})
            else:
                #self.turnRF()
                self.threadMovement = threading.Thread(target=self.actionThreadMovement,kwargs={'mvt':self.turnRF})
            self.threadMovement.start()
                
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
                    #self.turnRB(duration=float(duration))
                    self.threadMovement = threading.Thread(target=self.actionThreadMovement,kwargs={'mvt':self.turnRB,'duration':float(duration)})
                elif command.lower()[4] == 's':# THREAD
                    self.turnRB(stopable=True)
                elif command.lower()[4] == 'x':
                    angle = command.lower()[4:]
                    #self.turnRB(distance=float(angle))
                    self.threadMovement = threading.Thread(target=self.actionThreadMovement,kwargs={'mvt':self.turnRB,'angle':float(angle)})
            else:
                self.threadMovement = threading.Thread(target=self.actionThreadMovement,kwargs={'mvt':self.turnRB})
            self.threadMovement.start()
                

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
                    #self.turnLF(duration=float(duration))
                    self.threadMovement = threading.Thread(target=self.actionThreadMovement,kwargs={'mvt':self.turnLF,'duration':float(duration)})
                elif command.lower()[4] == 's':# THREAD
                    self.turnLF(stopable=True)
                elif command.lower()[4] == 'x':
                    angle = command.lower()[4:]
                    #self.turnLF(distance=float(angle))
                    self.threadMovement = threading.Thread(target=self.actionThreadMovement,kwargs={'mvt':self.turnLF,'angle':float(angle)})
            else:
                self.threadMovement = threading.Thread(target=self.actionThreadMovement,kwargs={'mvt':self.turnLF})
            self.threadMovement.start()

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
                    #self.turnLB(duration=float(duration))
                    self.threadMovement = threading.Thread(target=self.actionThreadMovement,kwargs={'mvt':self.turnLB,'duration':float(duration)})
                elif command.lower()[4] == 's':# THREAD
                    self.turnLB(stopable=True)
                elif command.lower()[4] == 'x':
                    distance = command.lower()[4:]
                    #self.turnLB(distance=float(distance))
                    self.threadMovement = threading.Thread(target=self.actionThreadMovement,kwargs={'mvt':self.turnLB,'angle':float(angle)})               
            else:
                self.threadMovement = threading.Thread(target=self.actionThreadMovement,kwargs={'mvt':self.turnLB})
            self.threadMovement.start()

        elif command.lower()[0] == 't':
            # regardé delay photo semble pas instatané peut-être mettre des thread ?
            
            if 'd' in command.lower() and 'n' in command.lower(): # THREAD
                delay = re.search('t d(.*) n',command.lower()).group(1)
                self.takePicture(delay=float(delay),nameable=True)
                #self.threadCamera(self.takePicture,{'delay':float(delay),'nameable':True})

            elif 'd' in command.lower():
                delay = re.search('t d(.*)',command.lower()).group(1)
                #self.takePicture(delay=float(delay))
                self.threadCamera = threading.Thread(target=self.actionThreadCamera,kwargs={'action':self.takePicture,'delay':delay})
                
            elif 'n' in command.lower(): # THREAD
                self.takePicture(nameable=True)
                #self.threadCamera(self.takePicture,{'nameable':True})
            else:
                self.threadCamera = threading.Thread(target=self.actionThreadCamera,kwargs={'action':self.takePicture})
            self.threadCamera.start()
            
                                        
        elif command.lower()[0] == 'v':
            if 'd' in command.lower() and 'n' in command.lower() : # THREAD
                duration = re.search('v d(.*) ',command.lower()).group(1)
                self.recordVideo(duration=float(duration),nameable=True)
                #self.threadCamera(self.recordVideo.{'duration':float(duration),'nameable':True})
            
            elif 's' in command.lower(): # THREAD
                self.recordVideo(stopable=True)
                #self.threadCamera(self.recordVideo.{'stopable':True})
            elif 's' in command.lower() and 'n' in command.lower() : # THREAD
                self.recordVideo(stopable=True,nameable=True)
                #self.threadCamera(self.recordVideo.{'nameable':True,'stopable':True})
            elif 'd' in command.lower():
                duration = re.search('v d(.*)',command.lower()).group(1)
                self.threadCamera = threading.Thread(target=self.actionThreadCamera,kwargs={'action':self.recordVideo,'duration':duration})
            self.threadCamera.start()
                
        elif 'stop' in command.lower():
            self.stopAllMotor()

        
            
            
        
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
    def test_connection(self):
        print('command receive')
    
        
a = Command()


