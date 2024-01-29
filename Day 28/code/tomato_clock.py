from tkinter import *
import math
import os
import sys

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#E21818"
GREEN = "#65B741"
YELLOW = "#f7f5dd"
GREY = "#B7C4CF"
ORANGE = "#FC6736"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_time, text="00:00")
    timer_text.config(text="TomatoTimer", fg=RED)
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def resource_path(relative_path):
    """ Get absolute path to resource, for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

image_path = resource_path('tomato_tomato.png')

def ring_bell():
    window.bell()


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_text.config(text="BIGBreak", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_text.config(text="Break", fg=RED)
    else:
        count_down(work_sec)
        timer_text.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    count_minute = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_time, text=f"{count_minute}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✓"
        check_mark.config(text=marks)
        ring_bell()
        window.attributes('-topmost', True)
        window.deiconify()
        window.attributes('-topmost', False)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("TomatoClocko")
window.config(padx=100, pady=50, bg=GREY)


canvas = Canvas(width=500, height=520, bg=GREY, highlightthickness=0)
tomato = PhotoImage(file=image_path)
canvas.create_image(250, 260, image=tomato)
timer_time = canvas.create_text(250, 290, text="00:00", fill="white", font=(FONT_NAME, 50, "bold"))
canvas.grid(column=1, row=2)

timer_text = Label(text="TomatoTimer", bg=GREY, fg=RED, font=(FONT_NAME, 50, "bold"))
timer_text.grid(column=1, row=0)
check_mark = Label(bg=GREY, fg=RED, font=(FONT_NAME, 50, "bold"))
check_mark.grid(column=1, row=4)


start_button = Button(text="Start", bg=GREY, command=start_timer, font=(FONT_NAME, 15, "bold"))
reset_button = Button(text="Reset", bg=GREY, command=reset_timer, font=(FONT_NAME, 15, "bold"))
start_button.grid(column=0, row=3)
reset_button.grid(column=2, row=3)


window.mainloop()
