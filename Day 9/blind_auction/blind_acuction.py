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
        if winner_bet[0] == participant["bet"]:    # selecting the winner to a list
            winner_name.append(participant["name"])


    # if auction_bets.count(winner_bet[0]) > 1:   # counting if there are more than 1 winner
    #     winner_bet.clear()  # clear the list and restart
    #     print("Two people bet the same amount, the auction will restart \n")
    #     return False
    # else:
    #     print(f"The Winner is {winner_name} with a bid of ${winner_bet[0]}")
    #     auction_bets.clear()
    #     return True


bidders = "yes"
while bidders == "yes":     # while loop to add all the bidders to the auction

    name = input("What is your name?: ")
    bet = int(input("What is your bid? $"))
    add_new_participant(the_name=name, money_amount=bet)    # adding people to auction list, need to redo until all
    # ready
    bidders = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    print("\n" * 100)
    print(art.person_art)
    print(art.text_art)
    if bidders == "yes":
        continue

    select_winner_to_list()
    if len(winner_name) > 1:   # counting if there are more than 1 winner
        winner_bet.clear()     # clear the lists and restart
        winner_name.clear()
        auction_bets.clear()
        auction_list.clear()
        print("Two people bet the same amount, the auction will restart \n")
        bidders = "yes"
    else:
        print(f"The Winner is {winner_name[0]} with a bid of ${winner_bet[0]}")
        bidders = "no"
