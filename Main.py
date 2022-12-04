from Admin import admin_login_page
from Voter import voter_login
import subprocess as sb_p
import tkinter as tk


def Home(root, frame1, frame2):

    for frame in root.winfo_children():
        for widget in frame.winfo_children():
            widget.destroy()

    tk.Button(frame2, text="Home", command = lambda: Home(root, frame1, frame2)).grid(row=0,column=0)
    tk.Label(frame2, text="                                                                         ").grid(row = 0,column = 1)
    tk.Label(frame2, text="                                                                         ").grid(row = 0,column = 2)
    tk.Label(frame2, text="         ").grid(row = 1,column = 1)
    frame2.pack(side=tk.TOP)

    root.title("Voter System Home")

    tk.Label(frame1, text="Home", font=('Inter', 25, 'bold')).grid(row = 0, column = 1, rowspan=1)
    tk.Label(frame1, text="").grid(row = 1,column = 0)
    #Admin Login
    admin = tk.Button(frame1, text="Admin Login", width=15, command = lambda: admin_login_page(root, frame1))

    #Voter Login
    voter = tk.Button(frame1, text="Voter Login", width=15, command = lambda: voter_login(root, frame1))

    #New Tab
    newTab = tk.Button(frame1, text="New Window", width=15, command = lambda: sb_p.call('start python main.py', shell=True))

    tk.Label(frame1, text="").grid(row = 2,column = 0)
    tk.Label(frame1, text="").grid(row = 4,column = 0)
    tk.Label(frame1, text="").grid(row = 6,column = 0)
    admin.grid(row = 3, column = 1, columnspan = 2)
    voter.grid(row = 5, column = 1, columnspan = 2)
    newTab.grid(row = 7, column = 1, columnspan = 2)

    frame1.pack()
    root.mainloop()


def new_home():
    root = tk.Tk()
    root.geometry('600x600')
    frame1 = tk.Frame(root)
    frame2 = tk.Frame(root)
    Home(root, frame1, frame2)


if __name__ == "__main__":
    new_home()
