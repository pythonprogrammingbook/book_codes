import unittest, math
import circle_func  # 导入被测试模块

# 创建一个继承unittest.TestCase的类
class Tests(unittest.TestCase):
    # 创建test_为前缀的方法，里面用self.assert方法调用被测试的对象
    def test_area(self):
        self.assertAlmostEqual(circle_func.area(1), math.pi)

    # 创建test_为前缀的方法，里面用self.assert方法调用被测试的对象
    def test_circumference(self):
        self.assertAlmostEqual(circle_func.circumference(1), math.pi*2)
        self.assertl

#5.unittest.main()作为主函数入口
if __name__ == '__main__':
    unittest.main()