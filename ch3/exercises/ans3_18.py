# 请用“*”打印出五行五列的等腰直角三角形
N = 5
for i in range(N):
    for j in range(i + 1):
        print("*", end="")
    print()