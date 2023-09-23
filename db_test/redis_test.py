import redis


def main():
    # 创建一个Redis连接
    redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

    # 设置一个键值对
    redis_client.set('name', 'John')

    # 获取键对应的值
    name = redis_client.get('name')

    if name:
        print(f"Name: {name}")
    else:
        print("Key 'name' not found in Redis.")


# redis test
# ModuleNotFoundError: No module named 'concurrent.futures'
# 与标准库同名的package会影响依赖的加载，说明项目的package优先级>本地库的优先级
# 在Python 3.10及更高版本中，redis库不再依赖于concurrent.futures模块。
# concurrent.futures模块已经被合并到标准库中，不再是一个独立的模块
if __name__ == '__main__':
    main()
