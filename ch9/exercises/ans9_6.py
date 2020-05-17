# 请设计并实现一个能输入用户名和密码的登录窗口
import tkinter as tk  #导入tkinter模块
window = tk.Tk()  #创建主窗口对象
screen_width = window.winfo_screenwidth()  #获取屏幕宽度
screen_height = window.winfo_screenheight()  #获取屏幕高度
x = (screen_width - 200) / 2  #计算窗口坐标x
y = (screen_height - 100) / 2  #计算窗口坐标y
window.geometry('250x100+%d+%d' % (x, y))  #设置窗口大小与位置
window.title('login')  #设置窗口标题

#放置两个标签，一个为“账户”，一个为“密码”，字体：微软雅黑，12号
tk.Label(window, text='账户', font=('微软雅黑', 12)).grid(row=0, column=0)
tk.Label(window, text='密码', font=('微软雅黑', 12)).grid(row=1, column=0)
#在标签的右侧放置输入控件
var_usr_name = tk.StringVar()
var_usr_pwd = tk.StringVar()
tk.Entry(window, width=15, textvariable=var_usr_name).grid(row=0, column=1)
tk.Entry(window, width=15, textvariable=var_usr_pwd, show='*').grid(row=1,column=1)


#定义"登录"按钮的回调函数
def login():
    user = var_usr_name.get()
    psw = var_usr_pwd.get()
    if user and psw:
        print("Username:%s\nPassword:%s" % (user, psw))
    else:
        print("Please Enter Username and Password!")


#放置两个按钮，一个“登录”，一个“取消”

tk.Button(window,
          text='登录',
          font=('Microsoft YaHei', 11),
          anchor=tk.CENTER,
          padx=3,
          width=12,
          command=login).grid(row=2, column=0)
tk.Button(window,
          text='取消',
          font=('Microsoft YaHei', 11),
          anchor=tk.CENTER,
          padx=3,
          width=12,
          command=window.quit).grid(row=2, column=1)
window.mainloop()  #进入Tk事件循环