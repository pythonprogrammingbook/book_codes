from tkinter import *
window = Tk()
colors = ['red', 'green', 'light blue', 'yellow']
#利用padx和pady可以把控件边框和单元格边框分开
cells = [Label(window, font="Arial 12", text='cell(%d,%d)' % (i, j), bg=colors[(i + j) % 4]).grid(row=i, column=j, padx=2, pady=2)
        for i in range(4) for j in range(4)]
window.mainloop()