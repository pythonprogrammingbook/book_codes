import tkinter as tk #导入tkinter模块
window = tk.Tk()     #创建主窗口对象
screen_width = window.winfo_screenwidth()   #获取屏幕宽度
screen_height = window.winfo_screenheight()  #获取屏幕高度
x = (screen_width - 200) / 2  #计算窗口坐标x
y = (screen_height - 100) / 2  #计算窗口坐标y
window.geometry('200x100+%d+%d'%(x,y))  #设置窗口大小与位置
window.title('login')  #设置窗口标题
window.mainloop()  #进入Tk事件循环
