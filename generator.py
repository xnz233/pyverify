import tkinter as tk
import verify
import pyotp
from PIL import ImageTk
root = tk.Tk()
root.geometry("300x300")
root.title("OTP秘钥生成器")


def make():
    global verifier,tk_qrcode
    sec = pyotp.random_base32()
    verifier = verify.Verifier(sec)
    print(verifier.uri)
    tk_qrcode = ImageTk.PhotoImage(verifier.qrcode)
    c1.create_image(2, 2, anchor='nw', image=tk_qrcode)
    c1.grid(row=1, column=2)

def auth(event):
    user_input = e1.get()
    if verifier.verify(user_input):
        var.set('验证成功！')
    else:
        var.set('验证失败！')


b1 = tk.Button(root, text='生成二维码', command=make)
b1.grid(row=1, padx=10, pady=10)

c1 = tk.Canvas(root, width=200, height=200, bg='lightgray')
c1.grid(row=1, column=2)

e1 = tk.Entry(root)
e1.bind('<Return>', auth)
e1.place(x=120, y=218)

b2 = tk.Button(root, text='验证', width=6, command=auth)
b2.grid(row=2, padx=10, pady=10)

var = tk.StringVar()
l2 = tk.Label(root, textvariable=var, bg='lightgray', width=10)
l2.place(x=148, y=250)

l3 = tk.Label(root, text='Power by: 小牛仔')
l3.place(x=170, y=280)

root.mainloop()
