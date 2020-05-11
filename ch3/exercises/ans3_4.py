import random

target = random.randint(1, 100) #初始化目标值

guess = int(input("Guess a integer [1,100]:"))  #猜一个数

while guess != target:
    if guess > target:
        print("猜大了！")
    else:
        print("猜小了！")
    guess = int(input("Guess a integer [1,100]:"))  #继续猜一个数

print("猜中了")