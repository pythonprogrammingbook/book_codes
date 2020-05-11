# 给定一个正整数 rows，生成rows行杨辉三角
# C(rows,cols) = C(rows-1,cols-1) + C(rows-1,cols)
rows = 8
triangle = []

for i in range(rows):
    tmp = [1] * (i + 1)
    triangle.append(tmp)
    for j in range(1, i):
        triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

for row in triangle:
    print(row)