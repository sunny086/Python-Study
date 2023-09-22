# 必须按照顺序执行，多个任务无法同时在还行
import time
import multiprocessing


def sing():
    for i in range(5):
        print("sing: hero")
        time.sleep(1)  # 每唱一次，等1秒再唱


def dance():
    for i in range(5):
        print("dance: swan")
        time.sleep(1)  # 每唱一次，等1秒再跳

# 使用多进程实现多任务
def main():
    p1 = multiprocessing.Process(target=sing)
    p2 = multiprocessing.Process(target=dance)
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()
