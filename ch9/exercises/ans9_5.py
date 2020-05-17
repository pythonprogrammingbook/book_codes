# 请用place方式放置4x4的按钮，分别命名0~9、=、+、-、x、÷、CE
from tkinter import *
window = Tk()
window.title('place')  #设置窗口标题
window.geometry('240x160')  #设置窗口大小与位置
names = [
    '0', '1', '2', '4', '5', '6', '7', '=', '7', '8', '9', 'CE', '+', '-', 'x',
    '÷'
]
#利用padx和pady可以把控件边框和单元格边框分开
cells = [
    Button(window, width=5, font="Arial 12",
           text=names[i * 4 + j]).place(x=j*60+5, y=i*40+5, width=50, height=30) for i in range(4)for j in range(4)]
window.mainloop()