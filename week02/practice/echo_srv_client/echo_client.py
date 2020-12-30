import socket

HOST = 'localhost'
PORT = 30000


def echo_client():
    """Echo client"""
    # 创建一个ipv4，tcp的socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 连接到服务器
    s.connect((HOST, PORT))

    while 1:
        # 接收用户数据并发送给服务端
        data = input('input> ')
        # 设置退出条件
        if data == 'exit':
            break

        # 发送数据到服务端
        s.sendall(data.encode())

        # 接收服务端数据
        data = s.recv(1024)
        if not data:
            break
        else:
            print(data.decode('utf-8'))

    s.close()

if __name__ == "__main__":
    echo_client()