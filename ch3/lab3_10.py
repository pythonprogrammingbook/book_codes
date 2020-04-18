a, b = 9, 3  # 初始化a,b，a必须大于b  
greatest_common_divisor, least_common_multiple = 0,0  
for factor in range(b, 0, -1):  
    #若a,b都能整除factor  
    if b%factor == 0 and a%factor == 0:   
        #找到最大公约数和最小公倍数  
        greatest_common_divisor, least_common_multiple = factor, a*b//factor
        break  
print(greatest_common_divisor, least_common_multiple)
