# 获取CPU的核数N，创建N个线程，每个线程输出所在进程的进程id和自己的线程标识符，然后休眠5ms
import threading, os, time
N = os.cpu_count()  # 获取CPU的核数N

# 定义任务
def task():
    print(f"pid is {os.getpid()}. thread_id is {threading.get_ident()}")  # 输出pid和线程标识符
    time.sleep(0.005)  #休眠5ms


if __name__ == '__main__':
    print(f"CPU has {N} Cores.")
    print(f"Main process id:{os.getpid()}.")
    print("Start threading...")
    threads = [threading.Thread(target=task) for _ in range(N)]
    for thread in threads:
        thread.start()
    for thread in threads:
        if thread.is_alive:
            thread.join()
    print("Main process ends.")