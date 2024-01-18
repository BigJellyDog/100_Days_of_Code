from turtle import Turtle


class Road(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(100)
        self.setheading(90)
        self.penup()
        self.goto(300, -300)
        self.forward(20)
        self.pendown()
        self.goto(-300, -280)
        self.forward(40)
