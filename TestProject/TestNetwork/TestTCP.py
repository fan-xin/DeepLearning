import socket#穿件socket,使用IPv4的协议，使用面向对象的流s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#发起链接s.connect(('www.google.com',80))