from tkinter import *
import math
import os
import sys

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#E21818"
GREEN = "#65B741"
YELLOW = "#E8C872"
GREY = "#B7C4CF"
ORANGE = "#FC6736"
BLACK = "#000000"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
timer_active = False
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_time, text="00:00")
    timer_text.config(text="BananaTimer", fg=RED)
    check_mark.config(text="")
    global reps, timer_active
    reps = 0
    timer_active = False

# -------------------------------PAUSE MECHANISM---------------------------------#


is_paused = False


def pause_or_resume_timer():
    global is_paused
    if is_paused:
        resume_timer()
    else:
        pause_timer()


def pause_timer():
    global is_paused, timer, timer_active
    window.after_cancel(timer)
    is_paused = True
    timer_active = False
    pause_button.config(text="Resume")


def resume_timer():
    global is_paused, timer, timer_active
    is_paused = False
    timer_active = True
    pause_button.config(text="Pause")
    # Resume countdown from the current timer_text
    current_time = canvas.itemcget(timer_time, "text")
    min, sec = current_time.split(":")
    count = int(min) * 60 + int(sec)
    count_down(count)


# ---------------------------- TIMER MECHANISM ------------------------------- #

def resource_path(relative_path):
    """ Get absolute path to resource, for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

image_path = resource_path('banana.png')

def ring_bell():
    window.bell()


def start_timer():
    global reps, timer_active
    if not timer_active:
        timer_active = True
        reps += 1
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        if reps % 8 == 0:
            count_down(long_break_sec)
            timer_text.config(text="BIGBreak", fg=RED)
            reps = 0
        elif reps % 2 == 0:
            count_down(short_break_sec)
            timer_text.config(text="Break", fg=RED)
        else:
            count_down(work_sec)
            timer_text.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer, timer_active

    count_minute = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_time, text=f"{count_minute}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)

    else:
        if not is_paused:
            timer_active = False
            start_timer()
        marks = ""
        for _ in range(math.floor(reps/4)):
            marks += "✓"
        check_mark.config(text=marks)
        ring_bell()
        window.attributes('-topmost', True)
        window.deiconify()
        window.attributes('-topmost', False)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("BananaClocko")
window.config(padx=0, pady=0, bg=YELLOW)


canvas = Canvas(width=500, height=520, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file=image_path)
canvas.create_image(250, 250, image=tomato)
timer_time = canvas.create_text(200, 200, text="00:00", fill=BLACK, font=(FONT_NAME, 50, "bold"))
canvas.grid(column=1, row=2)

timer_text = Label(text="BananaTimer", bg=YELLOW, fg=RED, font=(FONT_NAME, 50, "bold"))
timer_text.grid(column=1, row=0)
check_mark = Label(bg=YELLOW, fg=RED, font=(FONT_NAME, 50, "bold"))
check_mark.grid(column=1, row=4)


start_button = Button(text="Start", bg=YELLOW, command=start_timer, font=(FONT_NAME, 15, "bold"))
reset_button = Button(text="Reset", bg=YELLOW, command=reset_timer, font=(FONT_NAME, 15, "bold"))
pause_button = Button(text="Pause", bg=YELLOW, command=pause_or_resume_timer, font=(FONT_NAME, 15, "bold"))
pause_button.grid(column=1, row=3)
start_button.grid(column=0, row=3)
reset_button.grid(column=2, row=3)


window.mainloop()
