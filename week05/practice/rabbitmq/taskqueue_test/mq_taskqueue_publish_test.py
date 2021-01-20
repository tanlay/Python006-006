import pika

auth = pika.PlainCredentials('guest','123')
paras = pika.ConnectionParameters(host='127.0.0.1',
        port=5672,
        virtual_host='/',
        credentials=auth,
        )
conn = pika.BlockingConnection(paras)
channel = conn.channel()

channel.queue_declare('taskqueue_demo_test', durable=True)

message='This is taskqueue rabbitmq'
channel.basic_publish(exchange='',
        routing_key='taskqueue_demo_test',
        body=message,
        properties=pika.BasicProperties(delivery_mode=2,)
        )
conn.close()
