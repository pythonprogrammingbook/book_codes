#导入Process、Pipe类，os和time模块
from multiprocessing import Process,Pipe
import os, time

#定义pipe_conn1函数
def pipe_conn1(conn):
    msg = "Hello from " + str(os.getpid())
    conn.send(msg)
    print("process_%s send:%s" % (os.getpid(), msg))
    msg = conn.recv()
    print("process_%s received:%s" % (os.getpid(), msg))

#定义pipe_conn2函数
def pipe_conn2(conn):
    msg = conn.recv()
    print("process_%s received:%s" % (os.getpid(), msg))
    msg = "Hello from " + str(os.getpid())
    conn.send(msg)
    print("process_%s send:%s" % (os.getpid(), msg))

if __name__ == "__main__":
    print("Parent Process %s starts" % (os.getpid()))
    conn1, conn2 = Pipe() #实例化一个Pipe对象
    p1 = Process(target=pipe_conn1, args=(conn1, ))
    p2 = Process(target=pipe_conn2, args=(conn2, ))
    #启动子线程
    p1.start()
    p2.start()
    #等待子线程执行完毕
    p1.join()
    p2.join()
    print("Parent Process ends")
