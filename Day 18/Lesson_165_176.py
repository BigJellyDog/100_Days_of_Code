import random
import turtle
from random import choice

tim = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(800, 800)
tim.shape("turtle")
tim.hideturtle()
tim.color("green")
screen.colormode(255)
tim.speed(10)


def tim_drawing_shapes():
    sides = 3
    for m in range(8):
        a = choice(range(255))
        b = choice(range(255))
        c = choice(range(255))
        for n in range(sides):
            angle = 360/sides
            color = (a, b, c)
            tim.pencolor(color)
            tim.right(angle)
            tim.forward(100)
        sides += 1


def tim_drawing_shapes2():
    sides = 3
    for m in range(8):
        a = choice(range(255))
        b = choice(range(255))
        c = choice(range(255))
        for n in range(sides):
            angle = -360 / sides
            color = (a, b, c)
            tim.pencolor(color)
            tim.right(angle)
            tim.forward(100)
        sides += 1


def tim_random_walk():
    tim.speed(10)
    tim.pensize(10)
    random_walk_length = choice(range(200))
    for number in range(random_walk_length):
        a = choice(range(255))
        b = choice(range(255))
        c = choice(range(255))
        color = (a, b, c)
        # random_move = choice([tim.forward, tim.back])
        # random_turn = choice([tim.left, tim.right])
        # random_action = choice([random_turn(choice([0, 90, 180, 270])), random_move(30)])
        for n in range(5):
            tim.pencolor(color)


def angela_random_walk():
    directions = [0, 90, 180, 270]
    tim.speed(10)
    tim.pensize(10)
    for n in range(200):
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)
        color = (a, b, c)
        tim.pencolor(color)
        tim.forward(30)
        tim.setheading(choice(directions))


def tim_random_circle():
    tim.speed(0)
    for m in range(0, 360, 5):
        a = random.randint(1, 255)
        b = random.randint(1, 255)
        c = random.randint(1, 255)
        color = (a, b, c)
        tim.color(color)
        tim.setheading(m)
        tim.circle(100)


# angela_random_walk()
# tim_random_walk()
# tim_random_circle()
tim_drawing_shapes()
tim_drawing_shapes2()

screen.exitonclick()
