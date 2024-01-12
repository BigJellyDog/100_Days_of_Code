from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed(0)
tim.shape("turtle")


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.back(10)


def move_left():
    tim.left(10)


def move_right():
    tim.right(10)


def clear_drawing():
    tim.goto(0, 0)
    tim.clear()


screen.listen()

screen.onkeypress(key="Up", fun=move_forwards)
screen.onkeypress(key="Down", fun=move_backwards)
screen.onkeypress(key="Left", fun=move_left)
screen.onkeypress(key="Right", fun=move_right)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()
