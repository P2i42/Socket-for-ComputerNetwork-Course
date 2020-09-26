# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Server(object):
    def setupUi(self, Server):
        Server.setObjectName("Server")
        Server.resize(633, 496)
        self.closeConnectionButton = QtWidgets.QPushButton(Server)
        self.closeConnectionButton.setGeometry(QtCore.QRect(500, 260, 121, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(17)
        self.closeConnectionButton.setFont(font)
        self.closeConnectionButton.setObjectName("closeConnectionButton")
        self.exitButton = QtWidgets.QPushButton(Server)
        self.exitButton.setGeometry(QtCore.QRect(430, 410, 121, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(17)
        self.exitButton.setFont(font)
        self.exitButton.setObjectName("exitButton")
        self.serverInfoLabel = QtWidgets.QLabel(Server)
        self.serverInfoLabel.setGeometry(QtCore.QRect(30, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.serverInfoLabel.setFont(font)
        self.serverInfoLabel.setObjectName("serverInfoLabel")
        self.userInfoLabel = QtWidgets.QLabel(Server)
        self.userInfoLabel.setGeometry(QtCore.QRect(360, 10, 141, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.userInfoLabel.setFont(font)
        self.userInfoLabel.setObjectName("userInfoLabel")
        self.waitConnectionButton = QtWidgets.QPushButton(Server)
        self.waitConnectionButton.setGeometry(QtCore.QRect(360, 260, 121, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(17)
        self.waitConnectionButton.setFont(font)
        self.waitConnectionButton.setObjectName("waitConnectionButton")
        self.recvFileRadioButton = QtWidgets.QRadioButton(Server)
        self.recvFileRadioButton.setGeometry(QtCore.QRect(360, 340, 121, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(17)
        self.recvFileRadioButton.setFont(font)
        self.recvFileRadioButton.setObjectName("recvFileRadioButton")
        self.recvTextRadioButton = QtWidgets.QRadioButton(Server)
        self.recvTextRadioButton.setGeometry(QtCore.QRect(500, 340, 111, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(17)
        self.recvTextRadioButton.setFont(font)
        self.recvTextRadioButton.setObjectName("recvTextRadioButton")
        self.userInfoEdit = QtWidgets.QTextEdit(Server)
        self.userInfoEdit.setGeometry(QtCore.QRect(360, 50, 261, 191))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.userInfoEdit.setFont(font)
        self.userInfoEdit.setObjectName("userInfoEdit")
        self.serverInfoEdit = QtWidgets.QTextEdit(Server)
        self.serverInfoEdit.setGeometry(QtCore.QRect(30, 50, 311, 421))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.serverInfoEdit.setFont(font)
        self.serverInfoEdit.setObjectName("serverInfoEdit")

        self.retranslateUi(Server)
        QtCore.QMetaObject.connectSlotsByName(Server)

    def retranslateUi(self, Server):
        _translate = QtCore.QCoreApplication.translate
        Server.setWindowTitle(_translate("Server", "服务端"))
        self.closeConnectionButton.setText(_translate("Server", "关闭连接"))
        self.exitButton.setText(_translate("Server", "退出"))
        self.serverInfoLabel.setText(_translate("Server", "服务器状态信息"))
        self.userInfoLabel.setText(_translate("Server", "用户登录信息"))
        self.waitConnectionButton.setText(_translate("Server", "接受信息"))
        self.recvFileRadioButton.setText(_translate("Server", "接收文件"))
        self.recvTextRadioButton.setText(_translate("Server", "接收文字"))
        self.userInfoEdit.setHtml(_translate("Server", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p></body></html>"))
