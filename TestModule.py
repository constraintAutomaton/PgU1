from MovementModule import Movement
import time


test = Movement()
#test.testSpeed('f',0.5)
#test.testSpeed('f',1)
#test.testSpeed('f',1.5)
#test.deleteTest('testF')
#test.showTest(test.testF)
#test.distanceApprox(98,test.testF,speedPour= 100)
#test.forward()
test.moveMotor('c','b')
test.moveMotor('d','b')
test.holdOn(1,False,0,0,None)
test.moveMotor('c','f')
test.moveMotor('d','f')
test.holdOn(1,False,0,0,None)
test.kill()




