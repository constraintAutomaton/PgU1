import subprocess

class OmxPlayer():
    def __init__(self):
        print('allo')
    def playVideo(self, path):
        subprocess.Popen('omxplayer --win "0 0 640 480" {}'.format(path),shell = True)
path = r'/home/pi/Documents/Python_project/PgU1_code/Video/2017-07-18___11:43:36.h264'
omx = OmxPlayer()
omx.playVideo(path)