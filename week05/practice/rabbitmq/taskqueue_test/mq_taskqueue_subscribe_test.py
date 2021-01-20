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

channel.queue_declare('taskqueue_demo_test', durable=True)

def callback(ch, method, properties, body):
    time.sleep(1)
    print(body.decode())
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume('taskqueue_demo_test', callback)
channel.start_consuming()
