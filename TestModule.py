import pexpect
import time
path = '/home/pi/Documents/Python_project/PgU1_code/Video/test___2017-07-24___18:35:38.h264'
child = pexpect.spawn('omxplayer --win "0 0 640 480" {}'.format(path))
time.sleep(2)
child.send('p')
time.sleep(2)
child.send('q')
#print(child)
