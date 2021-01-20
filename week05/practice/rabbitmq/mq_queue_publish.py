import pika

# 用户名密码
auth = pika.PlainCredentials('guest', '123')

# 虚拟队列需指定virtual_host,默认可不填
paras = pika.ConnectionParameters(host='127.0.0.1', port=5672, virtual_host='/', credentials=auth)

# 阻塞方法,消费者连接rabbitmq时默认阻塞,有消息则处理，没有就进入阻塞状态
conn = pika.BlockingConnection(paras)

# 建立信道, 建立一个TCP连接
channel = conn.channel()

# 申明消息队列,不存在则自动创建
channel.queue_declare(queue='direct_demo', durable=False)

# exchange指定交换机
# routing_key指定对列名
# 生产中json格式body
channel.basic_publish(exchange='', routing_key='direct_demo', body='send message to rabbitmq')

# 关闭与rabbitmq-server的连接
conn.close()
