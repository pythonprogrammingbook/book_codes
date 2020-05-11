ans = []
i = 1

while i < 100:
    if (i % 3 == 0 or i % 7 == 0) and not (i % 3 == 0 and i % 7 == 0):
        ans.append(i)
    i += 1
    
print(f"Answer:{ans}")