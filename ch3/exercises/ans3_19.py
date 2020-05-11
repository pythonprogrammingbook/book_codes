# 将一个正整数分解质因数，例如：输入70，输出[2,5,7]

def is_prime(positive_number):
    for i in range(2, positive_number):
        if positive_number % i == 0: # 若能被1和自身之外的数整除，则是合数
            return False
    else:
        return True # 只能被1和自身整除，是质数

prime_factors = [] # 初始化质因数列表
number = int(input("Please input a composite integer:"))
if is_prime(number):
    print("It's a prime number, please enter a composite integer!")
else:
    for i in range(2, number):
        for j in range(2, i):
            if number % j == 0 and is_prime(j):
                prime_factors.append(j)
                number = int(number / j)
                break
print(prime_factors)
