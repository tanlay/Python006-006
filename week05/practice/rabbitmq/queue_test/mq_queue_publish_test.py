import pika

auth = pika.PlainCredentials('guest', '123')

paras = pika.ConnectionParameters(host='127.0.0.1', port=5672, virtual_host='/', credentials=auth)

conn = pika.BlockingConnection(paras)

channel = conn.channel()

channel.queue_declare('direct_demo_test', durable=False)

channel.basic_publish(exchange='', routing_key='direct_demo_test', body="This is a rabbitmq publish test")

conn.close()
