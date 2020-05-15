# 对比多线程和多进程在多核CPU上执行计算密集和IO密集型任务的效率
import threading, multiprocessing
import os, time,math
# 定义计算密集型任务
def task_cpu(n):
    x = 0.0
    for i in range(2,n):
        x += sum([math.sin(i) for i in range(i)])
# 定义IO密集型任务
def task_io(n):
    for _ in range(n):
        time.sleep(0.005)

if __name__ == '__main__':
    # 测试多线程计算密集型任务
    print("启动多线程计算密集型任务")
    start = time.time()
    threads = [
        threading.Thread(target=task_cpu, args=(3000, ))
        for i in range(os.cpu_count())
    ]
    for thread in threads:
        thread.start()
    for thead in threads:
        if thread.is_alive():
            thread.join()
    end = time.time()
    print(f"多线程计算密集型任务耗时：{end-start}秒")
    # 测试多进程计算密集型任务
    print("启动多进程计算密集型任务")
    start = time.time()
    processes = [
        multiprocessing.Process(target=task_cpu, args=(3000, ))
        for i in range(os.cpu_count())
    ]
    for process in processes:
        process.start()
    for process in processes:
        if process.is_alive():
            process.join()
    end = time.time()
    print(f"多进程计算密集型任务耗时：{end-start}秒")

    # 测试多线程IO密集型任务
    print("启动多线程IO密集型任务")
    start = time.time()
    threads = [
        threading.Thread(target=task_io, args=(100, ))
        for i in range(os.cpu_count())
    ]
    for thread in threads:
        thread.start()
    for thead in threads:
        if thread.is_alive():
            thread.join()
    end = time.time()
    print(f"多线程IO密集型任务耗时：{end-start}秒")
    # 测试多进程IO密集型任务
    print("启动多进程IO密集型任务")
    start = time.time()
    processes = [
        multiprocessing.Process(target=task_io, args=(100, ))
        for i in range(os.cpu_count())
    ]
    for process in processes:
        process.start()
    for process in processes:
        if process.is_alive():
            process.join()
    end = time.time()
    print(f"多进程IO密集型任务耗时：{end-start}秒")