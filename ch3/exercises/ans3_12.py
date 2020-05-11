# 捕捉并处理除数为零的异常
a = 12
b = 0

try:
    c = a / b
except ZeroDivisionError as e:
    print(e)
