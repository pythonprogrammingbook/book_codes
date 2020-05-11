#《孙子算经》“今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二,问物几何？”
ans = 0

while not (ans % 3 == 2 and ans % 5 == 3 and ans % 7 == 2):
    ans += 1

print(f"Answer is {ans}")
    