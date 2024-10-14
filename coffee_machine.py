from recipes import MENU


def get_user_choice():
    ''' Gets a choice from user. Validates the input and keeps asking for
    user inputs till user enters a valid input. '''
    valid_choices = ['espresso', 'latte', 'cappuccino', 'off', 'report']
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    while choice not in valid_choices:
        print("Please choose one of the following options:\nespresso\nlatte\ncappuccino\n")
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return choice


def print_report(resources):
    ''' Displays a report related to available resources and money. '''
    print('Resources available:')
    print(f'- Water:    {resources["water"]} ml')
    print(f'- Milk:     {resources["milk"]} ml')
    print(f'- Coffee:   {resources["coffee"]} g')
    print(f'- Money:    ${resources["money"]}')


def get_input_coins(message):
    ''' Gets number of coins from the user as input, validates if the entered
    value is a number. The user is repeatedly asked to enter a valid value
    untill user input is valid. '''
    coins = input(f'{message}: ')
    while not coins.isdigit():
        print('Please enter a valid number.')
        coins = input(f'{message}: ')
    return int(coins)


def get_coins_from_user(choice):
    ''' Gets input coins (quarters, dimes, nickles, pennies) from the user. '''
    print(f"Price of {choice} is ${MENU[choice]["cost"]}")
    print('Please insert coins.')
    quarters = get_input_coins('how many quarters?')
    dimes = get_input_coins('how many dimes?')
    nickles = get_input_coins('how many nickles?')
    pennies = get_input_coins('how many pennies?')
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total


def is_resource_available(avail_resources, choice):
    ''' Checks whether resources needed to make coffee are available. '''
    required_resources = MENU[choice]["ingredients"]
    for resource in required_resources:
        if required_resources[resource] > avail_resources[resource]:
            print(f"Sorry there isn't enough {resource}.")
            return False
    return True


def update_available_resources(resources, choice):
    ''' Update the available resources and money. '''
    required_resources = MENU[choice]["ingredients"]
    resources["water"] -= required_resources["water"]
    resources["milk"] -= required_resources["milk"]
    resources["coffee"] -= required_resources["coffee"]
    resources["money"] += MENU[choice]["cost"]
    return resources


def order_cofee(resources, choice):
    ''' Method to proces coffee orders from users. It first checks
    availability of resources. If resources are available, then
    asks user to enter coins. If user has entered enough coins. It
    returns change and serves coffee to the user.'''
    required_cost = MENU[choice]["cost"]
    resource_available = is_resource_available(resources, choice)
    if resource_available:
        money_received = get_coins_from_user(choice)
        if money_received >= required_cost:
            resources = update_available_resources(resources, choice)
            return_change = round((money_received - required_cost), 2)
            print(f"Here is ${return_change} in change.")
            print(f"Here is your {choice} ☕️. Enjoy!")
        else:
            print(f"Sorry that's not enough money. Money refunded. ")
    return resources


def main():
    ''' Main method for executing coffee machine functionalities. '''
    # Initial resource availability
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0,
    }
    choice = ''
    while choice != 'off':
        choice =  get_user_choice()
        if choice == 'report':
            print_report(resources)
        elif choice in ['espresso', 'latte', 'cappuccino']:
            resources = order_cofee(resources, choice)
        elif choice == 'off':
            print('Turning off the coffee machine.')


if __name__ == "__main__":
    main()
