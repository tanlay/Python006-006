import redis

while True:
    # 从右侧发送
    phone = client.rpop('list_redis_demo')
    if not phone:
        print("send done")
        break
    sendsms(phone)

    retry_count = retry(phone)
        if retry_count > 5:
            print("打印出最后的重试列表")
            # 使用lpush添加到左侧
            client.lpush('list_redis_demo', phone)
