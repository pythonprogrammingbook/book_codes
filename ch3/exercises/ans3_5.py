heads = 35
feet = 94
chicken = heads #假设全部是鸡
rabbits = 0
# 鸡兔同笼, while解法版
while chicken * 2 + rabbits * 4 != feet: #检查是否符合脚的条件
    chicken -= 1
    rabbits += 1

print(f"Chicken:{chicken}; Rabbits:{rabbits}")