from tkinter import *
from tkinter.ttk import *

from time import  strftime

root = Tk()
root.title("clock")

def time():
    string = strftime('%l:%M:%S %p ')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("Digital-7", 200), background = "black", foreground = "cyan")
label.pack(anchor='center')

time()

mainloop()

# photo = PhotoImage(file = "path to file")
# root.iconphoto(False, photo)
