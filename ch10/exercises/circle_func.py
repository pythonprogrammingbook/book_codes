# 实现圆的周长和面积的计算
import math

def area(r):
    """计算圆的面积

    Args:
        r ([float]): [圆的半径]

    Returns:
        [float]: [圆的面积]
    """

    return math.pi * r**2  #计算圆的面积


def circumference(r):
    """计算圆的周长

    Args:
        r ([float]): [圆的半径]

    Returns:
        [float]: [圆的周长]
    """
    return 2 * math.pi * r