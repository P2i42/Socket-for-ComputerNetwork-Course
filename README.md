# Socket-for-ComputerNetwork-Course
  1. 运行mainUI.py 出现主界面，双开界面一个用于客户端，一个服务端

  2. 点击TCPserver或UDPserver按钮进入对应服务端界面，默认状态为仅接受文字

  3. 点击TCPclient或UDPclient按钮进入用户登录界面，此时点击主界面可返回，输入用户名和密码可用用户名：[admin, guest]， 密码与用户名相同，点击登录，用户名或密码不正确则弹出提示信息

  4. 输入服务端地址和端口号，UDP客户端点击确认，TCP客户端点击登录

  5.发送文字则在左侧文本输入框输入完成后点击文本发送，发送文件则点击选择文件发送，弹出windows文件选择器，选择完成点击打开即开始发送，发送完成后右侧框会出现提示信息。TCP客户端需点击重连后再次发送其他   信息，UDP客户端可直接发送，结束点击退出退出。

  6.服务端需点击接收信息来接受信息，选择接受文件则仅能接受文件信息，文本同理，左侧显示服务器状态信息，TCP服务端单次接受信息后会自动关闭该次连接套接字，右上角会显示客户端信息

  7.TCP服务端点击关闭连接则关闭监听和服务端Socket，UDP端关闭服务端Socket，点击退出作最后的套接字关闭确认，最后退出服务端。

  8. 查看程序运行文件夹，可以查找到服务端接受的两个文件
