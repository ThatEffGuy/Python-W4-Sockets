import socket

s = socket.socket()
host = socket.gethostname()
port = 4444

s.bind((host,port))
s.listen(10)
print('waiting for connection...')

while True:
    conn, addr = s.accept()
    data = conn.recv(1024)
    d = data.decode().split(',')
    print(d)
    print(type(d))
    data_add = int(d[0]) +int(d[1])
    conn.sendall(str(data_add).encode())

conn.close()