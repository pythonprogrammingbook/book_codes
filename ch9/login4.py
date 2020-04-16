import tkinter as tk  #导入tkinter模块
window = tk.Tk()  #创建主窗口对象
screen_width = window.winfo_screenwidth()  #获取屏幕宽度
screen_height = window.winfo_screenheight()  #获取屏幕高度
x = (screen_width - 200) / 2  #计算窗口坐标x
y = (screen_height - 100) / 2  #计算窗口坐标y
window.geometry('260x100+%d+%d' % (x, y))  #设置窗口大小与位置
window.title('login')  #设置窗口标题
#读取图片文件
logo = tk.PhotoImage(file="python_logo.png")
icon_login = tk.PhotoImage(file="login.png")
icon_cancel = tk.PhotoImage(file="cancel.png")
#在左侧放置一个标签，显示logo图片
tk.Label(window, justify=tk.LEFT, image=logo).grid(row=0, column=0, rowspan=2)
#放置两个标签，一个为“账户”，一个为“密码”，字体：微软雅黑，12号
tk.Label(window, text='账户', font=('微软雅黑', 12)).grid(row=0, column=1)
tk.Label(window, text='密码', font=('微软雅黑', 12)).grid(row=1, column=1)
#在标签的右侧放置输入控件
var_usr_name = tk.StringVar()
var_usr_pwd = tk.StringVar()
tk.Entry(window, width=15, textvariable=var_usr_name).grid(row=0, column=2)
tk.Entry(window, width=15, textvariable=var_usr_pwd,show='*').grid(row=1, column=2)

#定义"登录"按钮的回调函数
def login():
    user = var_usr_name.get()
    psw = var_usr_pwd.get()
    if user and psw :
        print("Username:%s\nPassword:%s" % (user, psw))
    else:
        print("Please Enter Username and Password!")
#放置两个按钮，一个“登录”，一个“取消”

tk.Button(window,compound=tk.LEFT,image=icon_login,text='登录',font=('Microsoft YaHei', 11),anchor=tk.E,padx=10, width=60, command=login).grid(row=2, column=1)
tk.Button(window,compound=tk.LEFT,image=icon_cancel,text='取消',font=('Microsoft YaHei', 11),anchor=tk.E,padx = 10,width=60,command=window.quit).grid(row=2, column=2)
window.mainloop()  #进入Tk事件循环
