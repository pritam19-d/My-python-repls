from random import choice
from art import logo, vs
from replit import clear
from game_data import data

value_A = choice(data)
is_game_over = False

score = 0

def check (a,b):
    if a > b:
        return "a"
    elif b > a:
        return "b"

def game(a):
    b = choice(data)
    while a == b:
        b = choice(data)
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.\n{vs}\n")
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
    return b

#need to create a loop until is_game_over is false
while not is_game_over:
    clear()
    print (logo)
    value_B = game(value_A)
    answer = check (value_A['follower_count'], value_B['follower_count'])
    print(f"Your current score is {score}.")
    print(f"testing: answer = {answer}")
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if answer == user_guess:
        score += 1
        value_A = value_B
    else:
        clear()
        is_game_over = True
        print(f"Sorry you gussed it wrong.\nGame Over!!\nYour total score is {score}")

