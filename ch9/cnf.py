import tkinter as tk
window = tk.Tk()
configs = {'font':('Arial','12','bold'),'fg': 'red', 'bg': 'white'}  #共同的属性配置
tk.Label(window, cnf=configs, text='abc').pack()  #cnf让代码更加简洁
tk.Label(window, cnf=configs, text='123').pack()
tk.Label(window, cnf=configs, text='xyz').pack()
tk.Label(window, cnf=configs, text='789').pack()
window.title('cnf')  #设置窗口标题
window.mainloop()  #进入Tk事件循环
