import redis


# 用来做队列,需要遍历数据,有序
client = redis.Redis(host='127.0.0.1', port=6379, db=1 ,password='foobared')

# 0, -1

# 插入数据 lpush,rpush
client.lpush('list_redis_demo', 'python')
client.rpush('list_redis_demo', 'java')

# 移除数据
# client.lpop('list_redis_demo')
# client.rpop('list_redis_demo')

# 打印列表元素
print(f"list_redis_demo元素: {client.lrange('list_redis_demo', 0, -1)}")

# 查看list表长度
print(client.llen('list_redis_demo'))
