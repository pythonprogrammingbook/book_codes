#导入Thread, RLock类
from threading import Thread, RLock
#初始化全局变量
g_sum = 0
sum = 499995000000
def child_thread(rl):
    global g_sum
    rl.acquire()  #获取可重入锁
    rl.acquire()  #获取可重入锁
    for i in range(100000):
        g_sum = g_sum + i
    rl.release()  #释放可重入锁
    rl.release()  #释放可重入锁

if __name__ == "__main__":
    rl = RLock()  #创建可重入锁
    threads = [Thread(target=child_thread, args=(rl,)) for i in range(100)]
    for t in threads:
        t.start()   #启动所有线程
    for t in threads:
        t.join()    #等待线程结束
    print("g_sum should be:%s;g_sum:%s"%(sum,g_sum))
