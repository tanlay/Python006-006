gennum = ( i for i in range(0,4))

for n in range(8):
    try:
        print(next(gennum))
    except StopIteration:
        print("已经是最后一个元素了")
        break