import socket

if __name__ == '__main__':
    # 创建TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接服务器
    s.connect(('127.0.0.1', 8080))

    # 套接字发送数据
    num = 1
    while True:
        data = 'hello' + str(num)
        rec = s.send(data.encode('utf-8'))
        print(rec)
        num = num + 1
        if num == 10:
            break

    # 关闭套接字
    s.close()
