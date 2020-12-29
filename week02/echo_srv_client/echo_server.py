import socket

HOST = 'localhost'
PORT = 30000


def echo_server():
    """Echo server"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 对象s绑定到指定的主机端口上
    s.bind((HOST, PORT))
    # 只接受一个连接
    s.listen(1)
    while 1:
        conn, addr = s.accept()
        # 输出客户端地址
        print(f'Connection by {addr}')
        while 1:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
            print(data.decode('utf-8'))
        conn.close()
    s.close()

if __name__ == "__main__":
    echo_server()
