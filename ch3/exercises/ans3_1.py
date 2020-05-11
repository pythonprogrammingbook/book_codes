#定义分段函数Relu(x)

def relu(x):
    if x >= 0:
        return x
    else:
        return 0
x = 3
print(f"Relu({x}) is ", relu(x))
print(f"Relu({-x}) is ", relu(-x))
