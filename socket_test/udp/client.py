import socket

if __name__ == '__main__':
    # 创建UDP套接字：第一个参数代表IPV4，第二个参数代表是UDP还是TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 套接字发送数据
    num = 1
    while True:
        data = 'hello' + str(num)
        # s.sendto('hello', ('127.0.0.1', 8080))
        s.sendto(data.encode('utf-8'), ('127.0.0.1', 8080))
        num = num + 1
        if num == 10:
            break

    # 关闭套接字
    s.close()
