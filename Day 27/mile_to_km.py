from tkinter import *
KM = 1.60934


def mile_to_km():
    mile = int(input_window.get())
    label.config(text=f"is equal to {mile*KM}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(200, 100)
padding_frame = Frame(window)
padding_frame.grid(padx=15, pady=20)

label = Label(text="is equal to")
label.grid(column=1, row=1)
label_m = Label(text="Miles")
label_km = Label(text="Km")
label_m.grid(column=2, row=0)
label_km.grid(column=2, row=1)


input_window = Entry()
input_window.get()
input_window.grid(column=1, row=0)

button = Button(text="Calculate", command=mile_to_km)
button.grid(column=1, row=2)






















window.mainloop()