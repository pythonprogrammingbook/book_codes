# 设计一个计算圆面积的函数、输入半径r，返回圆的面积，用Google风格撰写好函数的文档字符串
def circle_area(r):
    """计算圆的面积

    Args:
        r ([float]): [圆的半径]

    Returns:
        [float]: [圆的面积]
    """
    import math
    area = math.pi*r**2 #计算圆的面积
    return area

print(f"area:{circle_area(1)}")