import redis

client = redis.Redis(host='127.0.0.1', port=6379, db=0, password='foobared')

# 有序集合：数据量大时插入、查询时间较长，每个元素不重复，并可以实现排序

# 存数据
data = {'a': 4, 'b': 3, 'c': 1, 'd': 2, 'e': 5}
client.zadd('rank_zset', data)

# 查看数据
