import redis

pool = redis.ConnectionPool(host='127.0.0.1',port=6379, db=0, password='foobared')
cli = redis.StrictRedis(connection_pool=pool)


def counter(video_id):
    if not cli.hexists('video_view_num', video_id):
        # 创建hash video_view_num
        cli.hset('video_view_num', video_id, 0)
    # 自增+1
    cli.hincrby('video_view_num', video_id, 1)
    count_number = cli.hget('video_view_num', video_id).decode()
    print(f"{video_id}当前访问访问量：{count_number}")
    return count_number

counter(1001) # 返回 1
counter(1001) # 返回 2
counter(1002) # 返回 1
counter(1001) # 返回 3
counter(1002) # 返回 2
