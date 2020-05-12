# 请用time模块测量一个Python语句：p = [i for i in range(10000, 100000) if str(i) == str(i)[-1::-1]] 的执行时间
import time
start = time.time()
p = [i for i in range(10000, 100000) if str(i) == str(i)[-1::-1]]
end = time.time()
print(f"Excution time:{end-start} s")