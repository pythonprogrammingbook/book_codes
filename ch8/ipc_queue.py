#导入Process类，Queue类，os和time模块
from multiprocessing import Process,Queue
import os, time

#定义producer_task()函数
def producer_task(q):
    for i in range(3):
        if not q.full(): #若队列不满，则将消息放入队列
            msg = "msg" + str(i)
            q.put(msg)
            print("producer_%s puts:%s" % (os.getpid(), msg))
        time.sleep(0.1)
#定义consumer_task()函数
def consumer_task(q):
    for i in range(3):
        #最多等待2秒，从队列取出消息
        msg = q.get(timeout=2)
        print("consumer_%s gets:%s" % (os.getpid(), msg))
        time.sleep(0.1)

if __name__ == "__main__":
    print("Parent Process %s starts" % (os.getpid()))
    q = Queue() #实例化一个Queue对象
    producer = Process(target=producer_task, args=(q, ), name='producer')
    consumer = Process(target=consumer_task, args=(q, ), name='consumer')
    #启动子进程
    producer.start()
    consumer.start()
    #等待子进程执行完毕
    producer.join()
    consumer.join()
    print("Parent Process ends")
