import pika

auth = pika.PlainCredentials('guest', '123')
paras = pika.ConnectionParameters(host='127.0.0.1',
        port=5672,
        virtual_host='/',
        credentials=auth,
        )
conn = pika.BlockingConnection(paras)
channel = conn.channel()

# 申明交换机
channel.exchange_declare(exchange='logs',exchange_type='fanout')

# 申明消息队列
# exclusive 当与消费者断开连接是，队列立即被删除
# 随机产生队列
result = channel.queue_declare(queue='', exclusive=True)
# 获取队列名称
queue_name = result.method.queue

# 通过bind实现exchange发送到指定的queue
channel.queue_bind(exchange='logs', queue=queue_name)

# 定义回调函数处理队列中的消息
def callback(ch, method, properties, body):
    print(body.decode())
    # 手动确认消息
    # ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue=queue_name,
        on_message_callback=callback,
        auto_ack=True
        )

channel.start_consuming()

