import random
import time
import art
import os
# PC choose a number


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def choose_number():
    """Returning a random number from 1 to 100"""
    number = random.randint(1, 100)
    return number


random_number = choose_number()


def compare_user_input(guessed_number):
    """Takes the guess and returns if it's true or false"""
    global attempts
    if guessed_number > 100 or guessed_number < 1:
        attempts -= 1
        return "BETWEEN 1 AND 100."
    elif guessed_number == random_number:
        return f"You win the number was {guessed_number}!"
    elif guessed_number > random_number:
        attempts -= 1
        return "Too high.\nGuess again"
    elif guessed_number < random_number:
        attempts -= 1
        return "Too low.\nGuess again"


print(art.welcome_to)
time.sleep(3)
print(art.guess)
time.sleep(1)
print(art.the)
time.sleep(1)
print(art.number)
time.sleep(1)
print("With Jelly")
time.sleep(3)
clear()

print("I'm thinking of a number between 1 and 100.")
difficulty = ""
attempts = 5
while difficulty not in ['easy', 'hard']:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == 'easy':
    attempts = 10

# Game starts here
game = True
while game:

    while True:

        user_guess = input(f"You have {attempts} attempts remaining to guess the number.\nMake a guess: ")
        try:
            user_guess = int(user_guess)
            break
        except:
            print("Not funny :( -2 lives")
            attempts -= 2
            continue
    result = compare_user_input(guessed_number=user_guess)
    print(result)
    if "win" in result:
        game = False
    elif attempts == 0:
        clear()
        print(art.lose)
        print(f"The number was {random_number}")
        game = False
