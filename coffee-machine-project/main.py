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


# TODO 1. take the user input which one then prepare recipe according to the item asked for add value to the each type of coin.
order = input("Please press a button which type of coffee you want to order ('espresso','latte','cappuccino'): ")
ten_rs = int(input("Please enter the amount you want to pay as ₹10 coin. :"))
five_rs = int(input("Please enter the amount you want to pay as ₹5 coin. :"))
two_rs = int(input("Please enter the amount you want to pay as ₹2 coin. :"))
one_rs = int(input("Please enter the amount you want to pay as ₹1 coin. :"))
# TODO 2. check the MENU["cost"] is greater than equals to or not.. if less than that then return return the amount
money_enterd = (ten_rs*10)+(five_rs*5)+(two_rs*2)+(one_rs*2)
order_cost = MENU[order]["cost"]
if money_enterd > order_cost:
    change = money_enterd - order_cost
    print(f"here's your ₹{change} change sir/ma'am")
elif money_enterd == order_cost:
    print("Thanks for your money sir/ma'am, Please keep patience until I process your drink")
else:
    print(f"I dint got enough money to make the coffee for you, here's you money sir/ma'am {money_enterd}")
# TODO 3. create a function to deduct take that variable from MENU[variableName] resource item
def take_ingredients(res_ing, req_ing):
    if res_ing["water"] > req_ing[order][wa]:
        return res_ing - req_ing
    else:
        
# TODO 4. *additional check* check as the user asked for coffee if all the ingredients he got correctly or not
