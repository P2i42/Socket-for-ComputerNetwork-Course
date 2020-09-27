from socket import *
import struct, os
serverPort = 12000
# serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('192.168.1.106', serverPort))
print('ready')
while True:

    fileinfo_size = struct.calcsize('128sl')
    buf, clientAddr = serverSocket.recvfrom(fileinfo_size)

    if buf:
        # 获取文件名和文件大小
        filename, filesize = struct.unpack('128sl', buf)
        fn = filename.strip(b'\00')
        fn = fn.decode()
        print('file new name is {0}, filesize if {1}'.format(str(fn), filesize))
        recvd_size = 0  # 定义已接收文件的大小
        fp = open('./' + str(fn), 'wb')
        print('start receiving...')
        print(filesize)
        while not recvd_size == filesize:
            if filesize - recvd_size > 1024:
                data = serverSocket.recvfrom(1024)
                recvd_size += 1024
            else:
                data = serverSocket.recvfrom(filesize - recvd_size)
                recvd_size = filesize
            fp.write(data[0])
        fp.close()
        print('end receive...')


# serverSocket.listen(1)
# print('ready')
# while True:
#     print(1)
#     conSock, addr = serverSocket.accept()
#     print(conSock)
#     print(addr)
#     print(serverSocket.accept())
#     sen = conSock.recv(1024).decode()
#     capsen = sen.upper()
#     conSock.send(capsen.encode())
#     conSock.close()