import tkinter as tk
import dframe as df
from tkinter import *
from dframe import *
from PIL import ImageTk,Image

def resetAll(root,frame1):
    Label(frame1, text="").grid(row = 10,column = 0)
    msg = Message(frame1, text="Reset Complete", width=500)
    msg.grid(row = 11, column = 0, columnspan = 5)

def showVotes(root,frame1):

    result = df.show_result()
    root.title("Votes")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Vote Count", font=('Inter', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    repubLogo = ImageTk.PhotoImage((Image.open("img/repub.png")).resize((35,35),Image.ANTIALIAS))
    Label(frame1, image=repubLogo).grid(row = 2,column = 0)

    demoLogo = ImageTk.PhotoImage((Image.open("img/demo.png")).resize((25,38),Image.ANTIALIAS))
    Label(frame1, image=demoLogo).grid(row = 3,column = 0)

    greenLogo = ImageTk.PhotoImage((Image.open("img/green.png")).resize((45,30),Image.ANTIALIAS))
    Label(frame1, image=greenLogo).grid(row = 4,column = 0)


    Label(frame1, text="Republican Party:", font=('Inter', 12, 'bold')).grid(row = 2, column = 1)
    Label(frame1, text=result['repub'], font=('Inter', 12, 'bold')).grid(row = 2, column = 2)

    Label(frame1, text="Democratic Party:", font=('Inter', 12, 'bold')).grid(row = 3, column = 1)
    Label(frame1, text=result['demo'], font=('Inter', 12, 'bold')).grid(row = 3, column = 2)

    Label(frame1, text="Green Party:", font=('Inter', 12, 'bold')).grid(row = 4, column = 1)
    Label(frame1, text=result['green'], font=('Inter', 12, 'bold')).grid(row = 4, column = 2)

    frame1.pack()
    root.mainloop()

