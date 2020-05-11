x = 80
grade = ''  #初始化变量

if x > 100 or x < 0:  #处理输入数据越界
    print("input data error!")
elif x <= 100 and x >= 90:
    grade = 'A等'
elif x < 90 and x >= 80:
    grade = 'B等'
elif x < 80 and x >= 70:
    grade = 'C等'
elif x < 70 and x >= 60:
    grade = 'D等'
else:
    grade = 'E等'

print(f"grade is {grade}")