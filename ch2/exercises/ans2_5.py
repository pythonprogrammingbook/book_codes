year = 2017  #修改year变量后,运行程序

is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 500 == 0)

msg = "is" if is_leap else "is not"
print(f'{year} {msg} leap year')