import random
import my_module  # import your own file with the import function

random_integer = random.randint(1, 100)
print(random_integer)
print(my_module.numbers)  # use the values from other files by calling the file_name.value_name - cool stuff
random_float = random.random() * 5
print(random_float)


states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut"]
states_of_america[1] = "Pencilvania"
states_of_america.extend(["Angelaland", "Jack Bauer Land"])
print(states_of_america)
