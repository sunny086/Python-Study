import socket

if __name__ == '__main__':
    # 创建UDP套接字
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定服务器
    s.bind(('127.0.0.1', 8080))

    # socket创建的套接字属性默认是主动的，listen变为被动，用来接收客户端信息
    s.listen(128)

    # 不断循环接收不同客户端的连接
    while True:
        # 等待到来
        rec_client, rec_addr = s.accept()
        print(rec_addr)

        # 接收数据
        data = rec_client.recv(1024)
        print(data)

        # 发送数据
        rec_client.send('accept..'.encode('utf-8'))

        # 关闭套接字
        rec_client.close()
