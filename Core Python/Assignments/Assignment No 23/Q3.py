from tkinter import *

def convert():
    amt = float(e.get())
    result.set(amt * 83)   

root = Tk()
root.title("Currency Converter")

Label(root, text="USD").grid(row=0, column=0)
e = Entry(root)
e.grid(row=0, column=1)

Button(root, text="Convert to INR", command=convert).grid(row=1, column=1)

result = StringVar()
Entry(root, textvariable=result).grid(row=2, column=1)

root.mainloop()
