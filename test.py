def test01():
    var1 = 100
    if var1:
        print("1 - if 表达式条件为 true")
        print(var1)

    var2 = 0
    if var2:
        print("2 - if 表达式条件为 true")
        print(var2)
    print("Good bye!")


def test02():
    num = int(input("输入一个数字："))
    if num % 2 == 0:
        if num % 3 == 0:
            print("你输入的数字可以整除 2 和 3")
        else:
            print("你输入的数字可以整除 2，但不能整除 3")
    else:
        if num % 3 == 0:
            print("你输入的数字可以整除 3，但不能整除 2")
        else:
            print("你输入的数字不能整除 2 和 3")


def test_for():
    languages = ["C", "C++", "Perl", "Python"]
    languages.append("Java")
    languages.reverse()
    for x in languages:
        print(x)


def test_range():
    for i in range(5):
        print(i)


def test_while():
    count = 0
    while (count < 9):
        print('The count is:', count)
        count = count + 1

    print("Good bye!")


def test_break():
    for letter in 'Runoob':  # 第一个实例
        if letter == 'b':
            break
        print('当前字母为 :', letter)

    var = 10  # 第二个实例
    while var > 0:
        print('当期变量值为 :', var)
        var = var - 1
        if var == 5:
            break

    print("Good bye!")


def test_continue():
    for letter in 'Runoob':  # 第一个实例
        if letter == 'o':  # 字母为 o 时跳过输出
            continue
        print('当前字母 :', letter)

    var = 10  # 第二个实例
    while var > 0:
        var = var - 1
        if var == 5:  # 变量为 5 时跳过输出
            continue
        print('当前变量值 :', var)
    print("Good bye!")


def test_pass():
    for letter in 'Runoob':
        if letter == 'o':
            # 空语句块，暂时不执行任何操作 待实现的功能
            pass
            print('执行 pass 块')
        print('当前字母 :', letter)

    print("Good bye!")


'''
在Python中，数据类型大致有两类：
值类型：本身不允许被修改，有：数值类型、布尔类型、字符串类型、元组类型等
引用类型：本身允许修改，有：列表、字典
python的变量无类型限制，其实是因为变量的本质是指针，可以指向任意对象。指针的内存空间大小是与类型无关的，其内存空间只是保存了所指向数据的内存地址。
以下示例其实是让a指向一个新的内存地址，并不会修改变量b的值：
'''


def test_value_type():
    a = 1
    b = a
    a = 2
    print(b)  # 输出的结果是1


if __name__ == '__main__':
    # test01()
    # test02()
    # test_for()
    # test_range()
    # test_while()
    # test_break()
    # test_continue()
    # test_pass()
    test_value_type()
