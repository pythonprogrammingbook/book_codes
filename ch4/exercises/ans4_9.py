# 用random.randint(1,10)，随机生成一个有100个元素的列表，然后按照元素出现次数的高低，从高到底排序并输出
import random

numbers = [random.randint(1, 10) for i in range(100)]
numbers_info = {}
def sorted_by_freq(numbers):
    for number in numbers: # 遍历随机数列表
        if number not in numbers_info: # 若该元素没有统计过
            numbers_info[number] = numbers.count(number) # 以该元素为key，出现次数为value，加入字典
    return sorted(numbers_info.items(), key=lambda item: item[1], reverse=True) # 降序排序后返回

ans = sorted_by_freq(numbers)
print(ans)