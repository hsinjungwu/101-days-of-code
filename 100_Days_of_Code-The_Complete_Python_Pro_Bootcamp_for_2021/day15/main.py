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

import model

def sell():
    balance = 0
    while True:
        word = input("What would you like? (espresso/latte/cappuccino): ")
        if word == "off":
            break

        if word == "report":
            model.report(resources, balance)        
        elif word in MENU:                       
            drink = MENU[word]
            ingredients = drink["ingredients"]
            if model.resource_enough(resources, ingredients):
                money = model.process_coins()
                cost = drink["cost"]
                if money < cost:
                    print("Sorry that's not enough money. Money refunded.")

                for i in ingredients:
                    resources[i]-= ingredients[i]
                balance += cost
                change = money - cost
                if change > 0:
                    print(f"Here is ${change} in change.")
                print(f"Here is your {word} ☕️. Enjoy!")            
        else:
            print("Invalid Word")

sell()