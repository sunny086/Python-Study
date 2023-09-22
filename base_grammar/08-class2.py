class F1(object):
    def show(self):
        print('F1.show')


class S1(F1):
    def show(self):
        print('S1.show')


class S2(F1):
    def show(self):
        print('S2.show')


def Func(obj):
    # python是弱类型，即无论传递过来的是什么，obj变量都能够指向它，这也就没有所谓的多态了（弱化了这个概念）
    print(obj.show())


if __name__ == '__main__':
    s1_obj = S1()
    Func(s1_obj)

    s2_obj = S2()
    Func(s2_obj)
