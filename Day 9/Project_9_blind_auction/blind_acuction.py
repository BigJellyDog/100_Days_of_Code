import art

auction_list = []
auction_bets = []
winner_bet = []
winner_name = []
print(art.person_art)
print(art.text_art)


def add_new_participant(the_name, money_amount):
    auction_list.append({"name": the_name, "bet": money_amount})


def select_winner_to_list():
    for participant in auction_list:
        auction_bets.append(participant["bet"])
    winner_bet.append(max(auction_bets))
    for participant in auction_list:
        if winner_bet[0] == participant["bet"]:  # selecting the winner to a list
            winner_name.append(participant["name"])


bidders = "yes"
while bidders == "yes":  # while loop to add all the bidders to the auction

    """Asking for user name"""
    name = input("What is your name?: ")
    """Asking for user money with a while loop and try to define an error if he types something else then int value"""
    while True:
        try:
            bet = int(input("What is your bid? $"))
            break
        except:
            """Print a warning for user"""
            print("Please try to use money $$$ starting at $1 ")
    """Add the user to the list of participants"""
    add_new_participant(the_name=name, money_amount=bet)  # adding people to auction list, need to redo until all
    # ready
    while True:
        try:
            bidders = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
            if bidders != 'yes' and bidders != 'no':
                raise NameError("Please type 'yes' or 'no'.")  # Raise NameError with a message
            break
        except NameError as ne:
            print(f"{ne} {art.yes_or_no}")
    print("\n" * 1000)
    print(art.person_art)
    print(art.text_art)
    if bidders == "yes":
        continue

    select_winner_to_list()
    if len(winner_name) > 1:  # counting if there are more than 1 winner
        winner_bet.clear()  # clear the lists and restart
        winner_name.clear()
        auction_bets.clear()
        auction_list.clear()
        print("Two people bet the same amount, the auction will restart \n")
        bidders = "yes"
    else:
        print("\n" * 1000)
        print(art.person_art)
        print(art.winner)
        print(f"The Winner is {winner_name[0]} with a bid of ${winner_bet[0]}")
        bidders = "no"
