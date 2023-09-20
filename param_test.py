# 如果在调用参数时，缺省参数的值没有传入，则取其默认值：
def show2(num1, num2=100):
    print(num1 + num2)
    print("num1 = %d, num2 = %d" % (num1, num2))


# 注意：带有默认值的参数一定要位于参数列表的最后面。
show2(100)
