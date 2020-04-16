import socket
# 设置服务器地址
HOST = '127.0.0.1'
# 服务器端口号
PORT = 65431
#创建UDP套接字对象
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    send_data = input("Please input data or 'close' command to send: ")
    udp_client.sendto(send_data.encode(),(HOST, PORT))  #发送数据
    if send_data == 'close':
        print("Client is closed.")
        break
    info = udp_client.recv(1024).decode()  #接受服务器数据
    print("Recieved from server：" + info)
udp_client.close()  #关闭udp_client套接字
