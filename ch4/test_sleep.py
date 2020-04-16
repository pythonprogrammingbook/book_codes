import time
start_time = time.time() #记录开始时间
time.sleep(3.38)  #挂起3.38秒
end_time = time.time()  #记录结束时间
print('sleep:{0:.3f}s'.format(end_time-start_time))

