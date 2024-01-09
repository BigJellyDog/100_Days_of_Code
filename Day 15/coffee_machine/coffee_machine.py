"""My coffee machine code by Jelly"""
import resources  # Importing resources with 5 dictionaries of 3 drinks, the menu and the coffe machine resources


def insert_coins(drink_price):
    """Counting inserted coins by user"""
    print("Please insert coins:")
    try:
        quarters = float((int(input("How many quarters?: ")) * 0.25))
        dimes = float((int(input("How many dimes?: ")) * 0.10))
        nickles = float((int(input("How many nickles?: ")) * 0.05))
        pennies = float((int(input("How many pennies?: ")) * 0.01))
    except ValueError:
        return "Invalid input. Please use numbers for coins"
    inserted_value = quarters + dimes + nickles + pennies
    if inserted_value < drink_price:
        return "Sorry that's not enough money. Money refunded."
    else:
        return f"Here is ${round(inserted_value - drink_price, 2)} dollars in change."


coffe_machine = ""
while coffe_machine != "off":
    while coffe_machine not in ["report", "espresso", "cappuccino", "latte", "off"]:
        coffe_machine = input("What would you like? \n☕Espresso: $1.50\n☕Latte: $2.50\n☕Cappuccino: $3.00\n").lower()
    if coffe_machine == "off":
        break
    if "report" in coffe_machine:
        """Printing resources"""
        print(f"Water: {resources.resources['Water']}ml")
        print(f"Milk: {resources.resources['Milk']}ml")
        print(f"Coffee: {resources.resources['Coffee']}g")
        print(f"Money: ${resources.resources['Money']}\n")
        coffe_machine = ""
        continue

    for ingredient in resources.resources:
        """For loop to check for the order and resources"""
        if "Money" in ingredient:
            """Skip money key and add the money to the coffe machine"""
            pass
        elif resources.menu[coffe_machine][ingredient] > resources.resources[ingredient]:
            """Check if there are enough resources to make the drink"""
            print(f"Sorry there is not enough {ingredient}")
            coffe_machine = ""
            break
        else:
            checked_coins = insert_coins(drink_price=resources.menu[coffe_machine]["Money"])
            if "refunded" in checked_coins:
                print(checked_coins)
                coffe_machine = ""
                break
            elif "change" in checked_coins:
                print(checked_coins)
                resources.resources[ingredient] -= resources.menu[coffe_machine][ingredient]
                resources.resources["Money"] += resources.menu[coffe_machine]["Money"]
                print(f"Here is your {coffe_machine.capitalize()}. Enjoy!\n")
                coffe_machine = ""
                break

