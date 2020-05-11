# 输出[10000, 99999]之间的回文数
p_numbers = [i for i in range(10000, 100000) if str(i) == str(i)[-1::-1]]
print(p_numbers)