from PIL import ImageTk,Image
from Security import generate_qr
import tkinter as tk
import socket
import pyotp


##########################
# Establish Connection
########################## 
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


##########################
# Failed Message Return
##########################
def failed_return(root,frame1,client_socket,message):
    for widget in frame1.winfo_children():
        widget.destroy()
    message = message + "... \nTry again..."
    tk.Label(frame1, text=message, font=('Inter', 12, 'bold')).grid(row = 1, column = 1)
    client_socket.close()


##########################
# Server Communication
##########################
def log_server(root,frame1,client_socket,userID,password,otp,totp):
    message = userID + " " + password + " " + otp + " " + totp
    client_socket.send(message.encode())

    #Auth message
    message = client_socket.recv(1024) 
    message = message.decode()

    if(message=="Authenticate"):
        voting_page(root, frame1, client_socket)

    elif(message=="VoteCasted"):
        message = "Vote has Already been Cast"
        failed_return(root,frame1,client_socket,message)

    elif(message=="InvalidVoter"):
        message = "Invalid Voter"
        failed_return(root,frame1,client_socket,message)

    else:
        message = "Server Error"
        failed_return(root,frame1,client_socket,message)


##########################
# Cast/Record Vote
##########################
def cast_vote(root,frame1,vote,client_socket):

    for widget in frame1.winfo_children():
        widget.destroy()

    client_socket.send(vote.encode())

    message = client_socket.recv(1024).decode()
    print(message)

    if(message=="Successful"):
        tk.Label(frame1, text="Vote Casted Successfully", font=('Inter', 18, 'bold')).grid(row = 1, column = 1)
    else:
        tk.Label(frame1, text="Vote Cast Failed... \nTry again", font=('Inter', 18, 'bold')).grid(row = 1, column = 1)

    client_socket.close()

##########################
# Voter Login Screen
##########################
def voter_login(root,frame1):

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


    tk.Label(frame1, text="Voter Login", font=('Inter', 18, 'bold')).grid(row = 0, column = 2, rowspan=1)
    tk.Label(frame1, text="").grid(row = 1,column = 0)
    tk.Label(frame1, text="User ID:      ", anchor="e", justify=tk.LEFT).grid(row = 2,column = 0)
    tk.Entry(frame1, textvariable = userID).grid(row = 2,column = 2)

    tk.Label(frame1, text="Password:   ", anchor="e", justify=tk.LEFT).grid(row = 3,column = 0)
    tk.Entry(frame1, textvariable = password, show = '*').grid(row = 3,column = 2)

    tk.Label(frame1, text="OTP:   ", anchor="e", justify=tk.LEFT).grid(row = 4,column = 0)
    tk.Entry(frame1, textvariable = otp).grid(row = 4,column = 2)

    totp, save_path = generate_qr(pyotp.random_base32())

    tk.Label(frame1, text="\nPlease Scan With Google Authenticator", anchor="c", justify=tk.CENTER).grid(row = 5,column = 2)
    qr_code = ImageTk.PhotoImage((Image.open(save_path).resize((250,250),Image.ANTIALIAS)))
    tk.Label(frame1, image=qr_code).grid(row = 6,column = 2)

    tk.Button(frame1, text="Login", width=10, command = lambda: log_server(root, frame1, client_socket, userID.get(), password.get(), otp.get(), totp)).grid(row = 8, column = 2)
    tk.Label(frame1, text="").grid(row = 7,column = 0)

    frame1.pack()
    root.mainloop()

##########################
# Voting Page
##########################
def voting_page(root,frame1,client_socket):

    root.title("Cast Vote")
    for widget in frame1.winfo_children():
        widget.destroy()

    tk.Label(frame1, text="Cast Vote", font=('Inter', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
    tk.Label(frame1, text="").grid(row = 1,column = 0)

    vote = tk.StringVar(frame1,"-1")

    tk.Radiobutton(frame1, text = "Republican Party\n\nTommy Holland", variable = vote, value = "repub", indicator = 0, height = 4, width=15, command = lambda: cast_vote(root,frame1,"repub",client_socket)).grid(row = 2,column = 1)
    repubLogo = ImageTk.PhotoImage((Image.open("img/repub.png")).resize((45,45),Image.ANTIALIAS))
    tk.Label(frame1, image=repubLogo).grid(row = 2,column = 0)

    tk.Radiobutton(frame1, text = "Democratic Party\n\nBilly Cross", variable = vote, value = "demo", indicator = 0, height = 4, width=15, command = lambda: cast_vote(root,frame1,"demo",client_socket)).grid(row = 3,column = 1)
    demoLogo = ImageTk.PhotoImage((Image.open("img/demo.png")).resize((35,48),Image.ANTIALIAS))
    tk.Label(frame1, image=demoLogo).grid(row = 3,column = 0)

    tk.Radiobutton(frame1, text = "Green Party\n\nBailey Slater", variable = vote, value = "green", indicator = 0, height = 4, width=15, command = lambda: cast_vote(root,frame1,"green",client_socket) ).grid(row = 4,column = 1)
    greenLogo = ImageTk.PhotoImage((Image.open("img/green.png")).resize((55,40),Image.ANTIALIAS))
    tk.Label(frame1, image=greenLogo).grid(row = 4,column = 0)

    frame1.pack()
    root.mainloop()