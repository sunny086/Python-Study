def map_test01():
    tinydict = {
        'name': 'overnote',
        'code': 1,
        'site': 'overnote/python'
    }
    print(tinydict)  # 输出完整的字典
    print(tinydict.keys())  # 输出所有键
    print(tinydict.values())  # 输出所有值
    print(tinydict['name'])  # 输出键为'name'的值
    print(tinydict.get('name'))  # 输出键为'name'的值


def map_test02():
    dict = {}
    dict['one'] = "javascript"
    dict[2] = "golang"
    print(dict['one'])  # 输出键为 'one' 的值，若不存在则报错
    print(dict[2])  # 输出键为 2 的值


def map_test03():
    tinydict = {
        'name': 'overnote',
        'code': 1,
        'site': 'overnote/python'
    }
    # overnote
    print(tinydict.get("name"))
    print(tinydict.get("name1"))  # None
    print(tinydict.get("name1"))  # default  若不存在键，就返回参数给出的默认值


def set_test01():
    set1 = {1, 2, 4, 5}
    # 添加元素
    set1.add(8)
    # 修改元素：把传入的元素拆分，作为个体传入到集合中
    set1.update("abcd")
    # 删除元素      pop() 方法会随机删除元素，
    set1.remove(1)  # 如果没有该元素，则报错
    set1.discard(22)  # 如果没有该元素，不做任何操作


def set_test02():
    a = set('asdfghjklzxcvbnm')
    b = set('asdfgh')
    print(a)
    print(a - b)  # a 和 b 的差集
    print(a | b)  # a 和 b 的并集
    print(a & b)  # a 和 b 的交集
    print(a ^ b)  # a 和 b 中不同时存在的元素


def tuple_test01():
    tuple = ('abcd', 786, 2.23, 'overnote', 70.2)
    tinytuple = (123, 'overnote')

    print(tuple)  # 输出完整元组
    print(tuple[0])  # 输出元组的第一个元素
    print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
    print(tuple[2:])  # 输出从第三个元素开始的所有元素
    print(tinytuple * 2)  # 输出两次元组
    print(tuple + tinytuple)  # 连接元组


# 语法表示：
# 集合：集合使用花括号 {} 表示。例如：my_set = {1, 2, 3}。
# 列表：列表使用方括号 [] 表示。例如：my_list = [1, 2, 3]。
# 元组：元组使用圆括号 () 表示。例如：my_tuple = (1, 2, 3)。

# 可哈希性（Hashability）：
# 在Python中，字典的键和集合的元素必须是可哈希的，这意味着它们必须是不可变的数据类型，如整数、字符串、元组
# 集合：集合是不可哈希的，因为它们是可变的，不能用作字典的键或其他集合的元素。
# 列表：列表是不可哈希的，因为它们是可变的，不能用作字典的键或其他集合的元素。
# 元组：元组是可哈希的，因为它们是不可变的，可以用作字典的键或其他集合的元素。
# 集合（Set）和列表（List）不可哈希，主要是因为它们是可变的数据结构，而哈希值需要保持不变。

def set_list_tuple_test01():
    # 集合（Set）：集合中的元素是唯一的，可以包含不同的数据类型。例如，一个集合可以包含整数、浮点数、字符串等不同类型的元素。
    # 集合不可重复 无序
    my_set = {1, 2.5, "Hello", (1, 2)}
    print(my_set)
    # 列表（List）：列表中的元素可以是不同的数据类型，你可以混合存储整数、浮点数、字符串、列表、元组等各种类型的元素。
    my_list = [1, 2.5, "Hello", [3, 4], (5, 6)]
    print(my_list)
    # 元组（Tuple）：元组中的元素也可以是不同的数据类型，允许混合存储各种类型的元素。
    # 元组不可变，一旦创建不可修改，元组也可以包含列表和元组。
    my_tuple = (1, 2.5, "Hello", [3, 4], (5, 6))
    print(my_tuple)

    #  "TypeError: unhashable type: 'list'"
    #  是因为你尝试将一个列表作为字典的键或集合的元素，而列表是不可哈希的。
    #  在Python中，字典的键和集合的元素必须是可哈希的，这意味着它们必须是不可变的数据类型，如整数、字符串、元组
    my_set = {1, 2.5, "Hello", [1, 2]}  # TypeError: unhashable type: 'list'
    print(my_set)


if __name__ == '__main__':
    # map_test01()
    # map_test02()
    # map_test03()
    # set_test01()
    # set_test02()
    # tuple_test01()
    set_list_tuple_test01()
