import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import pandas as pd

PINK = "#e2979c"
RED = "#E21818"
GREEN = "#65B741"
YELLOW = "#E8C872"
GREY = "#2d2f3c"
ORANGE = "#FC6736"
BLACK = "#000000"
BLUE = "#287fbd"
BGCOLOR = "#dde9f1"
BOXCOLOR = "#afd6ef"
EEEECOLOR = "#d3e2ec"
FONT_NAME = "Courgette"


pass_screen = Tk()
pass_screen.config(bg=BGCOLOR)
pass_screen.title("Passwords")

pass_screen.grid_columnconfigure(0, weight=1)
pass_screen.grid_rowconfigure(0, weight=1)

tree = ttk.Treeview(pass_screen, columns=("Website", "Username"), show="headings")
tree.grid(row=0, column=0, sticky=NS)
tree.heading('Website', text="Website")
tree.heading('Username', text="Username")
tree.column('Website', anchor='w', width=100)
tree.column('Username', anchor='w', width=100)

style = ttk.Style()
style.configure("Treeview", rowheight=30, backgorund=BGCOLOR, fieldbackground=BGCOLOR)


reader = pd.read_csv("data.csv")

for i, row in reader.iterrows():
    # Inserting both website and username in the same row under their respective columns
    tree.insert('', tkinter.END, text=str(i), values=(row["Website"], row["Username"]))

scrollbar = Scrollbar(pass_screen, orient="vertical", command=tree.yview)
scrollbar.grid(row=0, column=1, sticky=NS)
tree['yscrollcommand'] = scrollbar.set


def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        small_window = Tk()
        small_window.title(f"{item["values"][0]}")
        small_window.configure(bg=BGCOLOR)
        Label(small_window, text="Website:", font=(FONT_NAME, 10), justify="left", bg=BGCOLOR).grid(row=0, column=0, padx=10, pady=5)
        website = Entry(small_window, justify="center", font=(FONT_NAME, 10), bd=0, highlightthickness=0, bg=BGCOLOR)
        website.grid(row=0, column=1, padx=5, pady=5)
        Label(small_window, text="Username:", font=(FONT_NAME, 10), justify="left", bg=BGCOLOR).grid(row=1, column=0, padx=10, pady=5)
        username = Entry(small_window, justify="center", font=(FONT_NAME, 10), bd=0, highlightthickness=0, bg=BGCOLOR)
        username.grid(row=1, column=1, padx=5, pady=5)
        Label(small_window, text="Password:", font=(FONT_NAME, 10), justify="left", bg=BGCOLOR).grid(row=2, column=0, padx=10, pady=5)
        password = Entry(small_window, justify="center", font=(FONT_NAME, 10), bd=0, highlightthickness=0, bg=BGCOLOR)
        password.grid(row=2, column=1, padx=5, pady=5)
        website.insert(0, item["values"][0])
        username.insert(0, item["values"][1])
        password.insert(0, "yourpassword")
        save_button = Button(small_window, text="Save", bd=0, bg=BOXCOLOR, font=(FONT_NAME, 10))
        delete_button = Button(small_window, text="Delete", bd=0, bg=BOXCOLOR,  font=(FONT_NAME, 10))
        save_button.grid(row=3, column=0, sticky="ew")
        delete_button.grid(row=3, column=1, sticky="ew")


tree.bind("<<TreeviewSelect>>", item_selected)

mainloop()
