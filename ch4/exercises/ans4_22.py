# 小学生算术练习器：随机生成100以内的自然数，并随机选择加、减、乘、除四种运算中的一种，并判断计算结果是否正确
import random
operators = {'+':'+', '-':'-', 'x':'*', '÷':'/'}
num1 = random.randint(1, 100)  # 随机生成第一个数
num2 = random.randint(1, 100)  # 随机生成第二个数
operator = random.choice(list(operators.keys()))  # 随机选择运算
answer = eval(str(num1) + operators[operator] + str(num2)) # 计算答案
user_input = eval(input(f"请计算{num1} {operator} {num2}:"))  #获得用户计算结果
if abs(answer - user_input) < 0.001:
    print('答对了!')
else:
    print("答错了，正确答案是{0:.3f}".format(answer))

