# 编写一个求和函数，输入任意个数值，返回所有输入参数的和
def calc_sum(*args):
    return sum(args)

print(f"sum is {calc_sum(1,2,3,4,5,6)}")