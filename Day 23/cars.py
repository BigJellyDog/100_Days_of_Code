import time
from turtle import Turtle
import random

STARTING_Y_COORDINATES = [300, 225, 150, 75, 0, -75, -150, -225]
COLORS = ["red", "orange", "yellow", "green", "purple"]
STARTING_MOVING_DISTANCE = 5
WEST = 180


class Car(Turtle):

    def __init__(self):
        self.speed = 5
        self.all_cars = []

    def create_cars(self):
        random_number = random.randint(1, 6)
        if random_number == 6:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.pencolor("black")
            random_y = random.choice(STARTING_Y_COORDINATES)
            new_car.goto(400, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed)


# class Car(Turtle):
#     starting_y_coordinates = [300, 225, 150, 75, 0, -75, -150, -225]
#     color_list = ["red", "green", "blue", "yellow", "orange", "purple", "brown", "magenta", "cyan"]
#     car_speed = 5
#     car_list = []
#     max_attempts = 50
#
#     def __init__(self):
#         super().__init__()
#         self.penup()
#         self.setheading(WEST)
#         self.speed(1)
#         self.shape("square")
#         self.shapesize(1, 2.5)
#         self.goto(random.randint(400, 800), random.choice(self.starting_y_coordinates))
#         self.car_list.append(self)
#
#     def drive(self):
#         for car in self.car_list:
#             car.forward(self.car_speed)
#         for m in range(len(self.car_list)):
#             for j in range(m + 1, len(self.car_list)):
#                 while self.car_list[m].distance(self.car_list[j]) < 50:
#                     self.car_list[m].goto(random.randint(400, 1000), random.choice(self.starting_y_coordinates))
#
#     def restart_car(self):
#         random_x = random.randrange(400, 800)
#         self.goto(random_x, random.choice(self.starting_y_coordinates))
#         """Check for distance between cars"""
#         for m in range(len(self.car_list)):
#             for j in range(m + 1, len(self.car_list)):
#                 while self.car_list[m].distance(self.car_list[j]) < 50:
#                     self.car_list[m].goto(random.randint(400, 1000), random.choice(self.starting_y_coordinates))
#
#     def make_random_cars(self, amount_of_cars):
#         """Make cars"""
#         for n in range(amount_of_cars):
#             self.color(random.choice(self.color_list))
#             self.pencolor("black")
#             self.car_list.append(self.clone())
#         for m in range(len(self.car_list)):
#             for j in range(m + 1, len(self.car_list)):
#                 if self.car_list[m].distance(self.car_list[j]) < 20:
#                     self.relocate_car(self.car_list[j])
#
#     @staticmethod
#     def is_close_to_any(car, others, threshold):
#         for other in others:
#             if car.distance(other) < threshold:
#                 return True
#         return False
#
#     def relocate_car(self, car):
#         new_x = random.randint(400, 1000)
#         new_y = random.choice(self.starting_y_coordinates)
#         car.goto(new_x, new_y)
#
#     def remove_cars(self):
#         for car in self.car_list:
#             car.goto(1000, 1000)
#         self.car_list.clear()
