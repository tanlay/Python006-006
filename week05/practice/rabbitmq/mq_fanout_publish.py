import pika

auth = pika.PlainCredentials('guest', '123')
paras = pika.ConnectionParameters(host='127.0.0.1',
        port=5672,
        virtual_host='/',
        credentials=auth,
        )
conn = pika.BlockingConnection(paras)
channel = conn.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = 'send message to fanout'

# 定义交换机，1对多
channel.basic_publish(exchange='logs',
        routing_key='',
        body=message,
        )
conn.close()
