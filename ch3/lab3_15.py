dividend = eval(input('Please Enter a dividend:')) #从键盘输入被除数  
divisor = eval(input('Please Enter a divisor:'))   #从键盘输入除数  
try:
    result = dividend / divisor
except ZeroDivisionError:  #捕捉除数为零异常  
    # 当除数为零异常发生，输出提示信息  
    print('Input Error: divisor can NOT be Zero!') 
