import socket
# 获取主机地址
HOST = '127.0.0.1'
# 端口号，请大于1023
PORT = 65431
#创建UDP套接字对象
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#将套接字绑定到地址
udp_server.bind((HOST, PORT))
print("UDP Server is working...")
while True:
    #阻塞，等待接收客户端数据
    data, addr = udp_server.recvfrom(1024)
    print('Recieved %s from %s:%s.' % (data, addr[0], addr[1]))
    if data == b'close':  #若接收到'close'
        print('Server is closed!')
        break
    udp_server.sendto(data, addr)  #回发接收到的数据
udp_server.close()  #关闭udp_server套接字
