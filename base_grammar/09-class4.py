class A(object):
    def __init__(self):
        print("这是 init 方法")

    # 实例化的类
    def __new__(cls):
        print("这是 new 方法")
        return object.__new__(cls)


if __name__ == '__main__':
    a = A()
    print(a)
    A.__new__(A)
