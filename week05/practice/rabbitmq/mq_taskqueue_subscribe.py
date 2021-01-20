import time
import pika

auth = pika.PlainCredentials('guest', '123')
paras = pika.ConnectionParameters(host='127.0.0.1',
        port=5672,
        virtual_host='/',
        credentials=auth,
        )
conn = pika.BlockingConnection(paras)

channel = conn.channel()

channel.queue_declare('task_queue', durable=True)

def callback(ch, method, properties, body):
    time.sleep(1)
    print(body.decode())
    # 手动确认消息
    ch.basic_ack(delivery_tag=method.delivery_tag)

# 如果消费者的chanbel未确认的消息数达到prefetch_count数，则不向该消费者发送消息
channel.basic_qos(prefetch_count=1)
# 消费者使用队列和哪个回调函数处理消息
channel.basic_consume('task_queue', callback)
# 开始接收消息并进入阻塞状态
channel.start_consuming()

