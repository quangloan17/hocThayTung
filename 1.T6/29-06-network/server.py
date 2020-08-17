#server.py

import socket
HOST = '127.0.0.1' #Để 0.0.0.0: Nhận dạng tất cả public internet
PORT = 8000 #Cổng test trong ứng dụng web

s = socket.socket()
s.bind((HOST,PORT))
s.listen()

while True:
    conn,addr = s.accept()
    data = conn.recv(4096) #recv là receive nhận 4 bytes
    msg = data.decode()
    resp = 'Tôi đã nhận được tin nhắn:' + msg
    conn.send(resp.encode())
    conn.close()
