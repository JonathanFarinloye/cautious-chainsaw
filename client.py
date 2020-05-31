import socket
import time
from multiprocessing import Process

sock = socket.socket()
# host = input(str("Enter the hostname of the server: "))
# print("server will start on host: ", host)
port = 3421
sock.connect(('serveo.net', port))
print("Connected to chat server")
print("To quit type {quit}")

while 1:
    incoming_message= sock.recv(1024)
    incoming_message=incoming_message.decode()
    print(" Server :", incoming_message)
    message = str(input(">>> "))
    if message == "{quit}":
        sock.send(b"Client has left")
        quit()
    else:
        message = message.encode()
        sock.send(message)
        print("Sent...")