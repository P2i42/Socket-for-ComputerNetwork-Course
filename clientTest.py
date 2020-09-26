from socket import *
import os, struct

serverName = '192.168.1.108'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
# clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1) #在客户端开启心跳维护
filepath = './blacklist.jpg'
    # 定义文件信息。128s表示文件名为128bytes长，l表示一个int或log文件类型，在此为文件大小
fileinfo_size = struct.calcsize('128sl')
# 定义文件头信息，包含文件名和文件大小
fhead = struct.pack('128sl', os.path.basename(filepath).encode('utf-8'), os.stat(filepath).st_size)
# 发送文件名称与文件大小
clientSocket.send(fhead)

# 将传输文件以二进制的形式分多次上传至服务器
fp = open(filepath, 'rb')
while True:
    data = fp.read(1024)
    if not data:
        print ('{0} file send over...'.format(os.path.basename(filepath)))
        break
    clientSocket.send(data)
# 关闭当期的套接字对象
clientSocket.close()
# sentence = input('input: ')
# clientSocket.send(sentence.encode())
# modsen = clientSocket.recv(1024)
# print('From server: ', modsen.decode())
# clientSocket.close()