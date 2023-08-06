import tkinter as tk
import pyotp
import qrcode
from tkinter import messagebox
from PIL import ImageTk


def verify(user):
    """读取秘钥文件"""
    try:
        with open('secdata.pass', 'r') as f:
            sec = f.read()
        totp = pyotp.TOTP(sec)
        result = totp.verify(user)
        return result
    except FileNotFoundError:
        return None


def init():
    """生成秘钥和对应二维码并返回Tk图像"""
    sec = pyotp.random_base32()
    with open('secdata.pass', 'w') as f:
        f.write(sec)
    totp = pyotp.TOTP(sec)
    uri = totp.provisioning_uri(name='admin', issuer_name='demo')
    img = qrcode.make(uri).resize((200, 200))
    print(totp.now())
    tk_img = ImageTk.PhotoImage(img)
    return tk_img


def gui_verify():
    """生成验证窗口"""
    root_verify = tk.Tk()
    root_verify.geometry("300x100")
    root_verify.protocol("WM_DELETE_WINDOW", exit)  # 监听窗口关闭事件，阻止运行下一步

    f1 = tk.Frame(root_verify, pady=25)
    f1.pack()

    l1 = tk.Label(f1, text="请输入验证码：")
    l1.pack(side="left")

    e1 = tk.Entry(f1)
    e1.pack()
    b1 = tk.Button(root_verify, text='验证', command=lambda: gui_exit(e1.get(), root_verify))  # 当按钮被按下时，使用匿名函数调用检测函数
    b1.pack()
    root_verify.mainloop()


def gui_exit(user, window):
    """检测验证是否成功"""
    if verify(user):
        window.destroy()
    else:
        messagebox.showerror("error", "验证码错误")

