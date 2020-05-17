# 请用grid方式放置4x4的按钮，分别命名0~9、=、+、-、x、÷、CE
from tkinter import *
window = Tk()
window.title('grid')  #设置窗口标题
names = ['0', '1', '2', '4', '5', '6', '7', '=', '7', '8', '9', 'CE', '+', '-', 'x', '÷']
#利用padx和pady可以把控件边框和单元格边框分开
cells = [
    Button(window,
          width = 5,
          font="Arial 12",
          text= names[i*4+j]).grid(row=i, column=j, padx=2, pady=2)
    for i in range(4) for j in range(4)
]
window.mainloop()