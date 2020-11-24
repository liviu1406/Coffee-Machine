# Write your code here
water = 400
milk = 540
cb = 120
d_cups = 9
money = 550


def menu():
    print(f'The coffee machine has:\n'
          f'{water} of water\n'
          f'{milk} of milk\n'
          f'{cb} of coffee beans\n'
          f'{d_cups} of disposable cups\n'
          f'{money} of money\n')


def action():
    print(f'Write action (buy, fill, take, remaining, exit):')


def buy():
    choice = input(f'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
    global water, milk, cb, d_cups, money
    if choice == '1':
        if water > 250 and cb > 16 and d_cups > 1:
            water -= 250
            cb -= 16
            d_cups -= 1
            money += 4
            print('I have enough resources, making you a coffee!\n')
            choose_actions()
        else:
            print('Sorry, not enough water' if water < 250 else 'Sorry, not enough coffee beans' if cb < 16
            else 'Sorry, not enough disposable cups' if d_cups < 1 else 'Check the code in buy() if == 1')
            print()
            choose_actions()
    elif choice == '2':
        if water > 350 and milk > 75 and cb > 20 and d_cups > 1:
            water -= 350
            milk -= 75
            cb -= 20
            d_cups -= 1
            money += 7
            print('I have enough resources, making you a coffee!\n')
            choose_actions()
        else:
            print('Sorry, not enough water' if water < 350 else 'Sorry, not enough milk' if milk < 75
            else 'Sorry, not enough coffee beans' if cb < 16
            else 'Sorry, not enough disposable cups' if d_cups < 1
            else 'Check the code in buy() if == 2')
            print()
            choose_actions()
    elif choice == '3':
        if water > 200 and milk > 100 and cb > 12 and d_cups > 1:
            water -= 200
            milk -= 100
            cb -= 12
            d_cups -= 1
            money += 6
            print('I have enough resources, making you a coffee!\n')
            choose_actions()
        else:
            print('Sorry, not enough water' if water < 200 else 'Sorry, not enough milk' if milk < 100
            else 'Sorry, not enough coffee beans' if cb < 12
            else 'Sorry, not enough disposable cups' if d_cups < 1
            else 'Check the code in buy() if == 2')
            print()
            choose_actions()
    elif choice == 'back':
        choose_actions()  # changed from menu()
    else:
        print(f'Sorry, not enough resources!\n')  # to be changed accordingly
        choose_actions()


def fill():
    global water, milk, cb, d_cups, money
    print('Write how many ml of water do you want to add:')
    add_water = int(input())
    print('Write how many ml of milk do you want to add:')
    add_milk = int(input())
    print('Write how many grams of coffee beans do you want to add:')
    add_cb = int(input())
    print(f'Write how many disposable cups of coffee do you want to add:')
    add_d_cups = int(input())

    water += add_water
    milk += add_milk
    cb += add_cb
    d_cups += add_d_cups
    print()
    choose_actions()


def take():
    global water, milk, cb, d_cups, money
    print()
    print(f'I gave you ${money}')
    print()
    money -= money
    choose_actions()


def remaining():
    print()
    make_coffee()


def exit_coffee():
    exit()


def make_coffee():
    menu()
    action()
    select = input()
    while True:
        if select == 'buy':
            buy()
        elif select == 'fill':
            fill()
        elif select == 'take':
            take()
        elif select == 'remaining':
            remaining()
        elif select == 'exit':
            exit_coffee()


def choose_actions():
    action()
    select = input()
    while True:
        if select == 'buy':
            # print()
            buy()
        elif select == 'fill':
            # print()
            fill()
        elif select == 'take':
            # print()
            take()
        elif select == 'remaining':
            # print()
            remaining()
        elif select == 'exit':
            exit_coffee()


choose_actions()


class CoffeeMachine:

    def __init__(self):
        self.state = "off"

    def user_interaction(self):
        while True:
            if self.state == "choosing an action":
                choose_actions()
            elif self.state == "choosing a type of coffee":
                make_coffee()


coffee = CoffeeMachine()
coffee.__init__()
