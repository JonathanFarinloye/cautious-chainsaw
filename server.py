import socket
import time
from multiprocessing import Process

sock = socket.socket()
# host = socket.gethostbyname("phantom")
# print("server will start on host: ", host)
port = 3421
sock.bind(('127.0.0.1', port))
print("server done binding to host and port successfully")
print("server is waiting for incoming connections")
sock.listen(1)
connection, address = sock.accept()
print(address, " Has connected to the server and is now online...")

while 1:
    message = str(input(">>>")).encode()
    connection.send(message)
    print("Sent...")
    in_message = connection.recv(1024)
    in_message = in_message.decode()
    print(" Client:", in_message)