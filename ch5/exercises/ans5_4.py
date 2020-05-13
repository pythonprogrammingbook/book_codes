# 先确认在VSCode的Settings中，勾选“Terminal：Excute In File Dir”
# 删除hello_world.txt文件中i为奇数的行
file_path = r'hello_world.txt'
with open(file_path, 'rt', encoding='utf-8') as fr:
    lines = fr.readlines()
with open(file_path, 'w', encoding='utf-8') as fw:
    for line in lines:
        if int(line.strip()[-1]) % 2 == 0: #检查索引是否为奇数
            fw.write(line) 
