# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\HP\Google_Drive\Personnel\Python\Projet\Gui_OmxPlayer\OmxPlayer.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(615, 497)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblHere = QtGui.QLabel(self.centralwidget)
        self.lblHere.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHere.setObjectName(_fromUtf8("lblHere"))
        self.verticalLayout.addWidget(self.lblHere)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lblTimeElapse = QtGui.QLabel(self.frame)
        self.lblTimeElapse.setObjectName(_fromUtf8("lblTimeElapse"))
        self.horizontalLayout_2.addWidget(self.lblTimeElapse)
        self.hSliderTime = QtGui.QSlider(self.frame)
        self.hSliderTime.setOrientation(QtCore.Qt.Horizontal)
        self.hSliderTime.setObjectName(_fromUtf8("hSliderTime"))
        self.horizontalLayout_2.addWidget(self.hSliderTime)
        self.lblTimeLeft = QtGui.QLabel(self.frame)
        self.lblTimeLeft.setObjectName(_fromUtf8("lblTimeLeft"))
        self.horizontalLayout_2.addWidget(self.lblTimeLeft)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnPlay = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPlay.sizePolicy().hasHeightForWidth())
        self.btnPlay.setSizePolicy(sizePolicy)
        self.btnPlay.setObjectName(_fromUtf8("btnPlay"))
        self.horizontalLayout.addWidget(self.btnPlay)
        self.btnPause = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPause.sizePolicy().hasHeightForWidth())
        self.btnPause.setSizePolicy(sizePolicy)
        self.btnPause.setObjectName(_fromUtf8("btnPause"))
        self.horizontalLayout.addWidget(self.btnPause)
        self.btnFullScreen = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnFullScreen.sizePolicy().hasHeightForWidth())
        self.btnFullScreen.setSizePolicy(sizePolicy)
        self.btnFullScreen.setObjectName(_fromUtf8("btnFullScreen"))
        self.horizontalLayout.addWidget(self.btnFullScreen)
        self.hSliderVolume = QtGui.QSlider(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hSliderVolume.sizePolicy().hasHeightForWidth())
        self.hSliderVolume.setSizePolicy(sizePolicy)
        self.hSliderVolume.setMaximum(100)
        self.hSliderVolume.setOrientation(QtCore.Qt.Horizontal)
        self.hSliderVolume.setObjectName(_fromUtf8("hSliderVolume"))
        self.horizontalLayout.addWidget(self.hSliderVolume)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 615, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.menuFile.addAction(self.actionOpen)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.lblHere.setText(_translate("MainWindow", "HERE", None))
        self.lblTimeElapse.setText(_translate("MainWindow", "00:00", None))
        self.lblTimeLeft.setText(_translate("MainWindow", "00:00", None))
        self.btnPlay.setText(_translate("MainWindow", "PLAY", None))
        self.btnPause.setText(_translate("MainWindow", "PAUSE", None))
        self.btnFullScreen.setText(_translate("MainWindow", "FULLSCREEN", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

