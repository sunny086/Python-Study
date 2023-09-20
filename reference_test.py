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


if __name__ == '__main__':
    # map_test01()
    # map_test02()
    map_test03()
