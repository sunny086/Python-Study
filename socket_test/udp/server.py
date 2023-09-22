import socket

if __name__ == '__main__':
    # 创建UDP套接字
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定本地信息，不绑定则随机分配
    s.bind(('127.0.0.1', 8080))

    # 接收数据
    while True:
        data = s.recvfrom(1024)
        print(data)

    # 关闭套接字
    s.close()
