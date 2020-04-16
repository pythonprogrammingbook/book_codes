#导入Thread类，os和time模块
from threading import Thread
import os, time

#定义Thread子类
class ChildThread(Thread):  #继承Thread类
    def __init__(self, sec=5, name=''):  #重写Thread类的__init__()方法
        Thread.__init__(self)  #调用Thread类的__init__()方法
        if name:
            self.name = name   #初始化线程的name属性
        if sec < 0:            #sec必须为非负数
            self.sec = 0
        else:
            self.sec = sec
    #重写Thread类的run()方法
    def run(self):
        print("thread_%d starts and sleep %d seconds" % (self.ident, self.sec))
        time.sleep(self.sec)
        print("thread_%d ends" % (self.ident))

if __name__ == "__main__":
    print("Parent Process %s starts" % (os.getpid()))
    #实例化三个Thread对象
    t1 = ChildThread(sec=3, name='NO.1')
    t2 = ChildThread(sec=2, name='NO.2')
    t3 = ChildThread(sec=1, name='NO.3')
    #启动线程
    t1.start()
    t2.start()
    t3.start()
    #查看线程信息
    print("t1:name=%s,id=%d,is_alive=%s" % (t1.name, t1.ident, t1.is_alive()))
    print("t2:name=%s,id=%d,is_alive=%s" % (t2.name, t2.ident, t2.is_alive()))
    print("t3:name=%s,id=%d,is_alive=%s" % (t3.name, t3.ident, t3.is_alive()))
    #等待线程执行结束
    t1.join()
    t2.join()
    t3.join()
    #查看线程信息
    print("t1:name=%s,id=%d,is_alive=%s" % (t1.name, t1.ident, t1.is_alive()))
    print("t2:name=%s,id=%d,is_alive=%s" % (t2.name, t2.ident, t2.is_alive()))
    print("t3:name=%s,id=%d,is_alive=%s" % (t3.name, t3.ident, t3.is_alive()))
    print("Parent Process ends")