# 请实现一个生产者-消费者模式的多线程程序，
# 三个生产者负责随机生成100以内的自然数并随机选择加、减、乘、除四种运算中的一种，
# 然后把算式发给消费者，消费者计算并打印出结果

#导入Process类，Queue类，os、time和random模块
from multiprocessing import Process, Queue
import os, time, random
operators = {'+': '+', '-': '-', 'x': '*', '÷': '/'}

def generate_question():
    num1 = random.randint(1, 100)  # 随机生成第一个数
    num2 = random.randint(1, 100)  # 随机生成第二个数
    operator = random.choice(list(operators.keys()))    # 随机选择运算
    return str(num1) + operators[operator] + str(num2)  # 问题

#定义消费者函数
def producer(q):
    for _ in range(3):
        if not q.full():  #若队列不满，则将消息放入队列
            msg = ":".join([generate_question(),str(os.getpid())]) # 将问题和pid合并为消息
            q.put(msg)
            print(f"producer_{os.getpid()} puts:{msg}.")
        time.sleep(0.1)

#定义消费者函数
def consumer(q):
    for _ in range(9): # 解答三个生产者的各三个问题
        #最多等待2秒，从队列取出消息
        msg = q.get(timeout=2)
        question, pid = msg.split(':') #从消息中提取出问题和pid
        print(f"from producer {pid}, {question} = {eval(question)}")

if __name__ == "__main__":
    q = Queue()  #实例化一个Queue对象
    producers = [Process(target=producer, args=(q,), name='producer'+str(i)) for i in range(3)]
    c =  Process(target=consumer, args=(q, ), name='consumer')
    #启动进程
    c.start()
    for p in producers:
        p.start()
    #等待消费者进程执行完毕
    c.join()
