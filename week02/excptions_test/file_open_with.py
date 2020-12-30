file1 = open('test.txt', 'r', encoding='utf-8')
try:
    data = file1.read()
    print(f"file1: {data}")
except FileNotFoundError:
    print("文件不存在")
finally:
    file1.close()

# 通过with来写更加简洁，更优雅啊
with open('test.txt', 'r', encoding='utf-8') as file2:
    data = file2.read()
    print(f"file2: {data}")
