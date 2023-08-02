import pyotp
import qrcode
import tkinter as tk
from PIL import ImageTk


def verify(user):
    try:
        with open('secdata.pass', 'r') as f:
            sec = f.read()
        totp = pyotp.TOTP(sec)
        result = totp.verify(user)
        return result
    except FileNotFoundError:
        return None


def init():
    sec = pyotp.random_base32()
    with open('secdata.pass', 'w') as f:
        f.write(sec)
    totp = pyotp.TOTP(sec)
    uri = totp.provisioning_uri(name='admin', issuer_name='demo')
    img = qrcode.make(uri).resize((200, 200))
    print(totp.now())
    tk_img = ImageTk.PhotoImage(img)
    return tk_img


def verify_gui():
    root = tk.Tk()
    root.geometry("300x100")
    root.protocol("WM_DELETE_WINDOW", exit)

    f1 = tk.Frame(root, pady=25)
    f1.pack()

    l1 = tk.Label(f1, text="请输入验证码：")
    l1.pack(side="left")

    e1 = tk.Entry(f1)
    e1.pack()
    b1 = tk.Button(root, text='验证', command=lambda: gui_exit(e1.get(), root))
    b1.pack()
    root.mainloop()


def gui_exit(user, window):
    if verify(user):
        window.destroy()
