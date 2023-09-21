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


if __name__ == '__main__':
    class1_test()
