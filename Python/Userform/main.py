from tkinter import *
root = Tk()

def getvalue():
    print(f"Username: {uservalue.get()}")
    print(f"Password: {passvalue.get()}")
    

# title
root.title("Userform")

# resizing
root.geometry("396x218")
root.minsize(396, 218)
root.maxsize(396, 218)

# Heading
Label(root, text="User Form", font="cascadia 25 bold").grid(row=0, column=3)


# User form layout
username = Label(root, text="Username", font="cascadia 15 bold")
password = Label(root, text="Password", font="cascadia 15 bold")

username.grid(row=1, column=2)
password.grid(row=2, column=2)

# User Entry
uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)

# packing user entry in grid
userentry.grid(row=1, column=3)
passentry.grid(row=2, column=3)

# button
Button(root, text="Submit", command=getvalue).grid(row=7, column=3)
root.mainloop()
