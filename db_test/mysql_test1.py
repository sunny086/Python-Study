import pymysql

username = input("username：")


def main():
    # 1. 链接数据库
    conn = pymysql.connect(host='localhost', port=3306, database='datart', user='root', password='tiger',
                           charset='utf8')

    # 2. 获取游标对象
    cursor = conn.cursor()

    # 3. 组织字符串
    # 在Python中，可以使用单引号或双引号来创建字符串。在SQL查询字符串中，使用三重引号（"""或'''）是为了多行字符串的创建，以便在多行的情况下更容易编写和阅读SQL查询。
    sql = """select * from user where username=%s;"""

    # 4. 执行查询语句
    cursor.execute(sql, [username])

    # 5. 显示相应的结果
    result = cursor.fetchall()
    if result:
        print(result)
    else:
        print("未找到匹配的用户。")

    # 6. 关闭
    cursor.close()
    conn.close()


# 精确查询
if __name__ == "__main__":
    main()
