def show1():
    print('人生苦短，我用Python')


def show2(num1, num2):
    print(num1 + num2)


def show3():
    info = 'hello'
    print(info)


# print(info) # NameError: name 'info' is not defined


# 当函数内出现局部变量和全局变量相同名字时，函数内部中的 变量名 = 数据 此时理解为定义了一个局部变量，而不是修改全局变量的值。
info = 'hello'


def show4():
    info = 'world'
    print(info)


# 如果要在函数内部修改全局变量，则需要借助 global 关键字的声明
def show5():
    global info
    info = 'world'
    print(info)


if __name__ == '__main__':
    show1()
    show2(1, 2)
    show3()  # hello
    show4()  # world 输出的是局部赋值的
    print(info)  # hello 输出的是全局的
    show5()  # world
    print(info)  # world 被global修饰了 全局修改
