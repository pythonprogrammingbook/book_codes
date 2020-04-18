while True:  
    try:  
        dividend = int(input('Enter an integer dividend:'))#从键盘输入被除数  
        divisor = int(input('Enter an integer divisor:'))   #从键盘输入除数  
        result = dividend / divisor         
    except ZeroDivisionError:                         #捕捉除数为零异常  
    # 当除数为零异常发生，输出提示信息  
        print('Error: divisor can NOT be Zero!')  
    except ValueError:                                #捕捉输入数据类型异常  
    # 当输入数据类型异常发生，输出提示信息  
        print('Error:Ingeter type is required!')  
    else:   #没有异常发生，输出计算结果  
        print('Result is {0:.2f}'.format(result))  
        break 
