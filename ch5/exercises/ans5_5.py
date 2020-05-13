# 先确认在VSCode的Settings中，勾选“Terminal：Excute In File Dir”
file_path = r'hello_world.txt'
import os
print(os.getcwd())  # 获取当前的工作路径

import sys
print(sys.path)  # Python模块的搜索路径

abs_path = os.path.abspath(file_path)
print(abs_path)  # hello_world.txt文件的绝对路径

print(os.path.basename(abs_path))  # 从绝对路径中拆分出最后一级文件名

print(os.path.dirname(abs_path))  # 从绝对路径中提取出目录名

dir, file = os.path.split(abs_path)  # 从绝对路径中拆分出目录和文件名
print(dir, file)

print(os.path.join(dir, file)) # 将目录和文件名合成路径