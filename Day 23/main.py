import random
from level_board import Board
import time
from turtle import Screen, Turtle
from turtle_runner import Runner
from road_maker import Road
from cars import Car

screen = Screen()
screen.screensize(600, 600)
screen.setup(700, 700)
screen.register_shape("turtle.gif")
screen.tracer(0)
screen.listen()

# Set up turtle and make it move
player = Runner()
scoreboard = Board()
screen.onkeypress(player.moving_up, "Up")
# Set up cars
cars = Car()


speed = 0.1

game_on = True
while game_on:

    screen.update()
    time.sleep(speed)

    cars.create_cars()
    cars.move_cars()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_on = False

    if player.ycor() > 300:
        cars.speed += 10
        player.goto(0, -300)
        scoreboard.increase_level()


screen.exitonclick()


