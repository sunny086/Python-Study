class People(object):
    country = 'china'

    @staticmethod
    # 静态方法
    def get_country():
        return People.country


# @staticmethod修饰的静态方法；实例和类都可以访问
if __name__ == '__main__':
    p = People()
    # 通过对象访问静态方法
    print(p.get_country())

    # 通过类访问静态方法
    print(People.get_country())
