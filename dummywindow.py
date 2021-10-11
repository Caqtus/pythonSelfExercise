import tkinter
from tkinter import ttk, Label, Tk
import time
import random

#makes new window with random size (in range)
#shows current time

root = Tk()
root.title("Hhuehuehue")
root.geometry("500x500")
root.resizable(1, 1)
frm = ttk.Frame(root, padding=10)
frm.grid(sticky = "n,e,s,w")
var1 = "test2"
label = Label(root, text=f"{var1}", font="Arial 50 bold", bg="#f2e750", fg="#363529")
label.grid(column=0, row=1)



def dummyWindow():

    randomNum = random.randint(10,100)
    var1 = time.strftime("%H:%M:%S")
    time_text = time.strftime("%H:%M:%S")
    width1 = root.winfo_width()
    height1 = root.winfo_height()
    label.config(text=var1, font="Arial 50 bold")


    winsize = f'{str(random.randint(200,500))}x{str(random.randint(200,500))}'
    root.geometry(winsize)
    print(width1, height1, winsize, var1)
    label.after(1000, dummyWindow)
    root.mainloop()


















