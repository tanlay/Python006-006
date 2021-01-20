import redis

# 键值对映射，基于hash table, 记录用户是否是VIP
client = redis.Redis(host='127.0.0.1', port=6379, db=0, password='foobared')

# 增加hash
client.hset('vip_user_hash', '10001', 1)
client.hset('vip_user_hash', '10002', 1)

# 删除hash
client.hdel('vip_user_hash', '10002')

# 查看hash值是否存在
print(f"10001是否存在: {client.hexists('vip_user_hash', '10001')}")
print(f"10002是否存在: {client.hexists('vip_user_hash', '10002')}")

# 添加多个hash键值对
data = {'10003': 0, '10004': 1, '10005': 1, '10006': 0}
client.hmset('vip_user_hash', data)

# hkeys: 获取所有字段名
# hget: 获取一个字段
# hmget: 获取多个字段
# hgetall: 获取一个hash table中所有键值对

print(f"获取vip_user_hash所有字段名: {client.hkeys('vip_user_hash')}")
print(f"获取vip_user_hash一个字段: {client.hget('vip_user_hash', '10006')}")
print(f"获取vip_user_hash所有键值对: {client.hgetall('vip_user_hash')}")
