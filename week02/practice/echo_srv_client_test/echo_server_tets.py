# import socket

# HOST = 'localhost'
# PORT = 30002

# def echo_server():
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.bind((HOST, PORT))
#     s.listen(1)

#     # print(s.accept)
#     while 1:
#         conn, addr = s.accept()
#         print(f'Connection by {addr}')
#         while 1:
#             data = conn.recv(1024)
#             if not data:
#                 break
#             conn.sendall(data)
#             print(data.decode('utf-8'))
#         conn.close
#     s.close()

# if __name__ == "__main__":
#     echo_server()

import socket

HOST = 'localhost'
PORT = 30004

def echo_server():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    while 1:
        conn, addr = s.accept()
        print(f'Connection bt {addr}')
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