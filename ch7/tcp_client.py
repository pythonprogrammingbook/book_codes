import socket
# 设置服务器地址
HOST = '127.0.0.1'
# 服务器端口号
PORT = 65432
#创建TCP套接字对象
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#连接服务器
tcp_client.connect((HOST, PORT))
while True:
    send_data = input("Please input data or 'close' command to send: ")
    tcp_client.sendall(send_data.encode()) #发送数据
    if send_data == 'close':
        print("Client is closed.")
        break
    info = tcp_client.recv(1024).decode()  #接受服务器数据
    print("Recieved from server：" + info)
tcp_client.close()                         #关闭tcp_client套接字
