import pandas as pd
import win32com.client as win32

from tkinter import *
from tkinter.ttk import *
from time import strftime


root = Tk()
root.title("Clock")

def update_time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)

    # Chama essa função a cada 1000 milesegundos
    
    label.after(1000, update_time)

label = Label(root, font=("ds-digital", 80), background="#1C1C1C",
        foreground="#00FF00")
label.pack(anchor="center")
update_time()

mainloop()