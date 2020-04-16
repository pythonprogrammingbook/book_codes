input_list = []
if not input_list: #若输入列表为空
    print('list is empty')

list1 = [x**2 for x in range(1,11)] #生成1到10的平方的列表
Celsius = [39.2, 36.5, 37.3, 37.8] 
Fahrenheit = [ ((float(9)/5)*x + 32) for x in Celsius ]
accumulation_sum = sum([i for i in range(101)])
[(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2]

list1 = []
for x in range(1,30):
    for y in range(x, 30):
        for z in range(y, 30):
            if x**2 + y**2 == z**2:
                list1.append((x,y,z))
                no_primes = [num for num in range(3, 100) for n in range(2, num) if num%n == 0]
                