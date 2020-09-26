# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tcpudp.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(407, 458)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 30, 341, 381))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(23)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.TCPbutton = QtWidgets.QPushButton(self.widget)
        self.TCPbutton.setMaximumSize(QtCore.QSize(231, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.TCPbutton.setFont(font)
        self.TCPbutton.setIconSize(QtCore.QSize(18, 18))
        self.TCPbutton.setObjectName("TCPbutton")
        self.gridLayout.addWidget(self.TCPbutton, 1, 0, 1, 1)
        self.UDPbutton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.UDPbutton.setFont(font)
        self.UDPbutton.setObjectName("UDPbutton")
        self.gridLayout.addWidget(self.UDPbutton, 2, 0, 1, 1)
        self.TCPbutton_2 = QtWidgets.QPushButton(self.widget)
        self.TCPbutton_2.setMaximumSize(QtCore.QSize(231, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.TCPbutton_2.setFont(font)
        self.TCPbutton_2.setIconSize(QtCore.QSize(18, 18))
        self.TCPbutton_2.setObjectName("TCPbutton_2")
        self.gridLayout.addWidget(self.TCPbutton_2, 3, 0, 1, 1)
        self.UDPbutton_2 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.UDPbutton_2.setFont(font)
        self.UDPbutton_2.setObjectName("UDPbutton_2")
        self.gridLayout.addWidget(self.UDPbutton_2, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Socket"))
        self.label.setText(_translate("MainWindow", "Socket通信实验"))
        self.TCPbutton.setText(_translate("MainWindow", "TCPclient"))
        self.UDPbutton.setText(_translate("MainWindow", "UDPclient"))
        self.TCPbutton_2.setText(_translate("MainWindow", "TCPserver"))
        self.UDPbutton_2.setText(_translate("MainWindow", "UDPserver"))
