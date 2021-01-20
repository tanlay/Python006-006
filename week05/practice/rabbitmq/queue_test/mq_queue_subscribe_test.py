import pika

auth = pika.PlainCredentials('guest', '123')
paras = pika.ConnectionParameters(host='127.0.0.1',port=5672, virtual_host='/', credentials=auth)
conn = pika.BlockingConnection(paras)
channel = conn.channel()
channel.queue_declare('direct_demo_test',durable=False)

def callback(ch, method, properties, body):
    channel.basic_ack(delivery_tag=method.delivery_tag)
    print(body.decode())

channel.basic_consume('direct_demo_test', on_message_callback=callback)

channel.start_consuming()
