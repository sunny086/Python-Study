class People(object):
    country = 'china'  # 公有的类属性
    name = 'Tom'  # 公有的类属性
    __age = 12  # 私有的类属性


# 对象的属性一般称呼为实例属性，类属性则是类本身所拥有的属性，该属性会被所有的实例对象共享，在内存中只存在一个副本，类似java中的静态成员。
def test1():
    p = People()
    print(p.name)  # 正确
    print(People.name)  # 正确
    # print(p.__age)  # 错误，不能在类外通过实例对象访问私有的类属性
    # print(People.__age) # 错误，不能在类外通过类对象访问私有的类属性


# 类属性等价于static 实例属性就是局部的实例
def test2():
    print(People.country)
    p = People()
    print(p.country)
    p.country = 'japan'
    print(p.country)  # 实例属性会屏蔽掉同名的类属性
    print(People.country)
    del p.country  # 删除实例属性
    print(p.country)


if __name__ == '__main__':
    # test1()
    test2()
