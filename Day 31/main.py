from tkinter import *
import pandas as pd


BACKGROUND_COLOR = "#b1ddc6"
CARD_BACK_COLOR = "#91c2af"
FONT = "Ariel"
random_row = pd.read_csv("spanish_words.csv").sample(n=1)
data = pd.read_csv("spanish_words.csv")

# ----------------------------------------------  BUTTON ACTIONS  ---------------------------------------------------- #


def reset():
    global data

    data = pd.read_csv("spanish_words.csv")

    for index, row in data.iterrows():

        if pd.notna(row['knownSpanish']) and pd.notna(row['knownEnglish']):
            data.at[index, 'Spanish'] = row['knownSpanish']
            data.at[index, 'English'] = row['knownEnglish']

            data.at[index, 'knownSpanish'] = pd.NA
            data.at[index, 'knownEnglish'] = pd.NA

    data.to_csv("spanish_words.csv", index=False)


def remove():
    global random_row, data

    index_of_random_row = random_row.index[0]

    data.loc[index_of_random_row, 'knownSpanish'] = data.loc[index_of_random_row, 'Spanish']
    data.loc[index_of_random_row, 'knownEnglish'] = data.loc[index_of_random_row, 'English']

    data.loc[index_of_random_row, 'Spanish'] = pd.NA
    data.loc[index_of_random_row, 'English'] = pd.NA

    data.to_csv("spanish_words.csv", index=False)

    next_card()


def next_card():
    global random_row, timer, data

    main_window.after_cancel(timer)

    data = pd.read_csv("spanish_words.csv")

    while random_row['Spanish'].isna().any() or random_row['English'].isna().any():
        random_row = data.sample(n=1)

    available_data = data[data['Spanish'].notna() & data['English'].notna()]

    # Safeguard against an empty DataFrame
    if not available_data.empty:
        random_row = available_data.sample(n=1)

        random_spanish_word = random_row.iloc[0]['Spanish']

        card_title.config(text="Spanish", bg="white", fg="black")
        card_word.config(text=random_spanish_word, bg="white", fg="black")
        flash_card_canvas.itemconfig(canvas_image, image=card_front)

        # Reset the timer for flipping the card
        timer = main_window.after(3000, func=flip_card)
    else:
        # Handle the case where all words have been moved to known
        card_title.config(text="Well Done!", bg="white", fg="black")
        card_word.config(text="No more words left.", bg="white", fg="black")
        flash_card_canvas.itemconfig(canvas_image, image=card_front)

        reset()


def flip_card():

    random_english_word = random_row.iloc[0]['English']

    flash_card_canvas.itemconfig(canvas_image, image=card_back)
    card_title.config(text="English", fg="white", bg=CARD_BACK_COLOR)
    card_word.config(text=random_english_word, fg="white", bg=CARD_BACK_COLOR)


# ----------------------------------------------  MAIN WINDOW  ------------------------------------------------------- #

main_window = Tk()
main_window.title("Flashy")
main_window.resizable(False, False)
main_window.config(bg=BACKGROUND_COLOR)

timer = main_window.after(3000, func=flip_card)

# ----------------------------------------------  LOAD IMAGES   ------------------------------------------------------ #

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
reset_image = PhotoImage(file="images/reset.png")

# -------------------------------------------------  CANVAS   -------------------------------------------------------- #


flash_card_canvas = Canvas(main_window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card_canvas.grid(row=0, column=0, rowspan=2, columnspan=3, padx=50, pady=50)
canvas_image = flash_card_canvas.create_image(400, 263, image=card_front, anchor=CENTER)

# -------------------------------------------------  BUTTONS   ------------------------------------------------------- #

# Red button
wrong_button = Button(
    image=wrong_image, highlightthickness=0, bd=0,
    activebackground=BACKGROUND_COLOR, command=next_card)
# active background is used to remove the white space when pressing the button to visually look better
wrong_button.grid(row=3, column=0)
# Green button
right_button = Button(
    image=right_image, highlightthickness=0, bd=0, bg=BACKGROUND_COLOR,
    activebackground=BACKGROUND_COLOR, command=remove)
right_button.grid(row=3, column=2, pady=50)

reset_button = Button(image=reset_image, bg=BACKGROUND_COLOR, bd=0, activebackground=BACKGROUND_COLOR,
                      text="reset", command=reset)
reset_button.grid(row=3, column=1)

# --------------------------------------------------  TEXT   --------------------------------------------------------- #

card_title = Label(main_window, text="Spanish", bg="white", font=(FONT, 40, "italic"))
card_title.grid(row=0, column=0, columnspan=3, pady=50)

card_word = Label(main_window, text="Word", bg="white", font=(FONT, 60, "bold"))
card_word.grid(row=1, column=0, columnspan=3, sticky=N)

# ---------------------------------------------------  DATA   -------------------------------------------------------- #


next_card()

mainloop()
