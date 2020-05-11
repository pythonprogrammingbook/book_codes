# 输出斐波那契数列 F(0)=1，F(1)=1, F(n)=F(n-1)+F(n-2)（n>=2，n∈N*）
fibonacci = [1, 1]
a, b = 1, 1  #初始化斐波那契数列的首二项
N = 10
for _ in range(N):
    a, b = b, a + b
    fibonacci.append(b)

print(fibonacci)
