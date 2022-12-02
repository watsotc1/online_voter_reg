import tkinter as tk
import dframe as df
import Admin as adm
from tkinter import ttk
from Admin import *
from tkinter import *
from dframe import *

def reg_server(root,frame1,name,gender,county,state,userID,password):
    if(password=='' or password==' '):
        msg = Message(frame1, text="Error: Missing Fileds", width=500)
        msg.grid(row = 10, column = 0, columnspan = 5)
        return -1

    vid = df.taking_data_voter(name, gender, county, state, userID, password)
    for widget in frame1.winfo_children():
        widget.destroy()
    txt = "Registered Voter with\n\n VOTER I.D. = " + str(vid)
    Label(frame1, text=txt, font=('Inter', 18, 'bold')).grid(row = 2, column = 1, columnspan=2)


def Register(root,frame1):

    root.title("Register Voter")
    for widget in frame1.winfo_children():
        widget.destroy()

    name = tk.StringVar()
    gender = tk.StringVar()
    county = tk.StringVar()
    state = tk.StringVar()
    userID = tk.StringVar()
    password = tk.StringVar()

    Label(frame1, text="Voter Registration", font=('Inter', 18, 'bold')).grid(row = 0, column = 2, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)

    Label(frame1, text="Name:", anchor="e", justify=LEFT).grid(row = 3,column = 0)
    Entry(frame1, textvariable = name).grid(row = 3, column = 2)
    
    Label(frame1, text="Gender:", anchor="e", justify=LEFT).grid(row = 4,column = 0)
    gender_dd = ttk.Combobox(frame1, textvariable = gender, width=17)
    gender_dd['values'] = ("Male","Female", "Prefer Not To Say")
    gender_dd.grid(row = 4, column = 2)
    gender_dd.current()

    Label(frame1, text="County:", anchor="e", justify=LEFT).grid(row = 5,column = 0)
    Entry(frame1, textvariable = county).grid(row = 5, column = 2)
    
    Label(frame1, text="State:", anchor="e", justify=LEFT).grid(row = 6,column = 0)
    Entry(frame1, textvariable = state).grid(row = 6, column = 2)

    Label(frame1, text="UserID:", anchor="e", justify=LEFT).grid(row = 7,column = 0)
    Entry(frame1, textvariable = userID).grid(row = 7, column = 2)

    Label(frame1, text="Password:", anchor="e", justify=LEFT).grid(row = 8,column = 0)
    Entry(frame1, textvariable = password).grid(row = 8, column = 2)

    reg = Button(frame1, text="Register", command = lambda: reg_server(root, frame1, name.get(), gender.get(), county.get(), state.get(), userID.get(), password.get()), width=10)
    Label(frame1, text="").grid(row = 8,column = 0)
    reg.grid(row = 9, column = 3, columnspan = 2)

    frame1.pack()
    root.mainloop()

