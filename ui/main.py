# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\NetEase\Documents\workspace\MusicPlayer\src\ui\main.ui'
#
# Created: Mon Dec 02 20:14:11 2013
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        MainWidget.setObjectName(_fromUtf8("MainWidget"))
        MainWidget.setWindowModality(QtCore.Qt.NonModal)
        MainWidget.resize(300, 405)
        MainWidget.setWindowTitle(_fromUtf8(""))
        MainWidget.setAutoFillBackground(True)
        self.header = QtGui.QWidget(MainWidget)
        self.header.setGeometry(QtCore.QRect(0, 0, 300, 30))
        self.header.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255)"))
        self.header.setObjectName(_fromUtf8("header"))
        self.btnClose = QtGui.QPushButton(self.header)
        self.btnClose.setGeometry(QtCore.QRect(280, 7, 16, 16))
        self.btnClose.setAutoFillBackground(False)
        self.btnClose.setStyleSheet(_fromUtf8("background: url(:/button/close) no-repeat;border:none"))
        self.btnClose.setText(_fromUtf8(""))
        self.btnClose.setObjectName(_fromUtf8("btnClose"))
        self.btnMenu = QtGui.QPushButton(self.header)
        self.btnMenu.setGeometry(QtCore.QRect(0, 0, 131, 31))
        self.btnMenu.setAutoFillBackground(False)
        self.btnMenu.setStyleSheet(_fromUtf8("background: url(:/button/title.jpg) no-repeat;border:none"))
        self.btnMenu.setText(_fromUtf8(""))
        self.btnMenu.setIconSize(QtCore.QSize(20, 20))
        self.btnMenu.setObjectName(_fromUtf8("btnMenu"))
        self.listSongs = QtGui.QListWidget(MainWidget)
        self.listSongs.setGeometry(QtCore.QRect(5, 145, 290, 225))
        self.listSongs.setObjectName(_fromUtf8("listSongs"))
        self.middle = QtGui.QWidget(MainWidget)
        self.middle.setGeometry(QtCore.QRect(0, 30, 300, 110))
        self.middle.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255)"))
        self.middle.setObjectName(_fromUtf8("middle"))
        self.cover = QtGui.QWidget(self.middle)
        self.cover.setGeometry(QtCore.QRect(10, 5, 100, 100))
        self.cover.setStyleSheet(_fromUtf8("background:url(:/logo/logo.png)"))
        self.cover.setObjectName(_fromUtf8("cover"))
        self.labelName = QtGui.QLabel(self.middle)
        self.labelName.setGeometry(QtCore.QRect(120, 10, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelName.setFont(font)
        self.labelName.setStyleSheet(_fromUtf8(""))
        self.labelName.setObjectName(_fromUtf8("labelName"))
        self.author = QtGui.QLabel(self.middle)
        self.author.setGeometry(QtCore.QRect(120, 31, 171, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(237, 131, 53))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(237, 131, 53))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.author.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.author.setFont(font)
        self.author.setTextFormat(QtCore.Qt.RichText)
        self.author.setObjectName(_fromUtf8("author"))
        self.btnStart = QtGui.QPushButton(self.middle)
        self.btnStart.setGeometry(QtCore.QRect(180, 70, 20, 15))
        self.btnStart.setStyleSheet(_fromUtf8("QPushButton#btnStart {border:none;background: url(:/button/btnStart.jpg);}"))
        self.btnStart.setText(_fromUtf8(""))
        self.btnStart.setObjectName(_fromUtf8("btnStart"))
        self.btnPrev = QtGui.QPushButton(self.middle)
        self.btnPrev.setGeometry(QtCore.QRect(153, 70, 20, 15))
        self.btnPrev.setAutoFillBackground(False)
        self.btnPrev.setStyleSheet(_fromUtf8("QPushButton#btnPrev {border:none;background: url(:/button/btnRewind.jpg);}\n"
""))
        self.btnPrev.setText(_fromUtf8(""))
        self.btnPrev.setObjectName(_fromUtf8("btnPrev"))
        self.btnNext = QtGui.QPushButton(self.middle)
        self.btnNext.setGeometry(QtCore.QRect(238, 70, 20, 15))
        self.btnNext.setStyleSheet(_fromUtf8("QPushButton#btnNext {border:none;background: url(:/button/btnForward.jpg);}"))
        self.btnNext.setText(_fromUtf8(""))
        self.btnNext.setObjectName(_fromUtf8("btnNext"))
        self.btnReset = QtGui.QPushButton(self.middle)
        self.btnReset.setGeometry(QtCore.QRect(210, 70, 20, 15))
        self.btnReset.setStyleSheet(_fromUtf8("QPushButton#btnReset {border:none;background: url(:/button/btnReset.jpg);}"))
        self.btnReset.setText(_fromUtf8(""))
        self.btnReset.setObjectName(_fromUtf8("btnReset"))
        self.consumeTime = QtGui.QLabel(self.middle)
        self.consumeTime.setGeometry(QtCore.QRect(118, 70, 31, 16))
        self.consumeTime.setObjectName(_fromUtf8("consumeTime"))
        self.totalTime = QtGui.QLabel(self.middle)
        self.totalTime.setGeometry(QtCore.QRect(264, 70, 30, 15))
        self.totalTime.setObjectName(_fromUtf8("totalTime"))
        self.seekSlider = phonon.Phonon.SeekSlider(self.middle)
        self.seekSlider = phonon.Phonon.SeekSlider(self.middle)
        self.seekSlider.setGeometry(QtCore.QRect(120, 90, 171, 19))
        self.seekSlider.setObjectName(_fromUtf8("seekSlider"))
        self.seperator1 = QtGui.QWidget(MainWidget)
        self.seperator1.setGeometry(QtCore.QRect(0, 30, 300, 1))
        self.seperator1.setStyleSheet(_fromUtf8("background:rgb(234,234,234)"))
        self.seperator1.setObjectName(_fromUtf8("seperator1"))
        self.footer = QtGui.QWidget(MainWidget)
        self.footer.setGeometry(QtCore.QRect(0, 370, 300, 35))
        self.footer.setStyleSheet(_fromUtf8("background: url(:/background/footerBg.jpg);"))
        self.footer.setObjectName(_fromUtf8("footer"))
        self.btnRepeat = QtGui.QPushButton(self.footer)
        self.btnRepeat.setGeometry(QtCore.QRect(260, 5, 40, 25))
        self.btnRepeat.setStyleSheet(_fromUtf8("QPushButton#btnRepeat {border:none;background: url(:/button/btnRepeat.jpg) no-repeat;}"))
        self.btnRepeat.setText(_fromUtf8(""))
        self.btnRepeat.setIconSize(QtCore.QSize(18, 18))
        self.btnRepeat.setObjectName(_fromUtf8("btnRepeat"))
        self.btnShuffle = QtGui.QPushButton(self.footer)
        self.btnShuffle.setGeometry(QtCore.QRect(220, 5, 40, 25))
        self.btnShuffle.setStyleSheet(_fromUtf8("QPushButton#btnShuffle {border:none;background: url(:/button/btnShuffle.jpg) no-repeat;}"))
        self.btnShuffle.setText(_fromUtf8(""))
        self.btnShuffle.setObjectName(_fromUtf8("btnShuffle"))
        self.btnAdd = QtGui.QPushButton(self.footer)
        self.btnAdd.setGeometry(QtCore.QRect(160, 7, 21, 25))
        self.btnAdd.setStyleSheet(_fromUtf8("QPushButton#btnAdd {border:none;background: url(:/button/btnAdd.jpg) no-repeat;}"))
        self.btnAdd.setText(_fromUtf8(""))
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.btnDel = QtGui.QPushButton(self.footer)
        self.btnDel.setGeometry(QtCore.QRect(190, 7, 21, 25))
        self.btnDel.setStyleSheet(_fromUtf8("QPushButton#btnDel {border:none;background: url(:/button/btnDel.jpg) no-repeat;}"))
        self.btnDel.setText(_fromUtf8(""))
        self.btnDel.setObjectName(_fromUtf8("btnDel"))
        self.volumeSlider = phonon.Phonon.VolumeSlider(self.footer)
        self.volumeSlider.setGeometry(QtCore.QRect(10, 10, 141, 22))
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))

        self.retranslateUi(MainWidget)
        QtCore.QMetaObject.connectSlotsByName(MainWidget)

    def retranslateUi(self, MainWidget):
        self.labelName.setText(_translate("MainWidget", "PLAYER", None))
        self.author.setText(_translate("MainWidget", "capsule", None))
        self.consumeTime.setText(_translate("MainWidget", "00:00", None))
        self.totalTime.setText(_translate("MainWidget", "00:00", None))

from PyQt4 import phonon
import assets_rc
