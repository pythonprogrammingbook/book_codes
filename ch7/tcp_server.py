import socket
# 获取主机地址
HOST = '127.0.0.1'
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
conn, addr = tcp_server.accept()
print("Connected by", addr)
while True:
    data = conn.recv(1024)  #接收数据
    if data == b'close':    #若接收到'close'
        print('Server is closed!')
        break
    print(data)             #显示接收到的数据
    conn.sendall(data)      #回发接收到的数据
conn.close()                #关闭conn套接字
tcp_server.close()          #关闭tcp_server套接字