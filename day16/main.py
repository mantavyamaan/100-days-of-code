from menu import Menu
from day16.coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import sys

money_machine = MoneyMachine()
menu=Menu()
coffee_maker=CoffeeMaker()

print("Welcome to Coffee Machine!")
while True:
    options=menu.get_items()
    choice=input(f"What would you like to have: {options}? ")
    if choice=="off":
        sys.exit()
    elif choice=="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)