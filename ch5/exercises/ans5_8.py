# 先确认在VSCode的Settings中，勾选“Terminal：Excute In File Dir”
# 将hello_world_copied.txt文件删除

file = r'hello_world_copied.txt'

import os

os.remove(file)