from tkinter import *
from tkinter import messagebox

def login():
    if user.get() == "admin" and pwd.get() == "1234":
        messagebox.showinfo("Success", "Login Successful")
    else:
        messagebox.showerror("Error", "Invalid Login")

root = Tk()
root.title("Login")

Label(root, text="Username").grid(row=0, column=0)
Label(root, text="Password").grid(row=1, column=0)

user = Entry(root)
pwd = Entry(root, show="*")
user.grid(row=0, column=1)
pwd.grid(row=1, column=1)

Button(root, text="Login", command=login).grid(row=2, column=1)

root.mainloop()
