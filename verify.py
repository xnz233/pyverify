import pyotp
import os
import qrcode
import tkinter as tk

class Verifier:
    def __init__(self, sec):
        self.totp = pyotp.TOTP(sec)
        self.uri = self.totp.provisioning_uri(name='admin', issuer_name='demo')
        self.qrcode = qrcode.make(self.uri).resize((200, 200))

    def verify(self, user):
        result = self.totp.verify(user)
        return result

    def verify_gui(self):
        self.root = tk.Tk()
        self.root.geometry("300x100")
        self.root.protocol("WM_DELETE_WINDOW", exit)

        f1 = tk.Frame(self.root, pady=25)
        f1.pack()

        l1 = tk.Label(f1, text="请输入验证码：")
        l1.pack(side="left")

        e1 = tk.Entry(f1)
        e1.pack()
        b1 = tk.Button(self.root, text='验证',
                       command=lambda: self.gui_exit(e1.get(), self.root))
        b1.pack()
        self.root.mainloop()

    def gui_exit(self, user, window):
        if self.verify(user):
            window.destroy()


if __name__ == '__main__':
    verifier = Verifier(pyotp.random_base32())
    print(verifier.totp.now())
    verifier.verify_gui()
    print('ok')
