"""Art project program"""
import random
from turtle import Turtle, Screen
import colorgram


colors = colorgram.extract('image.jpg', 35)
color_list = []
for color in colors:
    # rgb = (color.rgb[0], color.rgb[1], color.rgb[2]) # OLD WAY, NEW WAY JUST USE tuple() to tap into the list of
    # tuples
    # color_list.append(rgb)
    color_list.append(color.rgb)

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.penup()
tim.hideturtle()


def cool_turtle():
    for y in range(-375, 450, 50):
        for x in range(-450, 500, 50):
            tim.goto(x, y)
            tim.dot(15, random.choice(color_list))


# def tim_paint_picture(coloring_list):
#     tim.speed(0)
#     x = -500
#     y = -375
#     for m in range(17):
#         coordinates = (x, y)
#         tim.penup()
#         tim.goto(coordinates)
#         tim.pendown()
#         y += 50
#         for count in range(20):
#             tim.color(random.choice(colors).rgb)  # better method to use it
#             # tim.color(coloring_list[random.randint(0, len(coloring_list)-1)])
#             tim.dot(15)
#             tim.penup()
#             tim.forward(50)
#             tim.pendown()


# tim_paint_picture(color_list)
cool_turtle()
screen.exitonclick()
