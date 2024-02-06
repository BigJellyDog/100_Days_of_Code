from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

PINK = "#e2979c"
RED = "#E21818"
GREEN = "#65B741"
YELLOW = "#E8C872"
GREY = "#2d2f3c"
ORANGE = "#FC6736"
BLACK = "#000000"
FONT_NAME = "TkMenuFont"
# ---------------------------------------PASSWORD GENERATOR -------------------------------------#


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                    'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list = password_list + [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_list + [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)

    final_password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, final_password)
    pyperclip.copy(final_password)

# --------------------------------------SAVE PASSWORD------------------------------------------- #


def save_data():
    data = f"{website_str.get()} | {email_str.get()} | {password_str.get()} |\n"

    if len(website_str.get()) < 1 or len(password_str.get()) < 1:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=website_str.get(),
                                       message=f"There are the details entered: \nEmail: {email_str.get()}"
                                               f"\nPassword: {password_str.get()}\n Is it ok to save?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(data)
            website_input.delete(0, END)
            password_input.delete(0, END)
            email_input.delete(0, END)
            website_input.insert(0, "Website:")
            email_input.insert(0, "Email/Username:")
            password_input.insert(0, "Password:")
            website_input.focus()

# --------------------------------------- UPDATING GIF --------------------------------------#


# --------------------------------------- UI ----------------------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=0, pady=0, bg=GREY)

# making canvas and the
canvas = Canvas(width=200, height=200, bg=GREY, highlightthickness=0)
lock = PhotoImage(file="redlock3D.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(column=1, row=0)
# Icon for the logo
icon = PhotoImage(file="redlock3D.png")
window.call('wm', 'iconphoto', window, icon)

website = Label(text="Website:", bg=GREY, fg="white", font=(FONT_NAME, 10, "bold"))
# website.grid(column=0, row=1, sticky="e")
email_username = Label(text="Email/Username:", bg=GREY, fg="white", font=(FONT_NAME, 10, "bold"))
# email_username.grid(column=0, row=2)
password = Label(text="Password:", bg=GREY, fg="white", font=(FONT_NAME, 10, "bold"))
# password.grid(column=0, row=3, sticky="e")

website_str = StringVar()
website_input = Entry(textvariable=website_str, width=35)
website_input.focus()
email_str = StringVar()
email_input = Entry(textvariable=email_str, width=35)
password_str = StringVar()
password_input = Entry(textvariable=password_str, width=35)
website_input.grid(column=1, row=1, columnspan=2, sticky="w")
email_input.grid(column=1, row=2, columnspan=2, sticky="w")
password_input.grid(column=1, row=3, sticky='w')

# ------------- starting insert ------------------- #
website_input.insert(0, "Website:")
email_input.insert(0, "Email/Username:")
password_input.insert(0, "Password:")

generate_password_button = Button(text="Generate Password", command=generate_password, bg=GREY, fg="white", font=(FONT_NAME, 8, "bold"))
generate_password_button.grid(column=1, row=4, sticky="e")
add_button = Button(text="Add", bg=GREY, width=11, command=save_data, fg="white", font=(FONT_NAME, 8, "bold"))
add_button.grid(column=1, row=4, sticky="w")

window.mainloop()
