import time


# try except可以捕获多个异常
def test1():
    try:
        num = 1
        print('-----test--1---')
        open('123.txt', 'r')  # 如果123.txt文件不存在，那么会产生 IOError 异常
        print('-----test--2---')
        print(num)  # 如果num变量没有定义，那么会产生 NameError 异常
    # 如果想通过一次except捕获到多个异常可以用一个元组的方式
    except (IOError, NameError):
        pass
    else:
        print('没有捕获到异常，真高兴')


# finally语句可以在异常发生后强制执行
def test2():
    try:
        f = open('test.txt')
        try:
            while True:
                content = f.readline()
                if len(content) == 0:
                    break
                time.sleep(2)
                print(content)
        except:
            # 如果在读取文件的过程中，产生了异常，那么就会捕获到
            # 比如 按下了 ctrl+c
            print('意外终止了读取数据')
            pass
        finally:
            f.close()
            print('关闭文件')
    except:
        print("没有这个文件")


if __name__ == '__main__':
    test1()
    test2()
