import tkinter
from tkinter import *
# We can stop using tkinter in every object creation by using from tkinter import *

window = tkinter.Tk()
window.title('My first GUI programme')
window.minsize(width=600, height=400)
window.config(padx=50, pady=50)


def display_email():
    print("I got clicked")
    text_entered = input.get()
    my_label.config(text=text_entered)
    print(text_entered)


# my_label["text"] = "New text"
# my_label.config(text="New text_1")
my_label = tkinter.Label(text="Enter your email", font=('Arial', 18, 'bold'))
my_label.grid(row=0, column=0)
my_label.config(padx=10, pady=10)

input = tkinter.Entry(width=50)
input.insert(END, string="Email")
input.grid(row=3, column=3)
# input.config(padx=10, pady=10)

button = tkinter.Button(text="Click me", command=display_email)
button.grid(row=1, column=1)
button.config(padx=10, pady=10)


def clear_label():
    my_label.config(text="Enter your mail")
    input.delete(0, END)
    input.insert(0, string="Email")


button_2 = Button(text="Clear", command=clear_label)
button_2.grid(row=0, column=2)
button_2.config(padx=10, pady=10)

window.mainloop()
