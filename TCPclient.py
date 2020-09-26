import socket, os, struct

registeredID = ['admin', 'guest']
passWord = {'admin': 'admin', 'guest': 'guest'}
clientId = ''

def clientlogin(id, pw):
    registeredID = ['admin', 'guest']
    passWord = {'admin': 'admin', 'guest': 'guest'}
    # clientId = ''
    # id = input('ID: ')
    clientId = id
    # pw = input('PassWord: ')
    if clientId in registeredID:
        if pw == passWord[clientId]:
            return True #登录成功
        else:
            return False  # 用户名或密码错误
    else:
        return False #用户名或密码错误


def closeSocket():
    return False

def clientTCPlink(serverName, serverPort, id):
    # closeFlag = True    #未手动关闭
    # serverName = input('ServerName: ')
    # serverPort = input('ServerPort: ')
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    clientSocket.send(id.encode())
    return clientSocket

def sendText(clientSocket, text):
    # data = input('Data: ')
    clientSocket.send(text.encode())
    recvData = clientSocket.recv(1024)
    return recvData
    # print(recvData)

def sendFile(clientSocket, filepath):
    fileinfo_size = struct.calcsize('128sl')
    fhead = struct.pack('128sl', os.path.basename(filepath).encode('utf-8'), os.stat(filepath).st_size)
    clientSocket.send(fhead)
    fp = open(filepath, 'rb')
    while True:
        data = fp.read(1024)
        if not data:
            print('{0} file send over...'.format(os.path.basename(filepath)))
            break
        clientSocket.send(data)
    ACK = clientSocket.recv(1024).decode()
    return ACK


# def clientTCPlink():
#     if clientlogin():
#         closeFlag = True    #未手动关闭
#         serverName = input('ServerName: ')
#         serverPort = input('ServerPort: ')
#         clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         clientSocket.connect((serverName, serverPort))
#         while(closeFlag):
#             data = input('Data: ')
#             clientSocket.send(data.encode())
#             recvData = clientSocket.recv(1024)
#             print(recvData)

# print(clientlogin('admin', 'admin'))