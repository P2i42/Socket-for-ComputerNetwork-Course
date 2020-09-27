import socket, os, struct

def clientlogin(id, pw):
    registeredID = ['admin', 'guest', '1']
    passWord = {'admin': 'admin', 'guest': 'guest', '1': '1'}
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

def clientTCPlink(serverName, serverPort):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    return clientSocket

def sendText(clientSocket, text):
    # data = input('Data: ')
    clientSocket.send(text.encode())
    recvData = clientSocket.recv(1024).decode()
    return recvData
    # print(recvData)

def sendFile(clientSocket, filepath):
    fileInfoSize = struct.calcsize('128sl')
    header = struct.pack('128sl', os.path.basename(filepath).encode('utf-8'), os.stat(filepath).st_size)
    clientSocket.send(header)
    fp = open(filepath, 'rb')
    while True:
        data = fp.read(1024)
        if not data:
            print('{0} file send over...'.format(os.path.basename(filepath)))
            ACK = clientSocket.recv(1024).decode()
            print(ACK)
            return ACK
        clientSocket.send(data)
        print("sending")

