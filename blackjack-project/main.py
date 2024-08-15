import random
from replit import clear
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
continue_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

def pick_up():
    return cards[random.randint(0, len(cards) - 1)]

def add_all(list):
    if sum(list) > 21 and 11 in list:
        list.remove(11)
        list.append(1)
    return sum(list)

def main():
    clear()
    print(logo)
    users_deck = [pick_up()]
    computers_deck = [pick_up(), pick_up()]
    continus_draw = "y"

    while continus_draw == "y":
        users_deck.append(pick_up())
        if add_all(computers_deck) == 21 and len(computers_deck) == 2:
            return print(f"    Computer has a blackjack, **You loose.**\nComputer's hand {computers_deck}."
            )
        elif add_all(users_deck) == 21 and len(users_deck) == 2:
            return print(f"    You have a blackjack, **You win.**\nYou have {users_deck} in your hand."
            )
        elif add_all(users_deck) > 21:
            return print(f"Your current total is {add_all(users_deck)}, and you have {users_deck} in your hand\n    **You're Busted!!**\nComputer's hand {computers_deck}."
            )
        else:
            print(f"Your cards {users_deck}, current score: {add_all(users_deck)}")
            print(f"Computer's first card: [{computers_deck[0]}]")
            continus_draw = input("\nDo you wanna draw another card 'y' for yes 'n' to pass :")
    while add_all(computers_deck) < 17:
        computers_deck.append(pick_up())

    result = f"> Computer hand : {computers_deck}, total =  {add_all(computers_deck)}.\n> Your hand : {users_deck}, total = {add_all(users_deck)}."
    if 22 > add_all(computers_deck) > add_all(users_deck):
        return print(f"{result}\n    Oh Nooo! You loose, computer won\nYou should play another game\n")
    elif add_all(computers_deck) < add_all(users_deck):
        return print(f"{result}\n    Yeee!! You won..\n")
    elif add_all(computers_deck) == add_all(users_deck):
        return print(f"{result}\n    Shit! It's a draw.\nYou should play another game\n")
    else:
        return print(f"{result}\n    Computer Busted, You Won!!")

while continue_play == "y":
    main()
    continue_play = input("\nDo you want to play another game of Blackjack? Type 'y' or 'n': ")
