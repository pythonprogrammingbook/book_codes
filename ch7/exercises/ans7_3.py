# 请实现一个连接www.baidu.com网站的TCP客户端
# 请先用ping www.baidu.com 确保能ping通目标网站

import socket

ip = socket.gethostbyname("www.baidu.com")  # 请使用能ping通的网站域名
port = 80
print(f"Target IP:{ip}")

# 用try语句捕捉创建套接字失败的情况
try:
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket is created successfully!")
except socket.error as err:
    print(f"fail with error:{err}")

tcp_client.connect((ip, port)) #建立与baidu的连接
print(f"The socket has successfully connected to baidu on ({ip}:{port})")
tcp_client.close() # 关闭TCP连接