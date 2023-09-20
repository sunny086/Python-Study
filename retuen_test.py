def fn(a, b):
    r1 = a // b
    r2 = a % b
    return r1, r2  # 返回结构类型默认是元组


# Python的return支持返回多个数据，return后面可以是元组，列表、字典等，只要是能够存储多个数据的类型，就可以一次性返回多个数据：
if __name__ == '__main__':
    result = fn(5, 2)
    print(result)  # 输出(2, 1)

    # 多返回值可以直接进行拆包
    num1, num2 = fn(5, 2)
    print(num1)
    print(num2)
