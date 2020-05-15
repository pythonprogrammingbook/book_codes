# 请基于Semaphore类，解决题目8.5遇到的问题，让全局变量的最终结果达到预期。
from threading import Semaphore
import threading, os, time
N = os.cpu_count()  # 获取CPU的核数N
g_counter = 0  # 初始化全局变量

# 定义任务
def task(n, sem):
    global g_counter
    sem.acquire()  #获取信号量
    for i in range(n):
        g_counter += 1
    sem.release()  #释放信号量

if __name__ == '__main__':
    print(f"CPU has {N} Cores.")
    print("Start threading...")
    n = 1000000
    sem = Semaphore()  #创建信号量
    threads = [threading.Thread(target=task, args=(n, sem)) for _ in range(N)]
    for thread in threads:
        thread.start()
    for thread in threads:
        if thread.is_alive:
            thread.join()
    print(f"The g_counter is {g_counter}, expected:{N*n}")