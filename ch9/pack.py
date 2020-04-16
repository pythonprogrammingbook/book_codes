from tkinter import * #导入tkinter模块
window = Tk()     #创建主窗口对象
window.geometry('500x300')  #设置窗口大小与位置
window.title('pack')  #设置窗口标题
#放置10个Label控件，展示Pack放置方式和配置
Label(window, text='TOP1, fill=NONE', bg='red').pack(side=TOP, fill=NONE)
Label(window, text='TOP2, fill=X', bg='yellow').pack(side=TOP, fill=X)
Label(window, text='BOTTOM1, ipadx=0',bg='red').pack(side=BOTTOM, ipadx=0)
Label(window, text='BOTTOM2, ipadx=40,ipady=10',bg='yellow').pack(side=BOTTOM, ipadx=40, ipady=10)
Label(window, text="LEFT1\nexpand=False", bg='light blue').pack(side=LEFT, expand=False)
Label(window, text="LEFT2\nexpand=False", bg='yellow2').pack(side=LEFT, expand=False)
Label(window, text="LEFT3\nexpand=True",bg='light green').pack(side=LEFT, expand=True)
Label(window, text="RIGHT1\npadx=10\npady=0\nfill=NONE", bg='pink').pack(side=RIGHT, padx=10)
Label(window, text="RIGHT2\npadx=0\npady=10\nfill=tk.Y", bg='skyblue1').pack(side=RIGHT, padx=0, pady=10, fill=Y)
Label(window, text="RIGHT2\npadx=0\npady=0\nfill=tk.Y", bg='coral1').pack(side=RIGHT, padx=0, fill=Y)
#进入Tk事件循环
window.mainloop()
