from MovementModule import Movement
import time


test = Movement()
#test.testSpeed('f',0.5)
#test.testSpeed('f',1)
#test.testSpeed('f',1.5)
#test.deleteTest('testF')
test.showTest(test.testF)
test.distanceApprox(98,test.testF,speedPour= 100)

test.kill()




