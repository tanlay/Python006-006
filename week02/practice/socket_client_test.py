import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f"s1: {s}")

s.connect(('www.httpbin.org', 80))
print(f"s2: {s}")

s.send(b'GET / HTTP/1.1\r\nHost:time.geekbang.org\r\nConnection:close\n\r\n')


buffer = []

while 1:
    data = s.recv(1024)
    if data:
        buffer.append(data)
    else:
        break

s.close()

resp = b"".join(buffer)
header, html = resp.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# print(html.decode('utf-8'))
with open('index.html', 'wb') as f:
    f.write(html)
