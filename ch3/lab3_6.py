counter = 0           #初始化counter为0
while counter < 10:
    counter += 1      #counter累加1
    if counter % 2 != 0:
        continue      #跳过奇数
    print(counter)    #输出偶数
    