from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

machine = ""
while machine != "off":

    machine = input(
        f"What would you like?\n"
        f"Espresso ${menu.find_drink('espresso').cost}\n"
        f"Latte ${menu.find_drink('latte').cost}\n"
        f"Cappuccino ${menu.find_drink('cappuccino').cost}\n").lower()

    if machine == "report":
        CoffeeMaker.report(coffee_machine)
        MoneyMachine.report(money_machine)

    elif machine in ["latte", "espresso", "cappuccino"]:
        order = menu.find_drink(machine)
        if coffee_machine.is_resource_sufficient(order):
            if money_machine.make_payment(order.cost):
                coffee_machine.make_coffee(order)
        else:
            continue
