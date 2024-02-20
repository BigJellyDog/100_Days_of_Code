from tkinter import *
from quiz_brain import QuizBrain
from data import question_data
import requests

THEME_COLOR = "#375362"
FONT = "Arial"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.question_data = None
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.resizable(False, False)
        self.window.configure(bg=THEME_COLOR)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white", padx=20, pady=20)
        self.score.grid(row=0, column=0, columnspan=2)

        self.canvas = Canvas(self.window)
        self.canvas.configure(bg="white", width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=295,
            text="Test text in the canvas",
            font=(FONT, 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        self.false = PhotoImage(file="images/false.png")
        self.true = PhotoImage(file="images/true.png")
        self.restart = PhotoImage(file="images/restart.png")

        self.false_button = Button(
            image=self.false,
            bg=THEME_COLOR,
            activebackground=THEME_COLOR,
            border=0,
            command=self.press_wrong
        )
        self.true_button = Button(
            image=self.true,
            bg=THEME_COLOR,
            activebackground=THEME_COLOR,
            border=0,
            command=self.press_true
        )
        # self.restart_button = Button(
        #     image=self.restart,
        #     bg=THEME_COLOR,
        #     activebackground=THEME_COLOR,
        #     border=0,
        #
        # )

        self.false_button.grid(row=2, column=1, padx=20, pady=20)
        self.true_button.grid(row=2, column=0, padx=20, pady=20)
        # self.restart_button.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end! Your score is {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def press_true(self):
        try:
            is_right = self.quiz.check_answer("True", question_data[self.quiz.q_number]["correct_answer"])
        except IndexError:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end! Your score is {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        else:
            self.give_feedback(is_right)

    def press_wrong(self):
        try:
            is_right = self.quiz.check_answer("False", question_data[self.quiz.q_number-1]["correct_answer"])
        except IndexError:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end! Your score is {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        else:
            self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
            self.window.after(1000, func=self.get_next_question)
        else:
            self.canvas.configure(bg="red")
            self.window.after(1000, func=self.get_next_question)

