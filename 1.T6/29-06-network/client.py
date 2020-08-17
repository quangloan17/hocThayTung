#client.py
import socket

HOST = '127.0.0.1'
PORT = 8000

while True:
    text = input('Message: ')
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send(text.encode())
    data = s.recv(4096)
    print(data.decode())
    s.close()
