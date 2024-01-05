# enemies = 1
#
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")


# increase_enemies()
# print(f"enemies outside function: {enemies}")


# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
#
# drink_potion()


player_health = 10


def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    # drink_potion()


if 3 > 2:
    a_variable = 10     # This is still a global scope


# game_level = 3
#
#
# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]
#
#     print(new_enemy)
#
#



enemies = 1


def increase_enemies():
    global enemies
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


PI = 3.14159    # Uppercase means not modify anything
