import tkinter as tk
import socket
from tkinter import *
from VotingPage import votingPg
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


def establish_connection():
    host = socket.gethostname()
    port = 4001
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(client_socket)

    #Connection establishment message
    message = client_socket.recv(1024)      
    if(message.decode()=="Connection Established"):
        return client_socket
    else:
        return 'Failed'


def failed_return(root,frame1,client_socket,message):
    for widget in frame1.winfo_children():
        widget.destroy()
    message = message + "... \nTry again..."
    Label(frame1, text=message, font=('Inter', 12, 'bold')).grid(row = 1, column = 1)
    client_socket.close()

def log_server(root,frame1,client_socket,userID,password):
    message = userID + " " + password
    client_socket.send(message.encode())

    #Authenticatication message
    message = client_socket.recv(1024) 
    message = message.decode()

    if(message=="Authenticate"):
        votingPg(root, frame1, client_socket)

    elif(message=="VoteCasted"):
        message = "Vote has Already been Cast"
        failed_return(root,frame1,client_socket,message)

    elif(message=="InvalidVoter"):
        message = "Invalid Voter"
        failed_return(root,frame1,client_socket,message)

    else:
        message = "Server Error"
        failed_return(root,frame1,client_socket,message)



def voterLogin(root,frame1):

    client_socket = establish_connection()
    if(client_socket == 'Failed'):
        message = "Connection failed"
        failed_return(root,frame1,client_socket,message)

    root.title("Voter Login")
    for widget in frame1.winfo_children():
        widget.destroy()
    
    userID = tk.StringVar()
    password = tk.StringVar()
    otp = tk.StringVar()


    Label(frame1, text="Voter Login", font=('Inter', 18, 'bold')).grid(row = 0, column = 2, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)
    Label(frame1, text="User ID:      ", anchor="e", justify=LEFT).grid(row = 2,column = 0)
    Entry(frame1, textvariable = userID).grid(row = 2,column = 2)

    Label(frame1, text="Password:   ", anchor="e", justify=LEFT).grid(row = 3,column = 0)
    Entry(frame1, textvariable = password, show = '*').grid(row = 3,column = 2)

    Label(frame1, text="OTP:   ", anchor="e", justify=LEFT).grid(row = 4,column = 0)
    Entry(frame1, textvariable = otp, show = '*').grid(row = 4,column = 2)

    generate_qr('base32secret3232')    

    Label(frame1, text="\nPlease Scan With Google Authenticator", anchor="c", justify=CENTER).grid(row = 5,column = 2)
    qr_code = ImageTk.PhotoImage((Image.open("img/otp.png").resize((250,250),Image.ANTIALIAS)))
    Label(frame1, image=qr_code).grid(row = 6,column = 2)

    Button(frame1, text="Login", width=10, command = lambda: log_server(root, frame1, client_socket, userID.get(), password.get(), otp.get())).grid(row = 8, column = 2)
    Label(frame1, text="").grid(row = 7,column = 0)

    frame1.pack()
    root.mainloop()
