# 先确认在VSCode的Settings中，勾选“Terminal：Excute In File Dir”
# 以只读模式打开文本文件hello_world.txt，读入所有行并输出
file_path = r'hello_world.txt'
with open(file_path, 'rt', encoding='utf-8') as f:
    for line in f.readlines():
        print(line, end='')