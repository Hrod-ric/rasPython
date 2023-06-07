from tkinter import *
# from tkinter.ttk import *


root = Tk()
root_width, root_height = 200, 500
root.geometry("{}x{}".format(root_width, root_height))

b1 = Button(root, text="button", relief=FLAT)
b2 = Button(root, text="button", relief=RAISED)
b3 = Button(root, text="button", relief=SUNKEN)
b4 = Button(root, text="button", relief=GROOVE)
b5 = Button(root, text="button", relief=RIDGE)

b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()

root.mainloop()