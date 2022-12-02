import tkinter as tk
import socket
from tkinter import *
from PIL import ImageTk,Image

def voteCast(root,frame1,vote,client_socket):

    for widget in frame1.winfo_children():
        widget.destroy()

    client_socket.send(vote.encode())

    message = client_socket.recv(1024)
    print(message.decode())
    message = message.decode()
    if(message=="Successful"):
        Label(frame1, text="Vote Casted Successfully", font=('Inter', 18, 'bold')).grid(row = 1, column = 1)
    else:
        Label(frame1, text="Vote Cast Failed... \nTry again", font=('Inter', 18, 'bold')).grid(row = 1, column = 1)

    client_socket.close()



def votingPg(root,frame1,client_socket):

    root.title("Cast Vote")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Cast Vote", font=('Inter', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    Radiobutton(frame1, text = "Republican Party\n\nTommy Holland", variable = vote, value = "repub", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"repub",client_socket)).grid(row = 2,column = 1)
    repubLogo = ImageTk.PhotoImage((Image.open("img/repub.png")).resize((45,45),Image.ANTIALIAS))
    repubImg = Label(frame1, image=repubLogo).grid(row = 2,column = 0)

    Radiobutton(frame1, text = "Democratic Party\n\nBilly Cross", variable = vote, value = "demo", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"demo",client_socket)).grid(row = 3,column = 1)
    demoLogo = ImageTk.PhotoImage((Image.open("img/demo.png")).resize((35,48),Image.ANTIALIAS))
    demoImg = Label(frame1, image=demoLogo).grid(row = 3,column = 0)

    Radiobutton(frame1, text = "Green Party\n\nBailey Slater", variable = vote, value = "green", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"green",client_socket) ).grid(row = 4,column = 1)
    greenLogo = ImageTk.PhotoImage((Image.open("img/green.png")).resize((55,40),Image.ANTIALIAS))
    greenImg = Label(frame1, image=greenLogo).grid(row = 4,column = 0)

    frame1.pack()
    root.mainloop()
