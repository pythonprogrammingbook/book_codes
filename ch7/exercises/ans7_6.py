# 实现一个问答机器人服务器，接收客户端发的计算请求(算式)，返回计算结果给客户端。
import socketserver

# 创建一个继承自socketserver.BaseRequestHandler的类
class MyServer(socketserver.BaseRequestHandler):
    #方法名必须是handle
    def handle(self):
        conn = self.request  # request里封装了所有请求的数据

        while True:
            question = conn.recv(1024).decode()  #接收问题
            if question:
                print(f"From {self.client_address}:{question}")  #显示接收到的问题
                conn.sendall(str(eval(question)).encode())  #发送答案
            else:
                break


if __name__ == '__main__':
    # 将MyServer类，连同服务器的IP地址和端口号，作为参数一同传递给ThreadingTCPServer
    server = socketserver.ThreadingTCPServer(('192.168.0.101', 65432),
                                             MyServer)  # 请设置服务器IP地址和端口号
    print("Start ThreadingTCPServer!")
    # 启动ThreadingTCPServer，服务器将一直保持运行状态
    server.serve_forever()