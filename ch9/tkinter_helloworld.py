#第一步，导入tkinter模块
import tkinter as tk

#第四步，定义控件的功能代码
def say_hello():
    print("hello world!")

if __name__ == "__main__":
    #第二步，创建主窗口(Main Window)
    window = tk.Tk()
    window.title("hello world demo") #设置窗口标题
    window.geometry("280x80")  #设置窗口大小"宽度x高度"
    #第三步，创建控件，设置属性并关联功能代码
    button_hello = tk.Button(window,text="Hello World\n(click me)",
                             command=say_hello)
    button_quit = tk.Button(window,
                            text="QUIT",
                            fg="red",
                            command=window.destroy)
    #第五步，控件布局：指定控件的位置
    button_hello.pack(side='top')
    button_quit.pack(side='bottom')
    #第六步，调用主窗口对象的mainloop()方法，进入事件循环
    window.mainloop()
