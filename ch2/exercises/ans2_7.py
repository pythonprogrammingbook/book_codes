s = "nice to meet you!"
nums_t = s.count('t')  # 计算't'的个数
start = 0              # 初始化查找't'的起点
positions = []         # 初始化保存't'的位置
found = 0
for i in range(nums_t):
    found = s.find('t', start)
    positions.append(found)  # 记录找到的't'的位置
    start = found + 1        # 从下一个位置开始查找't'
print(f'The number of t is {nums_t}, positions are {positions}')
