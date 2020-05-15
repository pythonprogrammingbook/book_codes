# 获取CPU的核数N，创建N个线程。
# 每个线程对全局变量做10000次加1
# 查看全局变量最终的结果是否等于10000*N，并分析为什么？
import threading, os, time
N = os.cpu_count()  # 获取CPU的核数N
g_counter = 0       # 初始化全局变量
# 定义任务
def task(n):
    global g_counter
    for i in range(n):
        g_counter += 1

if __name__ == '__main__':
    print(f"CPU has {N} Cores.")
    print("Start threading...")
    n = 1000000
    threads = [
        threading.Thread(target=task, args=(n, )) for _ in range(N)
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        if thread.is_alive:
            thread.join()
    print(f"The g_counter is {g_counter}, expected:{N*n}")