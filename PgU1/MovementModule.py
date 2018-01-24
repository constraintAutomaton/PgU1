import RPi.GPIO as gpio
import time
import os
import pickle


class Movement():
    def __init__(self,regtime = 1, frequency = 100, maxSpeed=1, startPourSpeed = 100):
        
        gpio.setmode(gpio.BCM)
        with open(r'/home/pi/python_project/PgU1/PgU1/pin_mapping/wheel_motor','r') as file:
            for line in file:
                if 'motorCb' in line:
                    self.motorCb = int(line[8:])
                elif 'motorCf' in line:
                    self.motorCf = int(line[8:])
                elif 'motorBf' in line:
                    self.motorBf = int(line[8:])
                elif 'motorDb' in line:
                    self.motorDb = int(line[8:])
                elif 'motorDf' in line:
                    self.motorDf = int(line[8:])
                elif 'motorBb' in line:
                    self.motorBb = int(line[8:])
                elif 'motorAb' in line:
                    self.motorAb = int(line[8:])
                elif 'motorAf' in line:
                    self.motorAf = int(line[8:])

        self.frequency = frequency
        self.regTime = regtime
        self.maxSpeed = maxSpeed
        self.startPourSpeed = startPourSpeed
        self.listMotor = [self.motorAf,self.motorAb,self.motorBf,self.motorBb,self.motorCf,
                          self.motorCb,self.motorDf,self.motorDb]
        
        self.initGpio()
        
        self.initTestFileLocation()
        
    def initGpio(self): 
    
        gpio.setup(self.motorCb, gpio.OUT)
        gpio.setup(self.motorCf, gpio.OUT)
        gpio.setup(self.motorAb, gpio.OUT)
        gpio.setup(self.motorAf, gpio.OUT)
        gpio.setup(self.motorBf, gpio.OUT)
        gpio.setup(self.motorDb, gpio.OUT)
        gpio.setup(self.motorDf, gpio.OUT)
        gpio.setup(self.motorBb, gpio.OUT)

    def initPwm(self):
        
        self.motorCbP = gpio.PWM(self.motorCb,self.frequency)
        self.motorCfP = gpio.PWM(self.motorCf,self.frequency)
        self.motorBfP = gpio.PWM(self.motorBf,self.frequency)
        self.motorDbP = gpio.PWM(self.motorDb,self.frequency)
        self.motorDfP = gpio.PWM(self.motorDf,self.frequency)
        self.motorBbP = gpio.PWM(self.motorBb,self.frequency)
        self.motorAbP = gpio.PWM(self.motorAb,self.frequency)
        self.motorAfP = gpio.PWM(self.motorAf,self.frequency)

        self.listPWM = [self.motorCbP, self.motorCfP, self.motorBfP, self.motorDbP,
                        self.motorDfP, self.motorBbP, self.motorAbP, self.motorAfP]
        for PWM in self.listPWM: 
           PWM.start(0)
           
    def initTestFileLocation(self):
        self.testF = r'/home/pi/python_project/PgU1/PgU1/speed_test/speed_test/testF.pickle'
        self.testB = r'/home/pi/python_project/PgU1/PgU1/speed_test/speed_test/testB.pickle'
        self.testTrf = r'/home/pi/python_project/PgU1/PgU1/speed_test/speed_test/testTrf.pickle'
        self.testTrb = r'/home/pi/python_project/PgU1/PgU1/speed_test/speed_test/testTrb.pickle'
        self.testTlf = r'/home/pi/python_project/PgU1/PgU1/speed_test/speed_test/testTlf.pickle'
        self.testTlb = r'/home/pi/python_project/PgU1/PgU1/speed_test/speed_test/testTlb.pickle'
        
    def holdOn(self,duration,stopable,distance,angle,testFile):

        if stopable:
            input('press enter to stop')
                
        elif duration>0:
            time.sleep(duration)
            
        elif distance>0:
            time.sleep(self.distanceApprox(distance,testFile))
        elif angle>0:
            time.sleep(self.distanceApprox(angle,testFile))
        else:
            
            time.sleep(self.regTime)
            
        self.listMotor = [self.motorAf,self.motorAb,self.motorBf,self.motorBb,self.motorCf, 
                          self.motorCb,self.motorDf,self.motorDb]
        for motor in self.listMotor:
            gpio.output(motor,False) 
                
    def moveMotor(self,motor,direction):

        gpioMotorDir = getattr(self,'motor{}{}'.format(motor.upper(),direction))
        gpio.output(gpioMotorDir, True)
        
        
    def forward(self,duration=0,stopable=False,distance=0,angle=0):
        self.moveMotor('a','f')
        self.moveMotor('b','f')
        self.moveMotor('c','f')
        self.moveMotor('d','f')
        
        self.holdOn(duration,stopable,distance,angle,self.testF)
        
    def backward(self,duration=0,stopable=False,distance=0,angle=0):
        self.moveMotor('a','b')
        self.moveMotor('b','b')
        self.moveMotor('c','b')
        self.moveMotor('d','b')

        self.holdOn(duration,stopable,distance,angle,self.testB)

    def turnRF(self,duration=0,stopable=False,distance=0,angle=0):
        self.moveMotor('a','f')
        self.moveMotor('b','f')

        self.holdOn(duration,stopable,distance,angle,self.testTrf)

    def turnRB(self,duration=0,stopable=False,distance=0,angle=0):
        self.moveMotor('a','b')
        self.moveMotor('b','b')

        self.holdOn(duration,stopable,distance,angle,self.testTrb)

    def turnLF(self,duration=0,stopable=False,distance=0,angle=0):
        self.moveMotor('c','f')
        self.moveMotor('d','f')

        self.holdOn(duration,stopable,distance,angle,self.testTlf)

    def turnLB(self,duration=0,stopable=False,distance=0,angle=0):
        self.moveMotor('c','b')
        self.moveMotor('d','b')

        self.holdOn(duration,stopable,distance,angle,self.testTlb)

    def stopAllMotor(self):
        for motor in self.listMotor:
            gpio.output(motor,False)
        

    def changeSpeed(self,speed=0,speedPour=0):
        for motor in self.listPWM:
            motor.ChangeDutyCycle(speedPour)

    def kill(self):
        gpio.cleanup()
        
    def distanceApprox(self,distance,typeFile,speedPour=100):
        
        k = 0
        ya = 0
        xa = 0
        try:
            for y, x in self.openTest(typeFile).items():
                xa += x
                ya += y
            
            a = ya/xa
            
            duration = a*distance*(speedPour/100)+k

            

            return duration
        except:
            print('The test file don\'t exist. make some speed test before using the distance mode')
            return 0     
      
    def testSpeed(self,typeMvt,duration):
        
        
        if typeMvt == 'f':
            self.forward(duration=duration)
            typeFile = self.testF
        elif typeMvt == 'b':
            self.backward(duration=duration)
            typeFile = self.test
        elif typeMvt == 'trf':
            self.turnRF(duration=duration)
            typeFile = self.testTrf
        elif typeMvt == 'trb':
            self.turnRB(duration=duration)
            typeFile = self.testTrb
        elif typeMvt == 'tlf':
            self.turnLF(duration=duration)
            typeFile = self.testTlf
        elif typeMvt == 'tlb':
            self.turnLB(duration=duration)
            typeFile = self.testTlb

        distance = input('set the distance travel: ')
        
        data = (duration, float(distance))
        self.saveTest(typeFile, data)
        
    def saveTest(self, typeFile , data):
        
        try:
            with open('{}'.format(typeFile),'rb') as handle:
                test = pickle.load(handle)
                test[data[0]] = data[1]             
                
            with open('{}'.format(typeFile),'wb') as handle:
                pickle.dump(test, handle, protocol=pickle.HIGHEST_PROTOCOL)
                               
            
        except:
            with open('{}'.format(typeFile),'wb') as handle:
                test = {data[0]:data[1]}
                pickle.dump(test, handle, protocol=pickle.HIGHEST_PROTOCOL)
                
    def showTest(self, typeFile):
        try:
            with open('{}'.format(typeFile),'rb') as handle:
                    test = pickle.load(handle)
                    print(test)
        except:
            print('The file don\'t exist')
            self.kill()
    def deleteTest(self, typeFile):
        try:
            os.remove('{}'.format(typeFile))
        except:
            print('The file don\'t exist')
            self.kill()
        
    def openTest(self, typeFile):
        try:
            with open('{}'.format(typeFile),'rb') as handle:
                    test = pickle.load(handle)
            return test
        except:
            print('The file don\'t exist')
            self.kill()
            
            
        
            


         

