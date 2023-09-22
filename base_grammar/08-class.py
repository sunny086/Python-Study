# 在属性名和方法名 前面 加上两个下划线 __ 即成为私有权限
class Master(object):
    def __init__(self):
        self.kongfu = "古法煎饼果子配方"

    def make_cake(self):
        print("[古法] 按照 <%s> 制作了一份煎饼果子..." % self.kongfu)


class School(object):
    def __init__(self):
        self.kongfu = "现代煎饼果子配方"

    def make_cake(self):
        print("[现代] 按照 <%s> 制作了一份煎饼果子..." % self.kongfu)


class Prentice(School, Master):
    def __init__(self):
        self.kongfu = "猫氏煎饼果子配方"
        # 私有属性，可以在类内部通过self调用，但不能通过对象访问
        self.__money = 10000

    # 私有方法，可以在类内部通过self调用，但不能通过对象访问
    def __print_info(self):
        print(self.kongfu)
        print(self.__money)

    def make_cake(self):
        self.__init__()
        print("[猫氏] 按照 <%s> 制作了一份煎饼果子..." % self.kongfu)

    def make_old_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_new_cake(self):
        School.__init__(self)
        School.make_cake(self)


class PrenticePrentice(Prentice):
    pass


def test1():
    damao = Prentice()
    print(damao.kongfu)
    print(damao.make_cake())
    print(damao.make_old_cake())
    print(damao.make_new_cake())
    # 对象不能访问私有权限的属性和方法
    # AttributeError: 'Prentice' object has no attribute '__money'
    print(damao.__money)
    # AttributeError: 'Prentice' object has no attribute '__print_info'
    damao.__print_info()


def test2():
    pp = PrenticePrentice()
    print(pp.kongfu)
    print(pp.make_cake())
    print(pp.make_old_cake())
    print(pp.make_new_cake())
    # 子类不能继承父类私有权限的属性和方法
    # AttributeError: 'PrenticePrentice' object has no attribute '__money'
    print(pp.__money)
    pp.__print_info()


if __name__ == '__main__':
    test1()
    # test2()
