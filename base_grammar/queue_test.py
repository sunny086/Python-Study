import multiprocessing


def queue_test01():
    queue = multiprocessing.Queue(3)
    queue.put("111")
    queue.put(222)

    # 取数据
    res = queue.get()
    print(res)


if __name__ == '__main__':
    queue_test01()
