import pika

auth = pika.PlainCredentials('guest', '123')

paras = pika.ConnectionParameters(host='127.0.0.1', port=5672, virtual_host='/', credentials=auth)

conn = pika.BlockingConnection(paras)

channel = conn.channel()

# 申明消息队列,两边都申明
channel.queue_declare(queue='direct_demo', durable=False)

# 定义一个回调函数处理消息队列中的消息
def callback(ch, method, properties, body):
    # 手动确定消息, 防止消息丢失
    channel.basic_ack(delivery_tag=method.delivery_tag)
    # 处理消息
    print(body.decode())

# 消费者使用队列和那一个回调函数处理消息
channel.basic_consume('direct_demo', on_message_callback=callback)

# 接收消息，并进入阻塞状态
channel.start_consuming()
