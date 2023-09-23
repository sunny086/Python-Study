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
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    t1.start()
    t2.start()

    while True:
        # 查看当前所有的线程
        length = len(threading.enumerate())
        print("当前线程数为：%d" % length)
        if length <= 1:
            break
        time.sleep(0.5)


if __name__ == "__main__":
    main()
