# HINT: You can call clear() to clear the output in the console.

# print out the logo and welcome message

print("Welcome to the silent auction!!!")

# create empty dictionary
bids = {}
bid_cycle = False

while bid_cycle == False:
    # ask for user input
    bid_name = input("What is your name?: ").lower()
    bid_amount = int(input("What is your bid? $"))

    # store data in the dictionary
    bids[bid_name] = bid_amount

    # ask if any other bidders
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    # if yes, clear and repeate the above 3 steps
    if other_bidders == "yes":
        pass
    else:
        bid_cycle = True
    # if no, check for highest bidder and print out the winner

# check the highest value in the dictionary and print out the winner
winning_bid = max(bids)

print(f"The winner of the silent auction is {winning_bid} with a bid of ${bids[winning_bid]}")