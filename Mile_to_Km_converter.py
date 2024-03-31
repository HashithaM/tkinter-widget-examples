from tkinter import *

window = Tk()
window.title('Mile to Kilometer Converter')
window.minsize(width=600, height=400)
window.config(padx=50, pady=50)

input = Entry(width=10)
input.insert(END, string="Miles")
input.grid(row=0, column=1)

label_1 = Label(text="Miles", font=('Arial', 18, 'bold'))
label_1.grid(row=0, column=2)
label_1.config(padx=20, pady=20)

label_2 = Label(text="is equal to", font=('Arial', 18, 'bold'))
label_2.grid(row=1, column=0)
label_2.config(padx=20, pady=20)

label_3 = Label(text="kms", font=('Arial', 18, 'bold'))
label_3.grid(row=1, column=1)
label_3.config(padx=20, pady=20)

label_4 = Label(text="Km", font=('Arial', 18, 'bold'))
label_4.grid(row=1, column=2)
label_4.config(padx=20, pady=20)


def calculate():
    num_miles = float(input.get())
    kms = num_miles * 1.609
    label_3.config(text=f"{kms}")
    return kms


button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)
button.config(padx=20, pady=20)

window.mainloop()
