import time
from turtle import Turtle
import random
WEST = 180


class Car(Turtle):

    starting_y_coordinates = [300, 225, 150, 75, 0, -75, -150, -225]
    # random_car_numbers = random.randrange(15, 30)
    car_list = []

    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(WEST)
        self.shape("square")
        self.shapesize(1, 2.5)
        self.goto(random.randrange(400, 800), random.choice(self.starting_y_coordinates))

    def drive(self):
        self.forward(5)

    def restart_car(self):
        random_x = random.randrange(350, 400)
        self.goto(random_x, random.choice(self.starting_y_coordinates))

    def make_random_cars(self):
        for n in range(5):
            self.goto(400, random.choice(self.starting_y_coordinates))
            self.car_list.append(self)

    def move_all_cars(self):
        for cars in self.car_list:
            cars.forward(random.randint(1, 5))
            if cars.xcor() < -320:
                cars.goto(400, random.choice(self.starting_y_coordinates))

    def remove_cars(self):
        self.car_list.clear()
