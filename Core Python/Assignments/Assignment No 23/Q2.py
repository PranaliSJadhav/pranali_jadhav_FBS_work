from tkinter import *

def calc(op):
    a = int(e1.get())
    b = int(e2.get())
    if op == '+':
        r.set(a+b)
    elif op == '-':
        r.set(a-b)
    elif op == '*':
        r.set(a*b)
    elif op == '/':
        r.set(a/b)

root = Tk()
root.title("Calculator")

e1 = Entry(root)
e2 = Entry(root)
r = StringVar()

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Label(root, text="Result").grid(row=2, column=0)
Entry(root, textvariable=r).grid(row=2, column=1)

Button(root, text="+", command=lambda: calc('+')).grid(row=3, column=0)
Button(root, text="-", command=lambda: calc('-')).grid(row=3, column=1)
Button(root, text="*", command=lambda: calc('*')).grid(row=4, column=0)
Button(root, text="/", command=lambda: calc('/')).grid(row=4, column=1)

root.mainloop()

