# Coffee machine menu and resources
MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    },
}

resources = {
    "water": {"quantity": 300, "unit": "ml"},
    "milk": {"quantity": 200, "unit": "ml"},
    "coffee": {"quantity": 100, "unit": "g"},
}

earnings = 0
machine_on = True


def check_ingredients(needed_ingredients):
    """Check if there are enough ingredients to make the drink."""
    for ingredient, amount in needed_ingredients.items():
        if amount > resources[ingredient]['quantity']:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


def collect_payment():
    """Collect and return the total payment made."""
    print("Please insert coins.")
    coin_values = {'quarters': 0.25, 'dimes': 0.10, 'nickels': 0.05, 'pennies': 0.01}
    total_payment = 0.0
    for coin, value in coin_values.items():
        amount = int(input(f"How many {coin}? "))
        total_payment += amount * value
    return total_payment


def process_payment(money_received, drink_cost):
    """Process the payment and return whether it was successful."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global earnings
        earnings += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_drink(drink_name, ingredients):
    """Make the drink by deducting the ingredients from the resources."""
    for ingredient, amount in ingredients.items():
        resources[ingredient]['quantity'] -= amount
    print(f"Here is your {drink_name} ☕. Enjoy!")


def display_resources():
    """Display the current resources and earnings."""
    for resource, details in resources.items():
        print(f"{resource.capitalize()}: {details['quantity']}{details['unit']}")
    print(f"Earnings: ${earnings}")


def get_user_choice():
    """Get and return the user's drink choice."""
    return input("What would you like? (espresso/latte/cappuccino): ").lower()


def handle_shutdown():
    """Handle the shutdown of the coffee machine."""
    global machine_on
    machine_on = False
    print("Shutting down. Goodbye!")


def handle_resources():
    """Handle the display of current resources."""
    display_resources()


def handle_drink_order(choice):
    """Handle the drink order process."""
    drink = MENU[choice]
    if check_ingredients(drink["ingredients"]):
        payment = collect_payment()
        if process_payment(payment, drink["cost"]):
            make_drink(choice, drink["ingredients"])


def handle_order():
    """Handle user orders and process the coffee machine operations."""
    global machine_on
    while machine_on:
        choice = get_user_choice()
        if choice == "shutdown":
            handle_shutdown()
        elif choice == "resources":
            handle_resources()
        elif choice in MENU:
            handle_drink_order(choice)
        else:
            print("Invalid choice. Please select from espresso, latte, or cappuccino.")


# Start the coffee machine
handle_order()
