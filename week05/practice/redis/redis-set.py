import redis

# 集合用途: 去重，可用于数据分析，逻辑与或非


client = redis.Redis(host='127.0.0.1', port=6379, db=0, password='foobared')

# 添加数据到set. sadd()
print(client.sadd('redis_set_demo', 'now_data'))

# 移除数据 spop(), 随机移除，不固定顺序
# client.spop()

# 查看集合数据
print(client.smembers('redis_set_demo'))


client.sadd('redis_set_1', 'a', 'b', 'c', '3')
client.sadd('redis_set_2', '1', '2', '3', 'b')

print(f"redis_set_1: {client.smembers('redis_set_1')}")
print(f"redis_set_2: {client.smembers('redis_set_2')}")

# 交集
print(f"交集: {client.sinter('redis_set_1', 'redis_set_2')}")

# 并集
print(f"并集: {client.sunion('redis_set_1', 'redis_set_2')}")

# 差集
print(f"差集1: {client.sdiff('redis_set_1', 'redis_set_2')}")
print(f"差集2: {client.sdiff('redis_set_2', 'redis_set_1')}")
