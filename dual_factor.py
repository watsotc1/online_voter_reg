from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import pyotp
import pyqrcode
import png
from pyqrcode import QRCode

def generate_qr(keyword='base32secret3232'):
    s = pyotp.TOTP(keyword).provisioning_uri(name='alice@google.com', issuer_name='Secure Voting System')

    url = pyqrcode.create(s)

    url.png('img/otp.png', scale = 6)

def open_df_popup(root, frame):
    generate_qr('base32secret3232')    

    Label(frame, text="Please Scan With Google Authenticator", anchor="c", justify=CENTER).grid(row = 1,column = 0)
    qr_code = ImageTk.PhotoImage(Image.open("img/otp.png"))
    Label(frame, image=qr_code).grid(row = 2,column = 0)
