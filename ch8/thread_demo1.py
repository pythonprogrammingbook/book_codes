#导入Thread类，os和time模块
from threading import Thread, get_ident
import os, time

#定义thread_task()函数，输入参数：sec秒
def thread_task(sec):
    print("thread_%d starts and sleep %d seconds" % (get_ident(), sec))
    time.sleep(sec)
    print("thread_%d ends" % (get_ident()))


if __name__ == "__main__":
    print("Parent Process %s starts"%(os.getpid()))
    #实例化三个Thread对象
    t1 = Thread(target=thread_task, args=(3, ), name='NO.1')
    t2 = Thread(target=thread_task, args=(2, ), name='NO.2')
    t3 = Thread(target=thread_task, args=(1, ), name='NO.3')
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
