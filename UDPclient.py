import socket, os, struct

registeredID = ['admin', 'guest', '1']
passWord = {'admin': 'admin', 'guest': 'guest', '1': '1'}
clientId = ''

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

def sendText(clientSocket, text, serverPort, serverName):
    clientSocket.sendto(text.encode(), (serverName, serverPort))
    print('send already')
    # recvData = clientSocket.recvfrom(2048)
    recvData = "{ " + text + "}" + "已发送"
    return recvData

def sendFile(clientSocket, filepath, serverPort, serverName):
    server = (serverName, serverPort)
    fileinfo_size = struct.calcsize('128sl')
    fhead = struct.pack('128sl', os.path.basename(filepath).encode('utf-8'), os.stat(filepath).st_size)
    clientSocket.sendto(fhead, server)
    fp = open(filepath, 'rb')
    while True:
        data = fp.read(1024)
        if not data:
            print('{0} file send over...'.format(os.path.basename(filepath)))
            ACK = " 已发送"
            return ACK
        clientSocket.sendto(data, server)
        print('sending')
    # ACK = clientSocket.recv(1024).decode()



# def clientUDPlink():
#     if login():
#         closeFlag = True    #未手动关闭
#         serverName = input('ServerName: ')
#         serverPort = input('ServerPort: ')
#         clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         while(closeFlag):
#             data = input('Data: ')
#             clientSocket.sendto(data.encode(), (serverName, serverPort))
#             recvData = clientSocket.recvfrom(2048)
#             print(recvData.decode())


