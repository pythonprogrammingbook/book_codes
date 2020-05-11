# 输入半径r，若r小于0，则主动抛出一个异常信息：“半径小于零”；若r大于等于0，则计算圆的面积

import math
r = -2

if r < 0:
    raise ValueError("半径小于零")
else:
    area = r**2*math.pi