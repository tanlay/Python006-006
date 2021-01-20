import pika

auth = pika.PlainCredentials('guest', '123')
paras = pika.ConnectionParameters(host='127.0.0.1', port=5672, virtual_host='/', credentials=auth)
conn = pika.BlockingConnection(paras)
channel = conn.channel()

# 打开队列持久化
channel.queue_declare('task_queue', durable=True)
message = 'send message to taskqueue'
channel.basic_publish(exchange='',
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(delivery_mode=2,  # 消息持久化
        ))

conn.close()
