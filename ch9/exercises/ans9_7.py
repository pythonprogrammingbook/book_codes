# 请用用面向对象(OOP)的方式实现一个能输入用户名和密码的登录窗口
from tkinter import *  #导入tkinter模块
FONT = ('微软雅黑', 12)
# 定义GUI页面类
class LoginPage():
    def __init__(self, master):
        self.master = master
        self.initUI()

    def initUI(self):
        '''初始化UI'''
        self.center_window()  #让窗口在屏幕居中

        #放置两个标签，一个为“账户”，一个为“密码”，字体：微软雅黑，12号
        Label(self.master, text='账户', font=FONT).grid(row=0, column=0)
        Label(self.master, text='密码', font=FONT).grid(row=1, column=0)
        #放置两个输入控件
        self.entry_user = Entry(self.master, width=15)
        self.entry_user.grid(row=0, column=1)
        self.entry_psw = Entry(self.master, width=15, show='*')
        self.entry_psw.grid(row=1, column=1)
        #放置两个按钮
        Button(self.master,
               anchor=CENTER,
               text='登录',
               font=FONT,
               width=10,
               command=self.__button_login).grid(row=2, column=0)
        Button(self.master,
               anchor=CENTER,
               text='取消',
               font=FONT,
               width=10,
               command=self.master.quit).grid(row=2, column=1)

    def __button_login(self):
        '''登录按钮的回调函数'''
        user = self.entry_user.get()
        psw = self.entry_psw.get()
        if user and psw:
            print("Username:%s\nPassword:%s" % (user, psw))
        else:
            print("Please Enter Username and Password!")

    def center_window(self):
        '''让窗口在屏幕上居中'''
        screen_width = self.master.winfo_screenwidth()  #获取屏幕宽度
        screen_height = self.master.winfo_screenheight()  #获取屏幕高度
        x = (screen_width - 200) / 2  #计算窗口坐标x
        y = (screen_height - 100) / 2  #计算窗口坐标y
        self.master.geometry('225x100+%d+%d' % (x, y))  #设置窗口大小与位置
        self.master.title('login')  #设置窗口标题

def main():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    main()
