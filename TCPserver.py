import socket, struct

# 判断用户身份是否合法为合法用户 echo 数据
# legalAddr = ['192.168.1.107']

def listenServerTCPlink():
    legalAddr = ['192.168.1.108',
                 '192.168.1.107',
                 '192.168.1.106',
                 '192.168.1.105',
                 '10.89.72.41']
    serverIP = '192.168.1.106' # 当前服务端的IP地址
    serverPort = 12000
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((serverIP, serverPort))
    serverSocket.listen(1)
    return legalAddr, serverSocket

def recvFile(cnSocket):
    while True:
        fileInfoSize = struct.calcsize('128sl')
        fileHeaderRecv = cnSocket.recv(fileInfoSize)
        filename = ''
        if fileHeaderRecv:
            fileName, fileSize = struct.unpack('128sl', fileHeaderRecv)
            fn = fileName.strip(b'\00')
            fn = fn.decode()
            filename = str(fn)
            recvdSize = 0
            fp = open('./' + str(fn), 'wb')
            while not recvdSize == fileSize:    #循环接受文件数据
                if fileSize - recvdSize > 1024:
                    data = cnSocket.recv(1024)
                    recvdSize += len(data)
                else:
                    data = cnSocket.recv(fileSize - recvdSize)
                    recvdSize = fileSize
                fp.write(data)
            fp.close()
        Ack = filename + ' 文件接收成功！'
        cnSocket.send(Ack.encode())
        cnSocket.close()
        break

def recvText(cnSocket):
    recvData = cnSocket.recv(1024).decode()
    Ack = '{ ' + recvData + ' } ' + '接受成功!'
    cnSocket.send(Ack.encode())
    return Ack

