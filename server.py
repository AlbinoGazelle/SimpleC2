import socket
from threading import *
#create initial socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#define port
port = 8000
#bind to specific port and on valid interface
serversocket.bind(('', port))
print(f"Bound to port {port}")
#create class
class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        #start thread
        self.start()
    
    def run(self):
        while 1:
            data = self.sock.recv(1024).decode()
            print(f"recieved data from client: {data}")
            send_data = input("What do you want to send to client: \n")
            self.sock.send(send_data.encode())

serversocket.listen(5)
print ('server started and listening')
while 1:
    clientsocket, address = serversocket.accept()
    client(clientsocket, address)