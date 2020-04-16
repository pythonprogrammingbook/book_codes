#导入Process类, os和time模块
from multiprocessing import Pool
import os, time
#初始化全局变量
g_num = 100

def child_process(i):
    global g_num
    g_num += 1
    print("g_num:%s; pid:%s" % (g_num, os.getpid()))
    time.sleep(1)

if __name__ == "__main__":
    p = Pool() #实例化一个进程池对象
    p.map_async(child_process, range(3))
    p.close()  #关闭进程池对象，不在接收新的任务
    p.join()   #等待子线程执行完毕
    print("Parent pid:%s; g_num:%s" % (os.getpid(), g_num))
