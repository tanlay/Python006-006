# 使用urllib获取豆瓣250
from http import cookiejar
from urllib import request

# GET方法
resp = request.urlopen('http://httpbin.org/get')
print(resp.read().decode())

# POST方法
resp = request.urlopen("http://httpbin.org/post",
                       data=b'key=value', timeout=10)
print(resp.read().decode())

# cookie

# 创建一个cookiejar对象
cookie = cookiejar.CookieJar()

# 创建一个cookie处理器
handler = request.HTTPCookieProcessor(cookie)

# 创建一个Opener对象
opener = request.build_opener(handler)
