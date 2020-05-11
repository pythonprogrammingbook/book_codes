year, month = input("Please input year.month:").split('.')  # 获取年份.月份输入
year = int(year)
month = int(month)
days = 0
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)  # 计算闰年标志

if month in (1, 3, 5, 7, 8, 10, 12):
    days = 31
elif month in (4, 6, 9, 11):
    days = 30
elif is_leap:
    days = 29
else:
    days = 28

print(f"{year}.{month} has {days} days")

