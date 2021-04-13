from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_coffer_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

while True:
    word = input("What would you like? (espresso/latte/cappuccino): ")
    if word == "off":
        break
    elif word == "report":
        my_coffer_maker.report()
        my_money_machine.report()
    else:
        drink = my_menu.find_drink(word)
        if drink == None:
            print("Invalid Word")
        else:                                
            if my_coffer_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):                                        
                    my_coffer_maker.make_coffee(drink)

