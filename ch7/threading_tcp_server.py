import socketserver
# 创建一个继承自socketserver.BaseRequestHandler的类
class MyServer(socketserver.BaseRequestHandler):
    #方法名必须是handle
    def handle(self):
        conn = self.request  # request里封装了所有请求的数据
        conn.sendall(b"Welcome ThreadingTCPServer!")
        while True:
            data = conn.recv(1024)
            if data == b"close":  #若接收到'close',则关闭连接
                print('Connection is closed!')
                break
            print("Recieve %s from %s" % (data, self.client_address))
            conn.sendall(data)  #回发接收到的数据

if __name__ == '__main__':
    # 将MyServer类，连同服务器的IP地址和端口号，作为参数一同传递给ThreadingTCPServer
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 65432), MyServer)
    print("Start ThreadingTCPServer!")
    # 启动ThreadingTCPServer，服务器将一直保持运行状态
    server.serve_forever()