# import socket
import requests
r = requests.get("http://192.168.0.105")
print(r.text)
# o = socket.socket()
# same port as the server
# o.connect(("192.168.0.105", 80))
# print("connected")
# while True:
#     send_c_msg = input("send message: ")
#     msg = o.recv(36830).decode("utf-16")
#     print(msg)
#     o.send(send_c_msg.encode("utf-16"))
#     print(msg)
