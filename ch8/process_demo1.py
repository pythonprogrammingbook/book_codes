#导入Process类，os和time模块
from multiprocessing import Process
import os, time

#定义child_process()函数，输入参数：sec秒
def child_process(sec):
    print("child_process_%d starts and sleep %d seconds" % (os.getpid(), sec))
    time.sleep(sec)
    print("child_process_%d ends" % (os.getpid()))

if __name__ == "__main__":
    print("Parent Process %s starts" % (os.getpid()))
    #实例化三个Process对象
    p1 = Process(target=child_process, args=(3, ), name='NO.1')
    p2 = Process(target=child_process, args=(2, ), name='NO.2')
    p3 = Process(target=child_process, args=(1, ), name='NO.3')
    print("Child Processes start")
    #启动子进程
    p1.start()
    p2.start()
    p3.start()
    #查看子进程信息
    print("p1:name=%s,pid=%d,is_alive=%s" % (p1.name,p1.pid,p1.is_alive()))
    print("p2:name=%s,pid=%d,is_alive=%s" % (p2.name,p2.pid,p2.is_alive()))
    print("p3:name=%s,pid=%d,is_alive=%s" % (p3.name,p3.pid,p3.is_alive()))
    #等待子进程执行结束
    p1.join()
    p2.join()
    p3.join()
    #查看子进程信息
    print("p1:name=%s,pid=%d,is_alive=%s" % (p1.name, p1.pid, p1.is_alive()))
    print("p2:name=%s,pid=%d,is_alive=%s" % (p2.name, p2.pid, p2.is_alive()))
    print("p3:name=%s,pid=%d,is_alive=%s" % (p3.name, p3.pid, p3.is_alive()))
    print("Parent Process ends")
