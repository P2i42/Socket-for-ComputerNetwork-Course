import socket, struct, os

# 判断用户身份是否合法为合法用户 echo 数据
legalAddr = ['192.168.1.107']


def serverUDPCreate():
    legalAddr = ['192.168.1.108',
                 '192.168.1.107',
                 '192.168.1.106',
                 '192.168.1.105',
                 '10.89.72.41']
    serverIP = '192.168.1.106'  # 当前服务端的IP地址
    serverPort = 12000
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind((serverIP, serverPort))
    return legalAddr, serverSocket


def recvText(serverSocket, legalAddr):
    recvData, clientAddr = serverSocket.recvfrom(2048)
    if clientAddr != None and clientAddr[0] in legalAddr:
        Ack = '{ ' + recvData.decode() + ' } ' + '接受成功'
        return Ack, clientAddr
    else:
        Ack = "来自非法UDP客户端的访问"
        clientAddr = ('******', '******')
        return Ack, clientAddr

def recvFile(serverSocket, legalAddr):
    while True:
        fileInfoSize = struct.calcsize('128sl')
        fileHeaderRecv, clientAddr = serverSocket.recvfrom(fileInfoSize)
        filename = ''
        if clientAddr != None and clientAddr[0] in legalAddr:
            if fileHeaderRecv: #确保收到了头文件
                fileName, fileSize = struct.unpack('128sl', fileHeaderRecv)
                fn = fileName.strip(b'\00')
                fn = fn.decode()
                filename = str(fn)
                recvSize = 0  # 定义已接收文件的大小
                fp = open('./' + str(fn), 'wb')
                while not recvSize == fileSize:
                    if fileSize - recvSize > 1024:
                        data = serverSocket.recvfrom(1024)
                        recvSize += 1024
                    else:
                        data = serverSocket.recvfrom(fileSize - recvSize)
                        recvSize = fileSize
                    fp.write(data[0])
                fp.close()
                print('end receive...')
            Ack = "\n$ " + filename + "文件已接受！"
            return Ack, clientAddr
        else: # 若客户端地址非法
            Ack = "\n$ 来自非法UDP客户端的访问"
            clientAddr = ('******', '******')
            return Ack, clientAddr




