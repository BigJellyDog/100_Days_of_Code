import random
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
tim = Runner()
screen.onkeypress(tim.moving_up, "Up")

car = Car()
car.make_random_cars()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.01)

    for cars in car.car_list:
        cars.drive()



screen.exitonclick()

# TODO: Set up cars
# TODO: Set up road later
# TODO: Set up level logic
# TODO: Set up collision with cars
