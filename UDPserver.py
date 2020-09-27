import socket, struct, os

# TODO  判断用户身份是否合法为合法用户 echo 数据
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
    while (True):
        recvData, clientAddr = serverSocket.recvfrom(2048)
        if clientAddr != None and clientAddr[0] in legalAddr:
            Ack = '{ ' + recvData.decode() + ' } ' + '接受成功'
            serverSocket.sendto(Ack.encode(), clientAddr)
            return Ack
        else:
            Ack = "来自非法UDP客户端的访问"
            return Ack

def recvFile(serverSocket, legalAddr):
    while True:
        # 申请相同大小的空间存放发送过来的文件名与文件大小信息
        fileinfo_size = struct.calcsize('128sl')
        # 接收文件名与文件大小信息
        buf, clientAddr = serverSocket.recvfrom(fileinfo_size)
        if clientAddr != None and clientAddr[0] in legalAddr:
            # 判断是否接收到文件头信息
            if buf:
                # 获取文件名和文件大小
                filename, filesize = struct.unpack('128sl', buf)
                fn = filename.strip(b'\00')
                fn = fn.decode()
                print('file new name is {0}, filesize if {1}'.format(str(fn), filesize))

                recvd_size = 0  # 定义已接收文件的大小
                # 存储在该脚本所在目录下面
                fp = open('./' + str(fn), 'wb')
                print('start receiving...')

                # 将分批次传输的二进制流依次写入到文件
                while not recvd_size == filesize:
                    if filesize - recvd_size > 1024:
                        data = serverSocket.recvfrom(1024)
                        recvd_size += len(data)
                    else:
                        data = serverSocket.recvfrom(filesize - recvd_size)
                        recvd_size = filesize
                    fp.write(data)
                fp.close()
                print('end receive...')
            # 传输结束断开连接
            Ack = '文件接收成功！'
            serverSocket.sendto(Ack.encode(), clientAddr)
            Ack = "\n$ 文件已接受！"
            return Ack
        else: # 若客户端地址非法
            Ack = "\n$ 来自非法UDP客户端的访问"
            return Ack




