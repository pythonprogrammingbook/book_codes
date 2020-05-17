# 在题目9.2的基础上，分别设置fill、expand、ipadx、ipady、padx和pady属性，体验其效果
from tkinter import *  #导入tkinter模块
window = Tk()  #创建主窗口对象
window.geometry('500x300')  #设置窗口大小与位置
window.title('pack')  #设置窗口标题
#fill: X，水平填充；Y，垂直填充；BOTH，水平填充+垂直填充
Label(window, text='TOP', bg='red').pack(side=TOP, fill=X)
#expand：指定控件是否扩展(不填充)父控件(Parent widget)提供的额外空间。默认值：False，不扩展；可选值：True，扩展
Label(window, text='BOTTOM', bg='red').pack(side=BOTTOM, expand=True)
#ipadx/ipady：在水平/垂直方向，控件内部填充ipdax个像素
Label(window, text="LEFT", bg='light blue').pack(side=LEFT, ipady = 30)
#padx/pady：在水平/垂直方向，控件边框与单元格边框之间填充pdax个像素
Label(window, text="RIGHT", bg='pink').pack(side=RIGHT, padx=30)
#进入Tk事件循环
window.mainloop()