# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# ../ == going 1 lvl up in directories
# with open("../../../../../new_file.txt", mode="r") as file:
#     print(file.read())


with open("../../../../../new_file.txt", mode="r") as file:
    print(file.read())
