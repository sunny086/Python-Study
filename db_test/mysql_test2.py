import pymysql

username = input("username：")


def main():
    # 1. 链接数据库
    conn = pymysql.connect(host='localhost', port=3306, database='datart', user='root', password='tiger',
                           charset='utf8')

    # 2. 获取游标对象
    cursor = conn.cursor()

    # 3. 组织字符串
    sql = """select * from user where username like %s;"""

    # 4. 执行模糊查询语句
    cursor.execute(sql, ['%' + username + '%'])

    # 5. 显示相应的结果
    results = cursor.fetchall()
    if results:
        for result in results:
            print(result)
    else:
        print("未找到匹配的用户。")

    # 6. 关闭
    cursor.close()
    conn.close()


# 模糊查询
if __name__ == "__main__":
    main()
