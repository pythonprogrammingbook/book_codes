# 请实现一个问答机器人的客户端，客户端随机生成100以内的自然数并随机选择加、减、乘、除四种运算中的一种，
# 然后把算式发给服务器端，等待、接收并输出服务器端的答案。

import random
operators = {'+': '+', '-': '-', 'x': '*', '÷': '/'}
import socket
# 请设置服务器IP地址
HOST = '192.168.0.101'
# 服务器端口号
PORT = 65432
#创建TCP套接字对象
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#连接服务器
tcp_client.connect((HOST, PORT))
for _ in range(10):
    num1 = random.randint(1, 100)  # 随机生成第一个数
    num2 = random.randint(1, 100)  # 随机生成第二个数
    operator = random.choice(list(operators.keys()))  # 随机选择运算
    question = str(num1) + operators[operator] + str(num2) # 问题
    #发送问题给服务器
    tcp_client.sendall(question.encode())
    #接受服务器答案
    answer = tcp_client.recv(1024).decode()
    #显示答案
    print(f"{question} = {answer}")
tcp_client.close()  #关闭tcp_client套接字
