from PyQt5 import QtWidgets, QtCore, QtGui
from main import Ui_MainWindow
import socket
from TCPclientLoginUI import TCPlientLoginUIWindow
from serverUI import Ui_Server
from clientUI import Ui_client
import TCPclient
import TCPserver
import UDPclient
import UDPserver
import time

clientSocket = None  #全局变量 客户端Socket
serverSocket = None  #全局变量 服务端Socket
cnSocket = None #服务端连接Socket
serverName = None
serverPort = None
whichProtocol = ''

class mymainwindow(QtWidgets.QMainWindow, Ui_MainWindow):  #主页窗口
    def  __init__ (self):
        super(mymainwindow, self).__init__()
        self.setupUi(self)
        self.TCPbutton.clicked.connect(self.enterLoginTCP)  #TCPclient
        self.TCPbutton_2.clicked.connect(self.enterServerTCP)  #TCPserver
        self.UDPbutton.clicked.connect(self.enterLoginUDP)  #UDPclient
        self.UDPbutton_2.clicked.connect(self.enterServerUDP)  #UDPserver

    def enterLoginTCP(self):
        global whichProtocol
        whichProtocol = 'TCP'
        mytcploginwindow().loginshow()

    def enterServerTCP(self):
        global whichProtocol
        whichProtocol = 'TCP'
        myserverwindow().servershow()

    def enterLoginUDP(self):
        global whichProtocol
        whichProtocol = 'UDP'
        mytcploginwindow().loginshow()

    def enterServerUDP(self):
        global whichProtocol
        whichProtocol = 'UDP'
        myserverwindow().servershow()

class mytcploginwindow(QtWidgets.QMainWindow, TCPlientLoginUIWindow):
    def  __init__ (self):
        super(mytcploginwindow, self).__init__()
        self.setupUi(self)
        self.errMessage.setVisible(False)
        self.serverNameLabel.setVisible(False)
        self.serverPortLabel.setVisible(False)
        self.connectButton.setVisible(False)
        self.backButton.clicked.connect(self.back)
        self.loginButton.clicked.connect(self.login)    #登录
        self.connectButton.clicked.connect(self.connect)

    def loginshow(self):
        self.show()

    def back(self): # 返回主界面，原主界面未关闭，关闭本界面
        self.close()

    def login(self): # 登录
        global clientid, whichProtocol
        idText = str(self.idInput.text())
        pwText = str(self.pwInput.text())
        clientid = idText
        if whichProtocol == "TCP":
            if TCPclient.clientlogin(idText, pwText) == True:
                # 切换为连接界面
                self.idInput.clear()
                self.pwInput.clear()  #切换为服务端地址和端口号的输入框
                self.serverNameLabel.setVisible(True)
                self.serverPortLabel.setVisible(True)
                self.connectButton.setVisible(True)
                self.loginButton.setVisible(False)
                self.idLabel.setVisible(False)
                self.pwLabel.setVisible(False)
                self.errMessage.setVisible(False)

            else:
                self.errMessage.setVisible(True)
        else:
            if TCPclient.clientlogin(idText, pwText) == True:
                # 切换为连接界面
                self.idInput.clear()
                self.pwInput.clear()  # 切换为服务端地址和端口号的输入框
                self.serverNameLabel.setVisible(True)
                self.serverPortLabel.setVisible(True)
                self.connectButton.setText("确认")
                self.connectButton.setVisible(True)
                self.loginButton.setVisible(False)
                self.idLabel.setVisible(False)
                self.pwLabel.setVisible(False)
                self.errMessage.setVisible(False)

            else:
                self.errMessage.setVisible(True)

    def connect(self):
        global clientSocket, serverName, serverPort, whichProtocol
        serverName = str(self.idInput.text())
        serverPort = int(self.pwInput.text()) # 端口号是数字而非字符串
        print(serverName, serverPort)
        if whichProtocol == 'TCP':
            # clientSocket = TCPclient.clientTCPlink(serverName, serverPort, clientid)
            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            clientSocket.connect((serverName, serverPort))
            # clientSocket.send(id.encode())
            print(clientSocket)
        else:
            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        myclientwindow().clientshow()
        # self.close()


class myserverwindow(QtWidgets.QMainWindow, Ui_Server):
    def  __init__ (self):
        super(myserverwindow, self).__init__()
        self.setupUi(self)
        self.closeConnectionButton.clicked.connect(self.closeConnection)
        self.exitButton.clicked.connect(self.exit)
        self.waitConnectionButton.clicked.connect(self.waitConnection)
        self.recvTextRadioButton.setChecked(True) # 默认选择接受文本
        self.recvTextRadioButton.toggled.connect(lambda :self.btnstate(self.recvTextRadioButton))
        self.recvFileRadioButton.toggled.connect(lambda :self.btnstate(self.recvFileRadioButton))

    def servershow(self):
        self.show()
        global serverSocket, cnSocket, clientid, clientAddr, whichProtocol
        # legalAddr, serverSocket = TCPserver.listenServerTCPlink()
        serverIP = '192.168.1.105'  # 当前服务端的IP地址
        serverPort = 12000
        if whichProtocol == 'TCP':
            serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            serverSocket.bind((serverIP, serverPort))
            serverSocket.listen(1)
            self.serverInfoEdit.setText("$ 正在监听客户端发起的连接...")
            print(serverSocket)
        else:
            serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            serverSocket.bind((serverIP, serverPort))
            self.serverInfoEdit.setText("$ UDP服务端Socket已创建...")

    def waitConnection(self):
        print("waiting")
        global serverSocket, cnSocket, clientid, clientAddr
        # legalAddr, serverSocket = TCPserver.listenServerTCPlink()
        legalAddr = ['192.168.1.108',
                     '192.168.1.107',
                     '192.168.1.106',
                     '192.168.1.105',
                     '10.89.72.41']
        print(serverSocket)
        if whichProtocol == 'TCP':
            cnSocket, clientAddr = serverSocket.accept()
            print(cnSocket)
            print(clientAddr)
            if clientAddr != None and clientAddr[0] in legalAddr:
                self.userInfoEdit.setText(str('TCP客户端已连接！\n' +
                                             '客户地址：' + str(clientAddr[0])+ '\n' +
                                              '端口号：' + str(clientAddr[1])))
                # TODO 接受的是文件还是文字？
                # 通过radioButton选择
                print(self.recvFileRadioButton.isChecked())
                print(self.recvTextRadioButton.isChecked())
                if self.recvFileRadioButton.isChecked() == True: # TCP接受文件
                    TCPserver.recvFile(cnSocket)
                    newText = "\n$ 文件已接受！"
                    self.serverInfoEdit.append(newText)

                if self.recvTextRadioButton.isChecked() == True: # TCP接受文本
                    Ack = TCPserver.recvText(cnSocket)
                    print(Ack)
                    newText = "\n$ " + Ack
                    self.serverInfoEdit.append(newText)
            else:
                newText = "$ 来自非法TCP客户端的访问"
                self.serverInfoEdit.append(newText)

            cnSocket.close()
            newText = "\n$ TCP 连接Socket已关闭"
            self.serverInfoEdit.append(newText)

        else:   # UDP接受模块
            self.userInfoEdit.setText(str('上次的UDP客户端：\n' +
                                          '客户地址：' + str(clientAddr[0]) + '\n' +
                                          '端口号：' + str(clientAddr[1])))
            # 接受的是文件还是文字？ 通过radioButton选择
            print(self.recvFileRadioButton.isChecked())
            print(self.recvTextRadioButton.isChecked())
            if self.recvFileRadioButton.isChecked() == True:    # UDP接受文件
                Ack = UDPserver.recvFile(serverSocket, legalAddr)
                newText = Ack
                self.serverInfoEdit.append(newText)

            if self.recvTextRadioButton.isChecked() == True:    # UDP接受文本
                Ack = UDPserver.recvText(serverSocket, legalAddr)
                print(Ack)
                newText = "\n$ " + Ack
                self.serverInfoEdit.append(newText)



    def closeConnection(self): #TODO 关闭ServerSocket
        global serverSocket, whichProtocol
        if serverSocket != None:
            serverSocket.close()
        if whichProtocol == 'TCP':
            newText = "\n$ TCP 服务端Socket已关闭\n$ 监听已关闭"
        else:
            newText = "\n$ UDP 服务端Socket已关闭"
        self.userInfoEdit.setText(" ")
        self.serverInfoEdit.append(newText)

    def exit(self):
        global cnSocket, serverSocket # 保障全部关闭
        if cnSocket != None:
            cnSocket.close()
        if serverSocket != None:
            serverSocket.close()
        self.close()

    def btnstate(self, btn):
        print(btn.text())

class myclientwindow(QtWidgets.QMainWindow, Ui_client):
    def  __init__ (self):
        super(myclientwindow, self).__init__()
        self.setupUi(self)
        self.SendTextButton.clicked.connect(self.sendText)
        self.sendFileButton.clicked.connect(self.sendFile)
        self.exitButton.clicked.connect(self.exit)
        self.ReconnectButton.clicked.connect(self.reconnect)

    def clientshow(self):
        global whichProtocol
        self.show()
        if whichProtocol == 'TCP':
            self.serverACKEdit.setText("￥TCP 已连接服务端")
        else:
            self.ReconnectButton.setVisible(False) # UDP无需重连
            self.serverACKEdit.setText("UDP Socket准备就绪")
        self.sendTextEdit.setText('请输入要发送的文本：')

    def sendText(self): # TODO 发送文本至服务端
        global clientSocket, whichProtocol, serverPort, serverName
        text = self.sendTextEdit.toPlainText()
        if whichProtocol == 'TCP':
            recvData = TCPclient.sendText(clientSocket, text)
            self.serverACKEdit.append('￥ ' + recvData)
            self.serverACKEdit.setText("￥ TCP连接已被服务端关闭")
        else:

            recvData = UDPclient.sendText(clientSocket, text, serverPort, serverName)
            self.serverACKEdit.append('￥ ' + recvData)
            self.serverACKEdit.setText("￥ 单次UDP发送结束")

    def sendFile(self): # TODO 发送文件至服务端
        global clientSocket, whichProtocol, serverPort, serverName
        fileNamePlus = QtWidgets.QFileDialog.getOpenFileName(self, '选择文件', '')
        file = fileNamePlus[0]
        # Socket发送文件
        if whichProtocol == 'TCP':
            ACK = TCPclient.sendFile(clientSocket, file)
            self.serverACKEdit.append('￥ ' + file + ACK)
            self.serverACKEdit.setText("￥ TCP连接已被服务端关闭")
        else:
            ACK = UDPclient.sendFile(clientSocket, file, serverPort, serverName)
            self.serverACKEdit.append('￥ ' + file + ACK)
            self.serverACKEdit.setText("￥ 单次UDP发送结束")

    def reconnect(self):
        global serverName, serverPort
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        self.serverACKEdit.append('\n￥ 重新连接成功')

    def exit(self): # 关闭连接并退出
        global clientSocket
        clientSocket.close()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainui = mymainwindow()
    tcploginui = mytcploginwindow()
    serverui = myserverwindow()
    clientui = myclientwindow()
    mainui.show()
    mainui.TCPbutton.clicked.connect(tcploginui.loginshow)
    # mainui.TCPbutton_2.clicked.connect(serverui.servershow)
    mainui.UDPbutton.clicked.connect(tcploginui.loginshow)
    mainui.UDPbutton_2.clicked.connect(serverui.servershow)
    tcploginui.connectButton.clicked.connect(clientui.clientshow)
    sys.exit(app.exec_())