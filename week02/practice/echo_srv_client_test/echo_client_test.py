# import socket

# HOST = 'localhost'
# PORT = 30002

# def echo_client():
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.connect((HOST, PORT))

#     while 1:
#         data = input("input> ")
#         if data == 'exit':
#             break

#         s.sendall(data.encode())
#         data = s.recv(1024)
#         if not data:
#             break
#         else:
#             print(data.decode('utf-8'))

#     s.close()

# if __name__ == "__main__":
#     echo_client()


import socket

HOST = 'localhost'
PORT = 30004


def echo_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while 1:
        data = input('input> ')
        if data == 'exit':
            break
        s.sendall(data.encode())
        
        data = s.recv(1024)
        if not data:
            break
        print(data.decode('utf-8'))
    s.close()


if __name__ == "__main__":
    echo_client()
