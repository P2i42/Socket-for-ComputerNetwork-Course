import socket

#TODO  判断用户身份是否合法为合法用户 echo 数据
legalAddr = ['192.168.1.107']

def serverTCPlink():
    serverPort = 12000
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind(('', serverPort))
    while(True):
        recvData, addr = serverSocket.recvfrom(2048)
        if addr in legalAddr:
            Ack = '{ ' + recvData.decode() + ' } ' + '接受成功'
            serverSocket.sendto(Ack.encode(), addr)
            # cnSocket.close()


