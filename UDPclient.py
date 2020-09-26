import socket

registeredID = ['admin', 'guest']
passWord = {'admin': 'admin', 'guest': 'guest'}

def login():
    id = input('ID: ')
    pw = input('PassWord: ')
    if id in registeredID:
        if pw == passWord['id']:
            return True #登录成功
    else:
        return False #用户名或密码错误

def closeSocket():
    return False

def clientUDPlink():
    if login():
        closeFlag = True    #未手动关闭
        serverName = input('ServerName: ')
        serverPort = input('ServerPort: ')
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while(closeFlag):
            data = input('Data: ')
            clientSocket.sendto(data.encode(), (serverName, serverPort))
            recvData = clientSocket.recvfrom(2048)
            print(recvData.decode())
