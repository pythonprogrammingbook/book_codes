# 创建映射表
month_seasons = {1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring', 6: 'Summer',
                 7: 'Summer', 8: 'Summer', 9: 'Autumn', 10: 'Autumn', 11: 'Autumn', 12: 'Winter'}
# 获取用户输入
input_month = int(input("Please input month number[1~12]:"))
if input_month < 1:     #输入超下限，强制取1
    input_month = 1
elif input_month > 12:  #输入超下限，强制取12
    input_month = 12
# 查找对应的季节
season = month_seasons[input_month]
print(f"Month:{input_month} is {season}.")