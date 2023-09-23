import time
import threading

# 定义共享的全局变量
num = 0


def add100():
    global num
    mutex.acquire()  # 加锁：若已经加锁，则会直到锁被揭开
    for i in range(100000):
        num = num + 0.00001
    mutex.release()  # 解锁


def add1000():
    global num
    mutex.acquire()  # 加锁：若已经加锁，则会直到锁被揭开
    for i in range(100000):
        num = num + 1000
    mutex.release()  # 解锁


# 创建互斥锁，默认不会上锁
mutex = threading.Lock()


def main():
    t1 = threading.Thread(target=add100)
    t2 = threading.Thread(target=add1000)

    t1.start()
    t2.start()

    time.sleep(5)
    print(num)  # 100000001.0 永远不会变


if __name__ == "__main__":
    main()
