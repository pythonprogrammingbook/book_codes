fruits = ('apple', 'pear', 'grapefruit', 'pineapple', 'avocado')

for i, fruit in enumerate(fruits):
    if fruit[0] == 'a':  #检查是否以'a'开头
        print(f"{fruit} is at Position:{i}.")
    