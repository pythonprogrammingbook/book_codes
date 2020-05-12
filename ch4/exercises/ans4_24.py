# 用calendar模块实现闰年检测
import calendar

year = 2019
is_leap = '' if calendar.isleap(year) else ' not'
print(f"{year} is{is_leap} leap year.")