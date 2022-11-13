MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_enough_resource(drink_ordered):
    """check resources are sufficient to make selected drink"""
    for item in drink_ordered:
        if drink_ordered[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False

    return True


def update_resource(drink_ordered):
    """updates resources after each order"""
    for item in drink_ordered:
        resources[item] -= drink_ordered[item]


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


total_sales = 0

on = True

# TODO: 1. Print a report of all coffee machine resources
while on:
    cust_choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

    if cust_choice == "off":
        on = False
    elif cust_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Total_Sales: ${total_sales}")
    else:
        drink = MENU[cust_choice]
        if check_enough_resource(drink['ingredients']):
            total_coins = process_coins()
            if total_coins < drink['cost']:
                print(f"Sorry that's not enough money. Money refunded.")
            else:
                print(f"Here is your {cust_choice} ☕. Enjoy!")
                total_sales += drink['cost']
                update_resource(drink['ingredients'])
                if total_coins > drink['cost']:
                    change = round((total_coins - drink['cost']), 2)
                    print(f"Here is your change: ${change}.")
        # else:
        #     check_enough_resource(drink['ingredients'])

