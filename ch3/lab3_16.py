try:
    f = open('integers.txt', 'w+')
    num = int(input("Enter an integer: "))
except ValueError:
    #当输入数据类型异常发生时，输出提示信息
    print('Error: Integer type is required!')
else:  #没有异常发生，将num写入文件
    f.write(str(num))
    print('Write num into file.')
finally:  #不管是否发生异常，关闭文件，释放资源
    f.close()
    print('Finally, close the file.')