class People(object):
    # 私有类属性
    __country = 'china'

    # 类方法，用classmethod来进行修饰
    @classmethod
    def get_country(cls):
        return cls.__country

    @classmethod
    def set_country(cls, country):
        cls.__country = country


def test1():
    p = People()
    print(p.get_country())  # 可以用过实例对象引用
    print(People.get_country())  # 可以通过类对象引用


# 通过类方法对类属性进行修改 相当于修改了static的值
def test2():
    p = People()
    print(p.get_country())  # 可以用过实例对象访问
    print(People.get_country())  # 可以通过类访问

    p.set_country('japan')

    print(p.get_country())
    print(People.get_country())


# 类属性 类方法 实例方法 静态方法
if __name__ == '__main__':
    test1()
    print("====================================")
    test2()
