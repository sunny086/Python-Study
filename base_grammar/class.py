from datetime import datetime


class Class1:
    def __init__(self):
        self.user = None
        self.resourceType = None
        self.resourceId = None
        self.accessType = None
        self.accessTime = None
        self.duration = None
        self.field1 = "我是嫩爹"

    def set_user(self, user):
        self.user = user

    def set_resource_type(self, resource_type):
        self.resourceType = resource_type

    def set_resource_id(self, resource_id):
        self.resourceId = resource_id

    def set_access_type(self, access_type):
        self.accessType = access_type

    def set_access_time(self, access_time):
        # 使用 datetime 对象表示日期和时间
        self.accessTime = datetime.strptime(access_time, "%Y-%m-%d %H:%M:%S")

    def set_duration(self, duration):
        self.duration = duration

    def __str__(self):
        return (
            f"User: {self.user}\n"
            f"Resource Type: {self.resourceType}\n"
            f"Resource ID: {self.resourceId}\n"
            f"Access Type: {self.accessType}\n"
            f"Access Time: {self.accessTime}\n"
            f"Duration: {self.duration}\n"
        )


def class1_test():
    # 创建一个AccessLog对象
    class1 = Class1()
    class1.set_user("John")
    class1.set_resource_type("File")
    class1.set_resource_id("12345")
    class1.set_access_type("Read")
    class1.set_access_time("2023-09-21 15:30:00")
    class1.set_duration(5)

    # 打印对象信息
    print(class1)
    print(class1.field1)


class Class2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return (
            f"Class2(name='{self.name}', age={self.age})"
        )


def class2_test():
    class2 = Class2("张三", 18)
    print(class2.name)
    print(class2.age)
    print(class2)


# 在Python中，f 是格式化字符串字面值（Formatted String Literal）的前缀。它是Python 3.6及更高版本引入的一种字符串表示形式，用于创建包含表达式的字符串，并在字符串中插入表达式的值。
# 使用 f 字符串字面值可以更方便地在字符串中嵌入变量、表达式、函数调用等，并以更清晰的方式进行字符串格式化。在 f 字符串中，你可以在字符串中使用花括号 {} 来包围表达式，然后在花括号内写入要插入的表达式。
def format_test():
    name = "Alice"
    age = 30
    # 使用f字符串嵌入变量和表达式
    message = f"My name is {name} and I am {age} years old."
    # 打印message
    print(message)


if __name__ == '__main__':
    class1_test()
    print("\n")
    class2_test()
    print("\n")
    format_test()
