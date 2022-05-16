#!/bin/python3
import socket
obj = socket.socket()
obj.bind(("192.168.100.3", 7777))
obj.listen(2)
while True:
    obj2, host = obj.accept()
    data = obj2.recv(1500)
    print(data.decode())