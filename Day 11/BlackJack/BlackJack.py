import random
import art
import time

suits = ('♥', '♦', '♠', '♣')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10,
          'A': 11}

player_balance = 1000


def bet_input(s):
    """Asking for user input and returning it as a float number"""
    while True:

        user_bet = input(s)
        try:
            user_bet = int(user_bet)
            if user_bet not in range(1, player_balance + 1):
                print(f"A number starting from $1 to ${player_balance}")
                continue
            else:
                break
        except:
            print(f"Please choose an amount from your balance")
            continue

    return user_bet


def player_deal():
    """Deals a card to the players hand"""
    player_cards.append(deal_card(player_cards + computer_cards))


def comp_deal():
    """Deals a card to the cp player"""
    computer_cards.append(deal_card(player_cards + computer_cards))


def deal_card(used_cards):
    """Return a random card from the deck."""
    while True:
        suit = random.choice(suits)
        rank = random.choice(ranks)
        card = (rank, suit)
        if card not in used_cards:
            used_cards.append(card)
            return card


def calc_score(cards):
    """Calculate the total value"""
    score = sum(values[card[0]] for card in cards)
    aces_count = sum(1 for card in cards if card[0] == 'A')

    while score > 21 and aces_count:
        score -= 10
        aces_count -= 1

    return score


def check_if_bust(score):
    if score > 21:
        return "Player bust. You lose!"


def compare(player_one_score, player_two_score):
    """Compare the scores to get a winner"""
    if player_one_score > 21:
        return "Player bust. You lose!"
    elif player_two_score > 21:
        return "Computer busted. You win!"
    elif player_one_score == player_two_score:
        return "It's a draw!"
    elif player_one_score == 21:
        return "21! You win!"
    elif player_two_score == 21:
        return "Computer got 21, You lose!"
    elif player_one_score > player_two_score:
        return "You win!"
    else:
        return "You lose!"


def card_art(s):
    """Draws the card on the board"""
    pcarddisplay = []
    pcarddisplay.append("┌─────────────┐")
    pcarddisplay.append("│ {}           │")
    pcarddisplay.append("│             │")
    pcarddisplay.append("│             │")
    pcarddisplay.append("│     {}     │")
    pcarddisplay.append("│             │")
    pcarddisplay.append("│             │")
    pcarddisplay.append("│           {} │")
    pcarddisplay.append("└─────────────┘")

    if s[:1] == '1':
        x = ("│ ", s[:1] + "0", "          │")
        pcarddisplay[1] = "".join(x)

        x = ("│          ", s[:1] + "0", " │")
        pcarddisplay[7] = "".join(x)
    else:
        x = ("│ ", s[:1], "           │")
        pcarddisplay[1] = "".join(x)

        x = ("│           ", s[:1], " │")
        pcarddisplay[7] = "".join(x)

    if "♦" in s:
        pcarddisplay[4] = "│      ♦\u2002     │"
    if "♣" in s:
        pcarddisplay[4] = "│      ♣\u2002     │"
    if "♥" in s:
        pcarddisplay[4] = "│      ♥\u2002     │"
    if "♠" in s:
        pcarddisplay[4] = "│      ♠\u2002     │"
    if "?" in s:
        pcarddisplay[4] = "│      ?      │"
    return pcarddisplay


# print('\n'.join(map('  '.join, zip(*(card_art(c)for c in computer_display)))))
# print('\n'.join(map('  '.join, zip(*(card_art(c) for c in player_display)))))
# print('\n'.join(map('  '.join, zip(*(card_art(c)for c in computer_display_one_card)))))


game = True
while game:

    cp_turn = False
    print(art.welcome_to_blackjack)
    start = input(art.would_you_like_to_play)  # Player presses Enter to start playing
    # print("\n" * 1000)
    if player_balance == 0:
        print(art.no_money)
        print(art.better_luck_next_time)
        break

    bet = bet_input(f"Make a bet to start playing: Your balance is ${player_balance}: ")
    player_balance -= bet

    player_cards = []
    computer_cards = []

    player_deal()
    player_deal()
    comp_deal()
    comp_deal()

    player_display = []
    for x, y in player_cards:
        player_display.append(str(x + " " + y))

    computer_display = []

    computer_display_one_card = [str(computer_cards[0][0]) + " " + computer_cards[0][1], "?"]

    for x, y in computer_cards:
        computer_display.append(str(x + " " + y))

    print("Dealer cards are: ")
    print('\n'.join(map('  '.join, zip(*(card_art(c) for c in computer_display_one_card)))))
    print(f"Your cards are: ", f"Your balance is ${player_balance}")
    print('\n'.join(map('  '.join, zip(*(card_art(c) for c in player_display)))))

    player_turn = True
    while player_turn:
        player_score = calc_score(player_cards)
        cp_score = calc_score(computer_cards)
        if check_if_bust(player_score):
            print(check_if_bust(player_score))
            break
        if player_score == 21:
            print(f"BlackJack! You got {player_score} You win ${bet * 2}!")
            player_turn = False
            player_balance += bet * 2
            break
        else:
            hit_or_stand = input("Choose H or S to Hit or Stand: ").lower()
            if hit_or_stand == "h":
                player_deal()
                player_display = []
                for x, y in player_cards:
                    player_display.append(str(x + " " + y))
                print("\n" * 100)
                print(art.blackjack_line)
                print("Dealer cards are: ")
                print('\n'.join(map('  '.join, zip(*(card_art(c) for c in computer_display)))))
                print(f"Your cards are: ", f"Your balance is ${player_balance}")
                print('\n'.join(map('  '.join, zip(*(card_art(c) for c in player_display)))))
                if check_if_bust(calc_score(player_cards)):
                    print(f"Player bust. LOSER! Your score is {calc_score(player_cards)}")
                    break
            elif hit_or_stand == "s":
                print("\n" * 100)
                print(art.blackjack_line)
                print("Dealer cards are: ")
                print('\n'.join(map('  '.join, zip(*(card_art(c) for c in computer_display)))))
                print(f"Your cards are: ", f"Your balance is ${player_balance}")
                print('\n'.join(map('  '.join, zip(*(card_art(c) for c in player_display)))))
                player_turn = False
                cp_turn = True

    while cp_turn:
        print("\n" * 100)
        comp_deal()
        computer_display = []
        for x, y in computer_cards:
            computer_display.append(str(x + " " + y))
        print(art.blackjack_line)
        print("Dealer cards are: ")
        print('\n'.join(map('  '.join, zip(*(card_art(c) for c in computer_display)))))
        print(f"Your cards are: ")
        print('\n'.join(map('  '.join, zip(*(card_art(c) for c in player_display)))))
        time.sleep(2)
        cp_score = calc_score(computer_cards)
        player_score = calc_score(player_cards)
        if cp_score > 21:
            print(f"Dealer Busted with {cp_score}! You win ${bet * 2}!")
            player_balance += bet * 2
            print(f"Your Balance is: ${player_balance}")
            break
        elif cp_score == 21 and player_score == 21:
            print(f"It's a Draw!")
            print(f"You get your money back")
            player_balance += bet
            break
        elif cp_score > player_score:
            print(f"Dealer Win with {cp_score}! You lose with {player_score}!")
            print(f"Your balance is: ${player_balance}")
            break

    play_again = ""
    while play_again not in ["y", "n"]:
        play_again = input("Want to play again? Y or N: ").lower()
        if play_again == "y":
            game = True
        else:
            game = False
            print(art.good_bye)
