from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.setheading(random.uniform(0, 360))
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def moving_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.home()
        self.move_speed = 0.1
        self.bounce_x()

    # def reflect_horizontal(self):
    #     angle = self.heading()
    #     self.setheading(180 - angle)
    #
    # def reflect_vertical(self):
    #     angle = self.heading()
    #     self.setheading(-angle + random.uniform(-20, 20))
    #
    # def reflect_paddle(self):
    #     angle = self.heading()
    #     self.setheading(180 - angle + random.uniform(-20, 20))



