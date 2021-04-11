money_map = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}

resource_size = {
    "water": "ml",
    "milk": "ml",
    "coffee": "g",
}

def report(resources, money):
    global resource_size
    for r in resources:
        print(f"{str(r).capitalize()}: {resources[r]}{resource_size[r]}")        
    print(f"Money: ${money}")
   
def resource_enough(resources, ingredients):
    for r in ingredients:
        if (resources[r] < ingredients[r]):
            print(f"Sorry there is not enough {r}.")
            return False                    
    return True

def process_coins():
    print("Please insert coins.")
    money = 0
    global money_map
    for n in money_map:
        money += int(input(f"How may {n}?: "))*money_map[n]
    return money
