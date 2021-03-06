#导入Pool类，os和time模块
from multiprocessing import Pool
import os, time
#定义一个任务函数
def task(id):
    print('child process %s works on the task %s' % (os.getpid(), id))
    time.sleep(2)  #休眠2秒

if __name__ == "__main__":
    print("Parent Process %s starts" % os.getpid())
    p = Pool()  #实例化一个进程池对象
    for i in range(20):
        p.apply_async(task, args=(i,))  #用非阻塞方式调用task函数
    p.close()  #关闭进程池对象，不在接收新的任务
    p.join()  #等待子线程执行完毕
    print("Parent Process ends")