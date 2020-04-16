from tkinter import *  #导入tkinter模块
window = Tk()  #创建主窗口对象
window.title('Place Example')  #设置窗口标题
window.geometry('300x200')  #设置窗口大小与位置

colors = ['red', 'green', 'light blue', 'yellow']
#Place放置效果
[Label(window, font="Arial 12",text='place(80,%d),anchor=NW' % (20 + i * 40),
          bg=colors[i]).place(x=40, y=20 + i * 40, width=200, height=30)
    for i in range(4)
]
#进入Tk事件循环
window.mainloop()