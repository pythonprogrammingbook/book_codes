import tkinter as tk
window = tk.Tk()
window.geometry('300x100+618+382')
window.title("GUI Example")
tk.Label(window, text='Label', fg='red').grid(row=0, column=0)
tk.Button(window, text='Button', fg='white', bg='blue').grid(row=1, column=0)
tk.Checkbutton(window, text="Checkbutton1").grid(row=2, column=0)
tk.Checkbutton(window, text="Checkbutton2").grid(row=3, column=0)
tk.Entry(window, text="Entry", show=None).grid(row=0, column=1)
t = tk.Text(window,height=1,width=20)
t.insert(tk.END, 'This is Text widget')
t.grid(row=1, column=1)
tk.Radiobutton(window, text="Radiobutton1").grid(row=2, column=1)
tk.Radiobutton(window, text="Radiobutton2").grid(row=3, column=1)

menu = tk.Menu(window)
window.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
helpmenu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
window.mainloop()
