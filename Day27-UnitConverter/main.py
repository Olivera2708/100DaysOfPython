from tkinter import *
from typing import ContextManager

def button_click():
    mile = float(input.get())
    kilo = mile * 1.609344
    res.config(text=f"{kilo}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(200, 100)
window.config(padx=10, pady=10)

res = Label(text = "0")
res.grid(column=2, row=2)

my_label1 = Label(text = "is equal to")
my_label1.grid(column=1, row=2)

my_label2 = Label(text = "Miles")
my_label2.grid(column=3, row=1)

my_label3 = Label(text = "Km")
my_label3.grid(column=3, row=2)

button = Button(text="Calculate", command=button_click)
button.grid(column=2, row=3)

input = Entry(width=10)
input.grid(column=2, row=1)

window.mainloop()