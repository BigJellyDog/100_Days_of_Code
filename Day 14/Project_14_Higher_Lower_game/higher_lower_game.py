# Game data is a list with dictionaries inside
import game_data
import random
import art
data = game_data.data


def choose_random_card():
    """Creates 2 random integers for the data list, and returns them"""
    index = random.randint(0, len(data) - 1)
    return index


def game_a_and_b():
    """Chooses 2 random cards and prints the result for the user"""
    index_a = choose_random_card()
    index_b = choose_random_card()
    while index_b == index_a:
        """A while loop so that the cards don't match"""
        index_b = random.randint(0, len(data) - 1)
    card_a = data[index_a]
    card_b = data[index_b]
    score = 0

    game = True
    while game:
        print(art.higher_or_lower)
        print(f"Compare A: {card_a['name']}, a {card_a['description']}, from {card_a['country']}.")
        print(art.vs)
        print(f"Against B: {card_b['name']}, a {card_b['description']}, from {card_b['country']}.")

        user_guess = ""
        while user_guess not in ['H', 'L']:
            """Asking user"""
            user_guess = input(f"{card_b['name']} has Higher or Lower followers than {card_a['name']}? Type 'H' or 'L' : ").upper()

        """Choosing winner"""
        if card_a['follower_count'] > card_b['follower_count']:
            winner = "L"
        else:
            winner = "H"

        """Compare user input to winner and make a new round"""

        if user_guess == winner:
            score += 1
            print(f"You're right! Current score: {score}.")
            index_a = index_b
            index_b = choose_random_card()
            while index_b == index_a:
                """A while loop so that the cards don't match"""
                index_b = random.randint(0, len(data) - 1)
            card_a = data[index_a]
            card_b = data[index_b]
            print("\n"*100)
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game = False


game_a_and_b()
