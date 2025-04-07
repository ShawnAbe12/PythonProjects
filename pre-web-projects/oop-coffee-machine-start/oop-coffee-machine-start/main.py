from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
maker = CoffeeMaker()
money_machine = MoneyMachine()

Machine_on = True
while Machine_on:
    choice = input(f"What would you like? {menu.get_items()}: ").lower()
    if choice == "report":
        maker.report()
        money_machine.report()
    elif choice == "off":
        Machine_on = False
    elif menu.find_drink(choice):
        Item = menu.find_drink(choice)
        if maker.is_resource_sufficient(Item) and money_machine.make_payment(Item.cost) :
            maker.make_coffee(Item)




