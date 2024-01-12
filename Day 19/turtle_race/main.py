from turtle import Turtle, Screen
import random

# Setting up the screen
screen = Screen()
screen.setup(500, 400)
bet = ""
while bet not in ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black']:
    bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: \n"
                                            "-red -orange -yellow -green -blue -purple -black").lower()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black']

# Setting up the turtle
tim = Turtle("turtle")
tim.penup()
tim.goto(-230, -150)
turtle_list = []


def make_turtles(original_turtle, color_list):
    """Make some turtles"""
    s_t = -150  # s_t = starting_point
    for color in color_list:
        clone_turtle = original_turtle.clone()
        turtle_list.append(clone_turtle)
        clone_turtle.color(color)
        clone_turtle.goto(-230, s_t)
        s_t += 50


def turtle_race(turtles):
    """Makes the turtles race and returns the winner's color"""
    start = ""
    while start != "stop":
        rd_turtle = random.choice(turtles)
        rd_distance = random.randint(1, 10)
        rd_turtle.forward(rd_distance)
        (x, y) = rd_turtle.position()
        if x >= 250:
            start = "stop"
            return rd_turtle.pencolor()


make_turtles(tim, colors)
tim.hideturtle()
race_winner = turtle_race(turtle_list)
if race_winner == bet:
    print(f"Congratulation!!! {race_winner.capitalize()} won!!! ")
else:
    print(f"Sorry you lost :( the winner is {race_winner.capitalize()}, better luck next time!")


screen.exitonclick()
