# 获取CPU的核数N，创建N个进程，每个进程输出进程id，然后休眠5ms
import multiprocessing, os, time
N = multiprocessing.cpu_count()  # 获取CPU的核数N


# 定义任务
def task():
    print(f"process id is {os.getpid()}.")  # 输出进程id
    time.sleep(0.005)  #休眠5ms

if __name__ == '__main__':
    print(f"CPU has {N} Cores.")
    print(f"Main process id:{os.getpid()}.")
    print("Start multiprocessing...")
    processes = [multiprocessing.Process(target=task) for _ in range(N)]
    for process in processes:
        process.start()
    for process in processes:
        if process.is_alive:
            process.join()
    print("Main process ends.")
