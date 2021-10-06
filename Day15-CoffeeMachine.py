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

profit = 0

coffee = input("What would you like? (espresso/latte/cappuccino): ")
if coffee == "report":
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")
elif coffee == "resources":
    print(resources)
elif not(coffee == "espresso" or coffee == "latte" or coffee == "cappuccino"):
    print("We don't have that!")
else:
    if (resources["water"] < MENU[coffee]["ingredients"]["water"]) or\
            (resources["milk"] < MENU[coffee]["ingredients"]["milk"]) or\
            (resources["coffee"] < MENU[coffee]["ingredients"]["coffee"]):
        print("There is no enough resources")

    print("Please insert coins.")
    quarters = int(input("How many quarters? -> "))
    dimes = int(input("How many dimes? -> "))
    nickels = int(input("How many nickels? -> "))
    pennies = int(input("How many pennies? -> "))
    given = pennies * 0.01 + nickels * 0.05 + dimes * 0.1 + quarters * 0.25
    change = round(given - MENU[coffee]["cost"], 2)
    if change < 0:
        print("You didn't give enough money")
    else:
        for item in resources:
            resources[item] -= MENU[coffee]["ingredients"][item]
        profit += MENU[coffee]["cost"]
        print(f"Here is ${change} in change")
        print(f"Here is your {coffee}. Enyoj!")
