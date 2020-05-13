# 先确认在VSCode的Settings中，勾选“Terminal：Excute In File Dir”
# 在当前文件夹下将hello_world.txt文件复制为hello_world_bak.txt
src = r'hello_world.txt'
dst = r'hello_world_bak.txt'

import shutil

shutil.copyfile(src, dst) 