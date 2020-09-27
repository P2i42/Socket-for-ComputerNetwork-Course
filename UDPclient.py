import socket, os, struct

def clientlogin(id, pw):
    registeredID = ['admin', 'guest', '1']
    passWord = {'admin': 'admin', 'guest': 'guest', '1': '1'}
    clientId = id
    if clientId in registeredID:
        if pw == passWord[clientId]:
            return True #登录成功
        else:
            return False  # 用户名或密码错误
    else:
        return False #用户名或密码错误

def closeSocket():
    return False

def sendText(clientSocket, text, serverPort, serverName):
    clientSocket.sendto(text.encode(), (serverName, serverPort))
    recvData = "{ " + text + "}" + "已发送"
    return recvData

def sendFile(clientSocket, filepath, serverPort, serverName):
    server = (serverName, serverPort)
    fileInfoSize = struct.calcsize('128sl')
    header = struct.pack('128sl', os.path.basename(filepath).encode('utf-8'), os.stat(filepath).st_size)
    clientSocket.sendto(header, server)
    fp = open(filepath, 'rb')
    while True:
        data = fp.read(1024)
        if not data:
            print('{0} file send over...'.format(os.path.basename(filepath)))
            ACK = " 已发送"
            return ACK
        clientSocket.sendto(data, server)
        print('sending')



