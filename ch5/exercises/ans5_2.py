# 先确认在VSCode的Settings中，勾选“Terminal：Excute In File Dir”
# 请打开文本文件hello_world.txt，追加五行“hello,world!:i”，i从5到9
file_path = r'hello_world.txt'
with open(file_path, 'a') as f:
    for i in range(5, 10):
        f.write('hello,world!:' + str(i) + '\n')