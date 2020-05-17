# 请用pack方式在TOP，BOTTOM，LEFT和RIGHT放置四个标签控件
from tkinter import *  #导入tkinter模块
window = Tk()  #创建主窗口对象
window.geometry('500x300')  #设置窗口大小与位置
window.title('pack')  #设置窗口标题
#放置4个Label控件在TOP，BOTTOM，LEFT和RIGHT位置
Label(window, text='TOP', bg='red').pack(side=TOP)

Label(window, text='BOTTOM', bg='red').pack(side=BOTTOM)

Label(window, text="LEFT", bg='light blue').pack(side=LEFT)

Label(window, text="RIGHT",bg='pink').pack(side=RIGHT)

#进入Tk事件循环
window.mainloop()
