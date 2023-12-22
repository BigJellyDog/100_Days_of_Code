auction_list = []
auction_bets = []
auction_winner = []


def add_new_participant(the_name, money_amount):
    auction_list.append({"name": the_name, "money": money_amount})


def choose_winner():
    for participant in auction_list:
        auction_bets.append(participant["money"])

    auction_winner.append(max(auction_bets))
    for participant in auction_list:
        if auction_winner[0] == participant["money"]:
            print(participant["name"])


add_new_participant("Chris", 1000)
add_new_participant("Oscar", 2000)


choose_winner()


