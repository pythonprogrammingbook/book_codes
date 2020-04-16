#导入Thread, RLock类
from threading import Thread, RLock
#初始化全局变量
g_sum = 0
sum = 499995000000
def child_thread():
    global g_sum
    rlock.acquire()  #获取可重入锁
    rlock.acquire()  #获取可重入锁
    for i in range(100000):
        g_sum = g_sum + i
    rlock.release()  #释放可重入锁
    rlock.release()  #释放可重入锁

if __name__ == "__main__":
    threads = [Thread(target=child_thread) for i in range(100)]
    rlock = RLock() #创建可重入锁
    for t in threads:
        t.start()   #启动所有线程
    for t in threads:
        t.join()    #等待线程结束
    print("g_sum should be:%s;g_sum:%s"%(sum,g_sum))
