from tkinter import *  #导入tkinter模块
window = Tk()  #创建主窗口对象
window.title('Grid Example')  #设置窗口标题

colors = ['red', 'green', 'light blue', 'yellow']

#展示padx, pady设置效果
labels0 = [
    Label(window, font="Arial 18", text=' grid(%d,%d) ' % (0, j),
          bg=colors[j]).grid(row=0, column=j, padx=j * 5, pady=j * 5)
    for j in range(4)
]
#保持默认设置
labels1 = [
    Label(window, font="Arial 12", text='grid(%d,%d)' % (1, j),
          bg=colors[j]).grid(row=1, column=j) for j in range(4)
]
#展示sticky设置效果
flags = [N, S, W, E]
labels2 = [
    Label(window, font="Arial 12", text='grid(%d,%d)' % (2, j),
          bg=colors[j]).grid(row=2, column=j, sticky=flags[j])
    for j in range(4)
]
#展示ipadx和ipady设置效果
labels3 = [
    Label(window, font="Arial 12", text='grid(%d,%d)' % (3, j),
          bg=colors[j]).grid(row=3, column=j, ipadx=j * 5, ipady=j * 5)
    for j in range(4)
]
#进入Tk事件循环
window.mainloop()