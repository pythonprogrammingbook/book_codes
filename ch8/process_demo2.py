#导入Process类，os和time模块
from multiprocessing import Process
import os, time
#定义Process子类
class ChildProcess(Process):  #继承Process类
    def __init__(self, sec=5, name=''): #重写Process类的__init__()方法
        Process.__init__(self)  #调用Process类的__init__()方法
        if name:
            self.name = name   #为子进程初始化name属性
        if sec < 0:            #sec必须为非负数
            self.sec = 0
        else:
            self.sec = sec
    #重写Process类的run()方法
    def run(self):
        print("child_process_%d starts and sleep %d seconds" %(os.getpid(), self.sec))
        time.sleep(self.sec)
        print("child_process_%d ends" % (os.getpid()))

if __name__ == "__main__":
    print("Parent Process %s starts" % (os.getpid()))
    #实例化三个Process对象
    p1 = ChildProcess(sec=5, name='NO.1')
    p2 = ChildProcess(sec=4, name='NO.2')
    p3 = ChildProcess(sec=3, name='NO.3')
    print("Child Processes start")
    #启动子进程
    p1.start()
    p2.start()
    p3.start()
    #查看子进程信息
    print("p1:name=%s,pid=%d,is_alive=%s" % (p1.name, p1.pid, p1.is_alive()))
    print("p2:name=%s,pid=%d,is_alive=%s" % (p2.name, p2.pid, p2.is_alive()))
    print("p3:name=%s,pid=%d,is_alive=%s" % (p3.name, p3.pid, p3.is_alive()))
    #等待子进程执行结束
    p1.join()
    p2.join()
    p3.join()
    #查看子进程信息
    print("p1:name=%s,pid=%d,is_alive=%s" % (p1.name, p1.pid, p1.is_alive()))
    print("p2:name=%s,pid=%d,is_alive=%s" % (p2.name, p2.pid, p2.is_alive()))
    print("p3:name=%s,pid=%d,is_alive=%s" % (p3.name, p3.pid, p3.is_alive()))
    print("Parent Process ends")