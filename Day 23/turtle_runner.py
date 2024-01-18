from turtle import Turtle


class Runner(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle.gif")
        self.setheading(90)
        self.goto(0, -300)

    def moving_up(self):
        self.forward(20)

