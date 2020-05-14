# 实现一个问答机器人服务器，接收客户端发的计算请求(算式)，返回计算结果给客户端
import socket
# 请设置服务器IP地址
HOST = '192.168.0.101'
# 端口号，请大于1023
PORT = 65432
#创建TCP套接字对象
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#将套接字绑定到地址
tcp_server.bind((HOST, PORT))
#开始TCP监听
tcp_server.listen()
print("Server starts listening...")
#接受客户端连接
while True:
    conn, addr = tcp_server.accept()
    print("Connected by", addr)
    while True:
        question = conn.recv(1024).decode()  #接收问题
        if question:
            print(f"From {addr}:{question}")  #显示接收到的问题
            conn.sendall(str(eval(question)).encode())  #发送答案
        else:
            break
    conn.close()  #关闭conn套接字
tcp_server.close()  #关闭tcp_server套接字
