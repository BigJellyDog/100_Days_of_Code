from tkinter import *
from tkinter import ttk
from PIL import Image, ImageSequence
from tkinter import messagebox
import io
from random import choice, randint, shuffle
import pyperclip
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


# ----------------------------------- GIF HANDLING --------------------------------------#
def unpack_gif(src):
    # Load Gif
    image = Image.open(src)

    # Get frames and disposal method for each frame
    frames = []
    disposal = []
    for gifFrame in ImageSequence.Iterator(image):
        disposal.append(gifFrame.disposal_method)
        frames.append(gifFrame.convert('P'))

    # Loop through frames, and edit them based on their disposal method
    output = []
    last_frame = None
    # this_frame = None
    for i, loadedFrame in enumerate(frames):
        # Update this_frame
        this_frame = loadedFrame

        # If the disposal method is 2
        if disposal[i] == 2:
            # Check that this is not the first frame
            if i != 0:
                # Pastes thisFrames opaque pixels over lastFrame and appends lastFrame to output
                last_frame.paste(this_frame, mask=this_frame.convert('RGBA'))
                output.append(last_frame)
            else:
                output.append(this_frame)

        # If the disposal method is 1 or 0
        elif disposal[i] == 1 or disposal[i] == 0:
            # Appends this_frame to output
            output.append(this_frame)

        # If disposal method is anything other than 2, 1, or 0
        else:
            raise ValueError(
                'Disposal Methods other than 2:Restore to Background, '
                '1:Do Not Dispose, and 0:No Disposal are supported at this time')

        # Update lastFrame
        last_frame = loadedFrame
    output_photo_images = []
    for frame in output:
        # Save the frame to a bytes buffer
        buffer = io.BytesIO()
        frame.save(buffer, format="GIF")
        buffer.seek(0)

        # Create a PhotoImage from the buffer
        frame_photo = PhotoImage(data=buffer.read())
        output_photo_images.append(frame_photo)

    return output_photo_images
# ------------------------------------SAVE DATA ----------------------------------------- #


def save_data(website_data, username_data, password_data):
    csv_file_path = "data.csv"

    web_data = website_data.get()
    user_data = username_data.get()
    pass_data = password_data.get()

    if (
            web_data in ["", "Website"] or
            user_data in ["", "Username"] or
            pass_data in ["", "Password"]
    ):
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
        return

    new_data = pd.DataFrame({"Website": [web_data], "Username": [user_data], "Password": [pass_data]})

    try:
        existing_data = pd.read_csv(csv_file_path)
        updated_data = pd.concat([existing_data, new_data], ignore_index=True)
    except FileNotFoundError:
        updated_data = new_data

    updated_data.to_csv(csv_file_path, index=False)

    website_data.delete(0, END)
    password_data.delete(0, END)
    username_data.delete(0, END)
    website_data.insert(0, 'Website')
    username_data.insert(0, 'Username')
    password_data.insert(0, 'Password')
    website_data.config(bg=BGCOLOR)
    username_data.config(bg=BGCOLOR)
    password_data.config(bg=BGCOLOR)
    generate_button.config(fg=BGCOLOR, bg=BGCOLOR)
    label.focus()


# ----------------------------------- LIBRARY -------------------------------------- #

def library():
    pass_screen = Tk()
    pass_screen.resizable(False, False)
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
        tree.insert('', END, text=str(i), values=(row["Website"], row["Username"]))

    scrollbar = Scrollbar(pass_screen, orient="vertical", command=tree.yview)
    scrollbar.grid(row=0, column=1, sticky=NS)
    tree['yscrollcommand'] = scrollbar.set

    def confirm_delete(index, small_window):
        confirm_window = Toplevel()
        confirm_window.resizable(False, False)
        confirm_window.title("Confirm Delete")
        confirm_window.configure(bg=BGCOLOR)
        confirm_window.grab_set()

        Label(confirm_window, text="Are you sure?", font=(FONT_NAME, 10), bg=BGCOLOR).pack(
            pady=10)

        yes_button = Button(confirm_window, text="Yes", bd=0, bg=BOXCOLOR, font=(FONT_NAME, 10),
                            command=lambda: [delete_item(index), confirm_window.destroy()])
        yes_button.pack(side=LEFT, padx=10)

        no_button = Button(confirm_window, text="No", bd=0, bg=BOXCOLOR, font=(FONT_NAME, 10),
                           command=lambda: [confirm_window.destroy(), small_window.deiconify()])
        no_button.pack(side=RIGHT, padx=10)

        small_window.withdraw()

    def delete_item(index):
        selected_item = tree.selection()[0]  # Extract the first item from the tuple
        tree.delete(selected_item)  # Remove the item from the tree window_small
        reader.drop(index, inplace=True)  # Remove the row from the DataFrame
        reader.to_csv("data.csv", index=False)  # Save the DataFrame back to the CSV file

    def save_changes(index, website, username, password):
        reader.at[index, "Website"] = website.get()
        reader.at[index, "Username"] = username.get()
        reader.at[index, "Password"] = password.get()
        reader.to_csv("data.csv", index=False)

        tree.item(tree.selection()[0], values=(website.get(), username.get()))

    def item_selected(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            index = int(item['text'])  # Extract index from the tree item
            website_value = item['values'][0]
            username_value = item['values'][1]

            small_window = Tk()
            small_window.resizable(False, False)
            small_window.title(f"{website_value}")
            small_window.configure(bg=BGCOLOR)

            # Setup labels and entries for website, username, and password
            website_label, website_entry_small = setup_label_entry(small_window, "Website:", website_value, 0)
            username_label, username_entry = setup_label_entry(small_window, "Username:", username_value, 1)
            password_label, password_entry_small = setup_label_entry(small_window, "Password:",
                                                                     reader.at[index, "Password"], 2)

            # Setup save and delete buttons
            save_button = Button(small_window, text="Save", bd=0, bg=BOXCOLOR, font=(FONT_NAME, 10),
                                 command=lambda: save_changes(index, website_entry_small,
                                 username_entry, password_entry_small))

            save_button.grid(row=3, column=0, sticky="ew")

            delete_button = Button(small_window, text="Delete", bd=0, bg=BOXCOLOR, font=(FONT_NAME, 10),
                                   command=lambda: [confirm_delete(index, small_window)])
            delete_button.grid(row=3, column=1, sticky="ew")

    def setup_label_entry(window_small, text, initial_value, the_row):
        small_label = Label(window_small, text=text, font=(FONT_NAME, 10), justify="left", bg=BGCOLOR)
        small_label.grid(row=the_row, column=0, padx=10, pady=5)
        entry = Entry(window_small, justify="center", font=(FONT_NAME, 10), bd=0, highlightthickness=0, bg=BGCOLOR)
        entry.grid(row=the_row, column=1, padx=5, pady=5)
        entry.insert(0, initial_value)
        return small_label, entry

    tree.bind("<<TreeviewSelect>>", item_selected)

# ----------------------------------- ############ -------------------------------------- #


def start_animation():
    global frame_index, is_animating
    if is_animating:
        return  # Do nothing if the animation is already running

    frame_index = 0  # Reset to the first frame
    is_animating = True
    update_frame()


def update_frame():
    global frame_index, is_animating, animation_ended
    if not is_animating:
        return  # Exit if the animation has been stopped

    frame = gif_frames[frame_index]
    label.configure(image=frame)
    frame_index += 1

    if frame_index < len(gif_frames):
        window.after(15, update_frame)  # Schedule the next frame update with 15ms delay
    else:
        # When the animation ends, reset necessary variables and call save_data
        is_animating = False
        animation_ended = True  # This now indicates the animation just finished
        frame_index = 0  # Reset for the next animation cycle
        label.configure(image=gif_frames[0])  # Optionally reset to the first frame
        save_data(
                  website_data=website_entry,
                  username_data=email_entry,
                  password_data=password_entry
                  )  # Call save_data function automatically after animation ends


is_animating = False


def on_entry_click(event, entry, text):
    """function that gets called whenever entry is clicked"""
    if entry.get() == text:
        entry.delete(0, "end")
        entry.config(fg=BLUE, bg=EEEECOLOR)
        if entry == password_entry:
            generate_button.config(fg=BLACK, bg=BOXCOLOR)
            generate_button.place(x=60, y=410)


def on_focusout(event, entry, text):
    if entry.get() == '':
        entry.insert(0, text)
        entry.config(fg=BLUE, bg=BGCOLOR)
        if entry == password_entry:
            generate_button.place_forget()


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(6, 8))]
    password_list = password_list + [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_list + [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)

    final_password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, final_password)
    pyperclip.copy(final_password)


# ------------------------------------- ANIMATION HANDLING ----------------------------- #


window = Tk()
window.title("Password Manager")
# Assuming GREY is defined somewhere
window.config(bg=BLACK)
window.geometry("450x450")
window.resizable(False, False)
canvas = Canvas(width=450, height=700, bg=BGCOLOR, highlightthickness=0)
canvas.grid(column=0, row=0, rowspan=4, sticky="nsew")
gif_path = "blue_lock.gif"

# Load gif_frames
gif_frames = unpack_gif(gif_path)
frame_index = 0

if gif_frames:
    label = Label(window, image=gif_frames[0], highlightthickness=0, bg=BGCOLOR)
    label.grid(column=0, row=0, sticky="nsew")  # Use 'nsew' to have the label expand in all directions within the cell
    label.bind("<Button-1>", lambda event: start_animation())

    website_entry = Entry(window, width=15, justify="center", font=(FONT_NAME, 20), bd=0, bg=BGCOLOR,
                          highlightthickness=0, highlightcolor=BOXCOLOR,
                          highlightbackground=BOXCOLOR)
    email_entry = Entry(window, width=15, justify="center", font=(FONT_NAME, 20), bd=0, bg=BGCOLOR,
                        highlightthickness=0, highlightcolor=BOXCOLOR,
                        highlightbackground=BOXCOLOR)
    password_entry = Entry(window, width=20, justify="center", font=(FONT_NAME, 20), bd=0, bg=BGCOLOR,
                           highlightthickness=0, highlightcolor=BOXCOLOR,
                           highlightbackground=BOXCOLOR)

    password_entry.grid(row=3, column=0, pady=10)
    password_entry.insert(0, "Password")
    password_entry.bind('<FocusIn>', lambda event: on_entry_click(event, password_entry, text="Password"))
    password_entry.bind('<FocusOut>', lambda event: on_focusout(event, password_entry, text="Password"))
    password_entry.config(fg=BLUE)

    website_entry.grid(row=1, column=0, padx=8, pady=8)  # The entry is in the next row (1) and expands east-west
    website_entry.insert(0, "Website")
    website_entry.bind('<FocusIn>', lambda event: on_entry_click(event, website_entry, text="Website"))
    website_entry.bind('<FocusOut>', lambda event: on_focusout(event, website_entry, text="Website"))
    website_entry.config(fg=BLUE)

    email_entry.grid(row=2, column=0, padx=8, pady=8)  # The entry is in the next row (1) and expands east-west
    email_entry.insert(0, "Username")
    email_entry.bind('<FocusIn>', lambda event: on_entry_click(event, email_entry, text="Username"))
    email_entry.bind('<FocusOut>', lambda event: on_focusout(event, email_entry, text="Username"))
    email_entry.config(fg=BLUE)

    generate_button = Button(window, text="Generate", font=(FONT_NAME, 10, ), bd=0, bg=BGCOLOR,
                             highlightthickness=0, fg=EEEECOLOR, highlightcolor=BGCOLOR,
                             highlightbackground=BGCOLOR, command=generate_password)
    generate_button.place(x=60, y=410)

    book_image = PhotoImage(file="book50px.png")
    open_library_button = Label(window, image=book_image)
    open_library_button.bind("<Button-1>", lambda event: library())
    open_library_button.config(bg=BGCOLOR)
    open_library_button.place(x=0, y=0)

    # password_frame.columnconfigure(1, weight=1)

    window.grid_rowconfigure(0, weight=1)  # The row with the label can expand
    window.grid_rowconfigure(1, weight=0)
    window.grid_rowconfigure(2, weight=0)
    window.grid_rowconfigure(3, weight=0)
    window.grid_columnconfigure(0, weight=1)

    frame_index = 0  # Reset frame index for the animation
    window.after(0, update_frame)
else:
    print("No gif_frames loaded. Check the GIF file path.")

window.mainloop()
