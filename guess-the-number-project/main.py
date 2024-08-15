#Number Guessing Game Objectives:

# Include an ASCII art logo.
from art import logo
import random

print(logo)
# Allow the player to submit a guess for a number between 1 and 100.
guessed_number = random.randint(1,100)
users_guessed = ""
print("I have done guessing, now it's your turn to guees the number I guessed.😉")
life = 5
is_game_over = False
choosen_level = input("Choose your difficulty level \n'e' for easy,\n'n' for normal,\n'h' for hard\n> ")
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
if choosen_level == "e":
  life = 10
elif choosen_level == "n":
  life = 7
else:
  life =4

# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

def game_stats(guess1, guess2, life):
  if guess1 == guess2:
    print("You've gussed the correct number.")
    return True
  else:
    if life == 0:
      print(f"I gussed the number{guess2}")
      return True
    else:
      return False

def guidence(num1, num2):
  if num1 > num2:
    if num1 - num2 > 15:
      return "The number is much bigger than your guess."
    else:
      return "You are closer to the number, It's a bit largeer than your number"
  elif num2 > num1:
    if num2 - num1 > 15:
      return "The number is much smaller than your guess."
    else:
      return "You are closer to the number, It's a bit smaller than your number"
  else:
    return f"You gussed it correct!! The answer was {num1}"

while not is_game_over:
  users_guessed = int(input("Guess the number : "))
  #global is_game_over;
  is_game_over = game_stats(guess1=users_guessed, guess2=guessed_number, life=life)
  life -= 1
  print(f"Sorry that wasn't the correct answer, you have {life} life(s) left.")
  if not is_game_over:
    print(guidence(num1=guessed_number, num2=users_guessed))
  # if guessed_number == users_guessed:
  #   is_game_over = True
  #   if life == 0:
  #     print(f"You have {life} lifes remaining loose!! \nthe number I was guessing about {guessed_number}")
  #   else:
  #     print("You gussed it right, YOU WON!!")
  #     break
  # print(guidence())
  # print(f"You have {life} lives reaining")
  # life -= 1
