from math import pi #导入π常量

class Circle():
    """ 定义圆类 """  
    def __init__(self, r=1.0): #初始化属性r
        self.r = r

    def get_radius(self): #获取半径的值
        return self.r
    
    def set_radius(self, r):  #设置半径的值
        self.r = r    

    def calc_circumference(self): #计算圆周长
        return 2 * pi * self.r

    def calc_area(self):  #计算圆面积
        return pi * self.r ** 2

circle_a = Circle()
print(circle_a.calc_area())
        
