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
tk.Label(window, text='账户', font=('微软雅黑', 12), anchor=tk.E).grid(row=0, column=1,sticky=tk.E)
tk.Label(window, text='密码', font=('微软雅黑', 12), anchor=tk.E).grid(row=1, column=1,sticky=tk.E)
#在标签的右侧放置输入控件
var_usr_name = tk.StringVar()
var_usr_pwd = tk.StringVar()
tk.Entry(window, width=15, textvariable=var_usr_name).grid(row=0, column=2)
tk.Entry(window, width=15, textvariable=var_usr_pwd,show='*').grid(row=1, column=2)
#创建放置按钮的框架控件
frame = tk.Frame(window,width=200,height=35,padx=2,pady=2)
frame.grid(row=3, column=1, columnspan=2, sticky=tk.W)
#定义"登录"按钮的回调函数
def login():
    user = var_usr_name.get()
    psw = var_usr_pwd.get()
    if user and psw :
        print("Username:%s\nPassword:%s" % (user, psw))
    else:
        print("Please Enter Username and Password!")
#放置两个按钮，一个“登录”，一个“取消”
tk.Button(frame,compound=tk.LEFT,image=icon_login,text='登录',font=('微软雅黑', 11),anchor=tk.E, padx=5,command=login).grid(row=2, column=1,padx=10)
tk.Button(frame,compound=tk.LEFT,image=icon_cancel,text='取消',font=('微软雅黑', 11),anchor=tk.E, padx=5,command=window.quit).grid(row=2, column=2, padx=6,sticky=tk.E)

#定义菜单回调函数
def callback_hello():
    print("hello from menu!")
#创建菜单栏
menubar = tk.Menu(window)
#创建File下拉菜单，并添加到菜单栏
filemenu = tk.Menu(menubar, tearoff=False)
filemenu.add(itemType='command', label="Open", command=callback_hello)
filemenu.add(itemType='command', label="Save", command=callback_hello)
filemenu.add(itemType='separator')
filemenu.add(itemType='command', label="Exit", command=window.quit)
menubar.add(itemType='cascade', label="File", menu=filemenu, underline=0)
#创建Edit下拉菜单，并添加到菜单栏
editmenu = tk.Menu(menubar, tearoff=False)
editmenu.add(itemType='command', label="Cut", command=callback_hello)
editmenu.add(itemType='command', label="Copy", command=callback_hello)
editmenu.add(itemType='command', label="Paste", command=callback_hello)
menubar.add(itemType='cascade', label="Edit", menu=editmenu, underline=0)
#创建Help下拉菜单，并添加到菜单栏
helpmenu = tk.Menu(menubar, tearoff=False)
helpmenu.add(itemType='command', label="About", command=callback_hello)
menubar.add(itemType='cascade', label="Help", menu=helpmenu)
#显示菜单
window.config(menu=menubar)
#启动Tk消息循环
window.mainloop()