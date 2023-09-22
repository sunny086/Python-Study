import time
import threading

# 定义共享的全局变量
num = 0


def minus():
    global num
    for i in range(100000):
        num = num - 2


def add():
    global num
    for i in range(100000):
        num = num + 1


def main():
    t1 = threading.Thread(target=minus)
    t2 = threading.Thread(target=add)

    t1.start()
    t2.start()
    time.sleep(5)
    print(num)


if __name__ == "__main__":
    main()
