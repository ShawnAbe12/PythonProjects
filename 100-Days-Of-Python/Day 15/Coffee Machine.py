from Menu import MENU as menu
from Menu import resources

money = 0

cost_penny = 0.01
cost_nickle = 0.05
cost_dime = 0.10
cost_quarter = 0.25

machine_on = True


def check_resources(item):
    list = ["water", "milk", "coffee"]
    for i in list:
        if i in item:
            inside = item[i] <= resources[i]
            if not inside:
                print(f"There is not enough {i}")
                return False
    return True


def insert_coins():
    quarters = int(input("How many Quarters?: "))
    dimes = int(input("How many Dimes?: "))
    nickles = int(input("How many Nickles?: "))
    pennies = int(input("How many Pennies?: "))
    return quarters * cost_quarter + dimes * cost_dime + nickles * cost_nickle + pennies * cost_penny


def restock_item(type_of_restock, amount_to_restock, items_restock):
    items_restock[type_of_restock] += amount_to_restock


# resources["coffee"] = 0

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino) ").lower()
    match choice:
        case choice if choice in menu:
            item = menu[choice]
            item_resources = item["ingredients"]
            # print(f"Ingredients: {item_resources}\nCost: {item['cost']}")
            if check_resources(item_resources):
                print(f"Your total is {item['cost']}, Please insert the coins: ")
                total = insert_coins()
                change = round(total - item["cost"], 2)
                if total < item["cost"]:
                    print(f"You only entered {total}, Money refunded")
                else:
                    if change != 0:
                        print(f"Here is ${change} in change.")
                    print(f"Here is your {choice}, Enjoy!")
                    resources["water"] -= item_resources["water"]
                    if "milk" in item_resources:
                        resources["milk"] -= item_resources["milk"]
                    resources["coffee"] -= item_resources["coffee"]
                    money += item["cost"]
        case "off":
            machine_on = False
            print("The Machine has been turned Off, Goodbye")
            break
        case "report":
            print(
                f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${money}')
        case "restock":
            item_restock = input("What item would you like to restock?: ")
            amount = int(input("How much would you like to restock?: "))
            restock_item(item_restock, amount, resources)
        case _:
            print("This is not a valid menu item")
