fruits = ['apple', 'pear', 'grapefruit', 'pineapple', 'avocado']
fruits.append('blueberry')  #'blueberry'添加到列表中
fruits.remove('apple')      #将'apple'从列表中删除
position = fruits.index('pineapple')  #判断'pineapple'是在什么位置
fruits.insert(position, 'lemon')  #在'pineapple'前插入'lemon'
is_mango_in = 'mango' in fruits   #判断'mango'是否在列表中
types_fruits = len(set(fruits))   #计算fruits中一共有几种水果
print(fruits)
print(f"There are {types_fruits} fruits")
