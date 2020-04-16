#导入Thread, Condition类
from threading import Thread, Condition
g_num = 0  #全局资源
#定义消费者,负责消耗一个单位资源
def consumer(con, id):
    global g_num
    with con:
        print('Consumer %s waiting ...'%(id))
        con.wait()
        g_num -= 1  #消耗一个单位资源
        print('Consumer %s consumed one resource' % (id))

#定义生产者,负责生产十个单位资源,然后通知消费者消费
def producer(con):
    global g_num
    with con:
        print('Producer produce ten resources')
        g_num += 10
        con.notifyAll() #通知所有消费者消费资源

if __name__ == '__main__':
    con = Condition() #实例化条件对象
    #制造5个消费者和1个生产者
    cs = [Thread(target=consumer,args=(con,i)) for i in range(5)]
    p = Thread(target=producer,args=(con, ))
    for c in cs:
        c.start()  #启动消费者
    p.start()  #启动生产者
    for c in cs:
        c.join()  #等待消费者完成消费
    print("g_num is left:%s. Exit..." % (g_num))
