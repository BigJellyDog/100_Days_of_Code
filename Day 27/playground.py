def add(*args):
    return sum(args)


# print(add(100, 2000, 300, 400, 500, 234, 23432))

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


# calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT-R", seats=4, colour="green")

print(my_car.model)
print(my_car.make)
print(my_car.colour)
print(my_car.seats)