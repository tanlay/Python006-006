def a():
    return b()


def b():
    return c()


def c():
    return d()


def d():
    x = 0
    return 100/x


try:
    a()
except ZeroDivisionError as err:
    print("被除数不能为0哦")
    print("ZeroDivisionError: ", err)
