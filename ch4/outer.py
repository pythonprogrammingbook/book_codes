x = 10 #全局变量

def outer():
    x = 20  #对outer()来说是局部变量
            #对inner()来说是非局部变量
    def inner():
        x = 30 #对inner()来说是局部变量
        print("From inner():x={0:d}".format(x))
    inner()
    print("From outer():x={0:d}".format(x))

outer()
print("From module:x={0:d}".format(x))
