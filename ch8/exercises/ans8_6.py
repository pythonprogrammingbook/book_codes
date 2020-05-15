# 获取CPU的核数N，创建N个线程。每个线程使用同一个函数作为target输入，
# 在该函数中，定义一个局部变量，并对它做1000000次加1，
# 查看局部变量的最终结果是否等于1000000，并分析为什么？
import threading, os, time
N = os.cpu_count()  # 获取CPU的核数N
# 定义任务
def task(n):
    counter = 0
    for i in range(n):
        counter += 1   #局部变量n次自加1
    print(f"counter is {counter} in thread:{threading.get_ident()}")

if __name__ == '__main__':
    print(f"CPU has {N} Cores.")
    print("Start threading...")
    n = 1000000
    threads = [threading.Thread(target=task, args=(n, )) for _ in range(N)]
    for thread in threads:
        thread.start()
    for thread in threads:
        if thread.is_alive:
            thread.join()