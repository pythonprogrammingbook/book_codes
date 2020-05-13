# 首先请在VSCode的Settings中，勾选“Terminal：Excute In File Dir”
# 打开并读取文件模板
file = r'lines.txt'
with open(file, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        print(line, end='')