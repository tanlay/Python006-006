import redis

client = redis.Redis(host='127.0.0.1', port=6379, password='foobared')
client.set('name', 'Join')

# nx 参数，不会覆盖已经有的key
client.set('age', 26, nx=True)

# 更改字符串，在之后面添加字符串变成新串
client.append('name', '·Tom')
res = client.get('name')
# print(res)

print(res.decode())

# 字符串加减法
print(f"age: {client.get('age').decode()}")
# +1
res2 = client.incr('age')
print(f"age+1: {res2}")
res3 = client.decr('age')
print(f"age-1: {res3}")
