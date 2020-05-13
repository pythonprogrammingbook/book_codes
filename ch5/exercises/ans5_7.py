# 先确认在VSCode的Settings中，勾选“Terminal：Excute In File Dir”
# 将hello_world_bak.txt文件重命名为hello_world_copied.txt
src = r'hello_world_bak.txt'
dst = r'hello_world_copied.txt'

import os

os.rename(src, dst)
