#导入Thread类
from threading import Thread
#初始化全局变量
g_sum = 0
sum = 499995000000
def child_thread():
    global g_sum
    for i in range(100000):
        g_sum = g_sum + i

if __name__ == "__main__":
    threads = [Thread(target=child_thread)
               for i in range(100)]
    for t in threads:
        t.start()   #启动所有线程
    for t in threads:
        t.join()    #等待线程结束
    print("g_sum should be:%s;g_sum:%s"%(sum,g_sum))


