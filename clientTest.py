from socket import *
import os, struct

serverName = '192.168.1.106'
serverPort = 12000
text = '123'
clientSocket = socket(AF_INET, SOCK_DGRAM)
print(clientSocket)
filepath = './388.png'
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
        break
    clientSocket.sendto(data, server)
    print('sending')

# 关闭当期的套接字对象
clientSocket.close()




















# sentence = input('input: ')
# clientSocket.send(sentence.encode())
# modsen = clientSocket.recv(1024)
# print('From server: ', modsen.decode())
# clientSocket.close()