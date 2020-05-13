# 先确认在VSCode的Settings中，勾选“Terminal：Excute In File Dir”
# 输出当前操作系统的类型和路径分割符

import os

print(os.name)  # 输出当前操作系统的类型

print(os.sep)  # 输出路径分割符
