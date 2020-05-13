# 先确认在VSCode的Settings中，勾选“Terminal：Excute In File Dir”
# 请新建一个文本文件hello_world.txt，写入五行“hello,world!:i”，i从0到4

file_path = r'hello_world.txt'
with open(file_path, 'w') as f:
    for i in range(5):
        f.write('hello,world!:' + str(i) + '\n')
