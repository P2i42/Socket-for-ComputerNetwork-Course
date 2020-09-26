from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('192.168.1.105', serverPort))
serverSocket.listen(1)
print('ready')
while True:
    print(1)
    conSock, addr = serverSocket.accept()
    print(conSock)
    print(addr)
    print(serverSocket.accept())
    sen = conSock.recv(1024).decode()
    capsen = sen.upper()
    conSock.send(capsen.encode())
    conSock.close()