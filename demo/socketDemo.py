import socket
import sys


def server():
    # 创建 socket 对象
    serversocket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    # 获取本地主机名
    host = socket.gethostname()
    port = 9999
    # 绑定端口
    serversocket.bind((host, port))
    # 设置最大连接数，超过后排队
    serversocket.listen(5)
    while True:
        # 建立客户端连接
        clientsocket, addr = serversocket.accept()
        print("连接地址: %s" % str(addr))
        msg = '欢迎访问菜鸟教程！' + "\r\n"
        clientsocket.send(msg.encode('utf-8'))
        clientsocket.close()


def client():
    # 创建 socket 对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 获取本地主机名
    host = socket.gethostname()
    # 设置端口好
    port = 9999
    # 连接服务，指定主机和端口
    s.connect((host, port))
    # 接收小于 1024 字节的数据
    msg = s.recv(1024)
    s.close()
    print(msg.decode('utf-8'))


# server()
client()