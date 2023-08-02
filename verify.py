import pyotp
import qrcode
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
    img = qrcode.make(uri).resize((200,  200))
    print(img)
    tk_img = ImageTk.PhotoImage(img)
    return tk_img
