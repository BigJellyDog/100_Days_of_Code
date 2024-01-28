from tkinter import *


def button_clicked():
    my_label.config(text=input.get())


window = Tk()
window.title("My First GUI Program")
window.minsize(500, 300)
window.config(padx=100, pady=200)

my_label = Label(text="Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(text="New Text")
# my_label.config(padx=50, pady=50)


button = Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=2)
button2 = Button(text="Second button")
button2.grid(column=3, row=0)

input = Entry(width=10)
print(input.get())
input.grid(column=4, row=4)














window.mainloop()
