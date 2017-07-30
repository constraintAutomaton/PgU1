from PyQt4 import QtGui
import sys
import pexpect
from threading import Thread
from PyQt4.QtGui import QSound
import OmxPlayer

class OmxPlayer(QtGui.QMainWindow, OmxPlayer.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        
        self.btnPlay.clicked.connect(self.play)
        self.btnPause.clicked.connect(self.pause)
        self.command()
        
        
    def command(self):
        self.cRewind = '<'
        self.cFoward = '>'
        self.cQuit = 'q'
        self.cPause = 'p'
        self.cDvolume = '-'
        self.cIvolume = '+'
        self.cSeekm30 = '\027[D'
        self.cSeekp30 = '\027[C'
        self.cSeekm600 = '\027[B'
        self.cSeekp600 = '\027[A'
    
    def moveWindow(self,x1,y1,x2,y2):
        return '--win {},{},{},{}'.format(x1,y1,x2,y2)
        
    def play(self):
        x1 = self.lblHere.x() + self.centralwidget.x()
        y1 = self.lblHere.y() + self.centralwidget.y()
        x2 = self.lblHere.width()
        y2 = self.lblHere.height()
        print(x1,y1,x2,y2)
        path = '/home/pi/Documents/Python_project/PgU1_code/Video/test___2017-07-24___18:35:38.h264'
        self.omx = pexpect.spawn('omxplayer {} {}'.format(self.moveWindow(x1,y1,x2,y2), path))
        
        
        
    def pause(self):
        self.omx.send(self.cPause)
        
    def foward(self):
        self.omx.send(self.cFoward)
        

        
    def closeEvent(self,event):
        self.omx.send(self.cQuit)
        event.accept()


def main():
    app = QtGui.QApplication(sys.argv)
    form = OmxPlayer()
    form.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main() 