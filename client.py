import socket

s = socket.socket()
s.connect(('127.0.0.1',8000))
while True:
    str = input("S: ")
    s.send(str.encode())
    data = s.recv(1024).decode()
    if data == 'q':
        s.send("closing client".encode())
        break
    print(data)
s.close()