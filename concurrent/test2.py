import time
import threading


def sing():
    for i in range(5):
        print("sing: hero")
        time.sleep(1)  # 每唱一次，等1秒再唱


def dance():
    for i in range(5):
        print("dance: swan")
        time.sleep(1)  # 每唱一次，等1秒再跳


def main():
    t1 = threading.Thread(target=sing)  # 创建一个线程对象
    t2 = threading.Thread(target=dance)  # 创建一个线程对象
    t1.start()  # 开启线程
    t2.start()  # 开启线程


# 使用多线程实现多任务
if __name__ == "__main__":
    main()
