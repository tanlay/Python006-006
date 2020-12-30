def f1():
    1/0


def f2():
    list1 = []
    list1[1]
    f1()


def f3():
    f2()


try:
    # 修改f1(),f3()执行顺序发现，异常发生后，不会再接着捕获之后的异常了
    f1()
    f3()
except IndexError as err:
    print(f"亲，索引超过范围了. {err}")

except ZeroDivisionError as err:
    print(f"亲，被除数不能为0. {err}")