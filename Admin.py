from Register import *
from PIL import ImageTk,Image
import subprocess as sb_p
import tkinter as tk


##########################
#  Reset Database
##########################
def resetAll(root,frame1):
    tk.Label(frame1, text="").grid(row = 10,column = 0)
    msg = tk.Message(frame1, text="Reset Complete", width=500)
    msg.grid(row = 11, column = 0, columnspan = 5)


##########################
# Admin Login
##########################
def admin_login(root,frame1,admin_ID,password):

    if(admin_ID=="Admin" and password=="admin"):
        frame3 = root.winfo_children()[1]
        admin_home(root, frame1, frame3)
    else:
        msg = tk.Message(frame1, text="Either ID or Password is Incorrect", width=500)
        msg.grid(row = 6, column = 0, columnspan = 5)


##########################
# Admin Home Page
##########################
def admin_home(root,frame1,frame3):
    root.title("Admin")
    for widget in frame1.winfo_children():
        widget.destroy()

    tk.Button(frame3, text="Admin", command = lambda: admin_home(root, frame1, frame3)).grid(row = 1, column = 0)
    frame3.pack(side=tk.TOP)

    tk.Label(frame1, text="Admin", font=('Inter', 25, 'bold')).grid(row = 0, column = 1)
    tk.Label(frame1, text="").grid(row = 1,column = 0)

    #Admin Login
    run_server_btn = tk.Button(frame1, text="Run Server", width=15, command = lambda:sb_p.call('start python Server.py', shell=True))

    #Voter Login
    register_page_btn = tk.Button(frame1, text="Register Voter", width=15, command = lambda:register_page(root, frame1))

    #Show Votes
    show_current_votes_btn = tk.Button(frame1, text="Show Votes", width=15, command = lambda:show_current_votes(root, frame1))

    #Reset Data
    reset_btn = tk.Button(frame1, text="Reset All", width=15, command = lambda: resetAll(root, frame1))

    tk.Label(frame1, text="").grid(row = 2,column = 0)
    tk.Label(frame1, text="").grid(row = 4,column = 0)
    tk.Label(frame1, text="").grid(row = 6,column = 0)
    tk.Label(frame1, text="").grid(row = 8,column = 0)
    run_server_btn.grid(row = 3, column = 1, columnspan = 2)
    register_page_btn.grid(row = 5, column = 1, columnspan = 2)
    show_current_votes_btn.grid(row = 7, column = 1, columnspan = 2)
    reset_btn.grid(row = 9, column = 1, columnspan = 2)

    frame1.pack()
    root.mainloop()


##########################
# Admin Login Screen
##########################
def admin_login_page(root,frame1):

    root.title("Admin Login")
    for widget in frame1.winfo_children():
        widget.destroy()

    tk.Label(frame1, text="Admin Login", font=('Inter', 18, 'bold')).grid(row = 0, column = 2, rowspan=1)
    tk.Label(frame1, text="").grid(row = 1,column = 0)
    tk.Label(frame1, text="Admin ID:      ", anchor="e", justify=tk.LEFT).grid(row = 2,column = 0)
    tk.Label(frame1, text="Password:       ", anchor="e", justify=tk.LEFT).grid(row = 3,column = 0)

    admin_ID = tk.StringVar()
    password = tk.StringVar()

    tk.Entry(frame1, textvariable = admin_ID).grid(row = 2,column = 2)
    tk.Entry(frame1, textvariable = password, show = '*').grid(row = 3,column = 2)

    sub = tk.Button(frame1, text="Login", width=10, command = lambda: admin_login(root, frame1, admin_ID.get(), password.get()))
    tk.Label(frame1, text="").grid(row = 4,column = 0)
    sub.grid(row = 5, column = 3, columnspan = 2)

    frame1.pack()
    root.mainloop()


##########################
#Show Current Votes
##########################
def show_current_votes(root,frame1):

    result = show_result()
    root.title("Votes")
    for widget in frame1.winfo_children():
        widget.destroy()

    tk.Label(frame1, text="Vote Count", font=('Inter', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
    tk.Label(frame1, text="").grid(row = 1,column = 0)

    vote = tk.StringVar(frame1,"-1")

    repubLogo = ImageTk.PhotoImage((Image.open("img/repub.png")).resize((35,35),Image.ANTIALIAS))
    tk.Label(frame1, image=repubLogo).grid(row = 2,column = 0)

    demoLogo = ImageTk.PhotoImage((Image.open("img/demo.png")).resize((25,38),Image.ANTIALIAS))
    tk.Label(frame1, image=demoLogo).grid(row = 3,column = 0)

    greenLogo = ImageTk.PhotoImage((Image.open("img/green.png")).resize((45,30),Image.ANTIALIAS))
    tk.Label(frame1, image=greenLogo).grid(row = 4,column = 0)


    tk.Label(frame1, text="Republican Party:", font=('Inter', 12, 'bold')).grid(row = 2, column = 1)
    tk.Label(frame1, text=result['repub'], font=('Inter', 12, 'bold')).grid(row = 2, column = 2)

    tk.Label(frame1, text="Democratic Party:", font=('Inter', 12, 'bold')).grid(row = 3, column = 1)
    tk.Label(frame1, text=result['demo'], font=('Inter', 12, 'bold')).grid(row = 3, column = 2)

    tk.Label(frame1, text="Green Party:", font=('Inter', 12, 'bold')).grid(row = 4, column = 1)
    tk.Label(frame1, text=result['green'], font=('Inter', 12, 'bold')).grid(row = 4, column = 2)

    frame1.pack()
    root.mainloop()