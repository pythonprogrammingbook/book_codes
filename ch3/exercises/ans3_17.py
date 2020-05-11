# 鸡兔同笼问题，有35个头，94只脚，请问鸡兔各几只？
heads = 35
feet = 94

# 鸡兔同笼, for循环解答版
for chicken in range(0, heads):
    rabbits = heads - chicken
    if rabbits * 4 + chicken * 2 == feet:
        break

print(f"Chicken:{chicken}; Rabbits:{rabbits}")