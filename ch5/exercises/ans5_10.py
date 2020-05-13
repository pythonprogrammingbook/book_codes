# 先确认在VSCode的Settings中，勾选“Terminal：Excute In File Dir”

import os

cwd = os.getcwd()       # 获取当前目录
os.mkdir('hello')       # 在当前目录下创建hello文件夹
print(os.listdir(cwd))  # 输出当前目录中的所有文件和文件夹的名字

os.rmdir('hello')       # 在当前目录下删除hello文件夹
print(os.listdir(cwd))  # 输出当前目录中的所有文件和文件夹的名字
