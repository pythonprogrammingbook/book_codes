#导入Thread类, os和time模块
from threading import Thread, get_ident
import os, time
#初始化全局变量
g_num = 100

def child_thread():
    global g_num
    g_num += 1
    print("g_num:%s; thread:%s; pid:%s" % (g_num, get_ident(), os.getpid()))
    time.sleep(1)

if __name__ == "__main__":
    threads = [Thread(target=child_thread) for i in range(3)]
    for t in threads:
        t.start()   #启动所有线程
    for t in threads:
        t.join()    #等待线程结束
    print("Parent pid:%s; g_num:%s" % (os.getpid(), g_num))


