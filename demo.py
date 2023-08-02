import tkinter as tk

import verify

root = tk.Tk()
root.geometry("300x300")
root.title("OTP验证器demo")


def make():
    # noinspection PyGlobalUndefined
    global img
    img = verify.init()
    c1.create_image(2, 2, anchor='nw', image=img)
    c1.grid(row=1, column=2)


def auth(event):
    user_input = e1.get()
    if verify.verify(user_input):
        var.set('验证成功！')
    else:
        var.set('验证失败！')


b1 = tk.Button(root, text='生成二维码', command=make)
b1.grid(row=1, padx=10, pady=10)

c1 = tk.Canvas(root, width=200, height=200, bg='lightgray')
c1.grid(row=1, column=2)

e1 = tk.Entry(root)
# noinspection PyTypeChecker
e1.bind('<Return>', auth)
e1.place(x=120, y=218)

b2 = tk.Button(root, text='验证', width=6, command=auth)
b2.grid(row=2, padx=10, pady=10)

var = tk.StringVar()
l2 = tk.Label(root, textvariable=var, bg='lightgray', width=10)
l2.place(x=148, y=250)

l3 = tk.Label(root, text='Power by：小牛仔')
l3.place(x=170, y=280)

root.mainloop()
