# 用递归函数的方式实现斐波那契数计算
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
# 打印斐波那契数列
for i in range(10):
    print(fib(i), end=' ')