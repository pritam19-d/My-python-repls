import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print("Welcome to the classic Rock-Paper-Scissors Game")
user_choosen = int(input("Choose your option from below \n'1' for 'Rock', \n'2' for 'Paper' \n'3' for 'Scissor'\n >"))
random_num = random.randint(0,2)

rps = [rock, paper, scissors]

if (user_choosen-1) == 0:
  print(rock)
  comp_choosen = rps[random_num]
  print(f"The computer chooses {comp_choosen}")
  
  if random_num == 1:
    print("You lost, Computer wins!")
  elif random_num == 2:
    print("Hurray!!! You win!! Computer loses the game!")
  elif random_num == 0:
    print("That was a draw, try once again!")
elif (user_choosen-1) == 1:
  print(paper)
  comp_choosen = rps[random_num]
  print(f"The computer chooses {comp_choosen}")

  if random_num == 2:
    print("You lost, Computer wins!")
  elif random_num == 0:
    print("Hurray!!! You win!! Computer loses the game!")
  elif random_num == 1:
    print("That was a draw, try once again!")
elif (user_choosen-1) == 2:
  print(scissors)
  comp_choosen = rps[random_num]
  print(f"The computer chooses: {comp_choosen}")

  if random_num == 0:
    print("You lost, Computer wins!")
  elif random_num == 1:
    print("Hurray!!! You win!! Computer loses the game!")
  elif random_num == 2:
    print("That was a draw, try once again!")
else:
  print("That was an invalid number please enter 1 or 2 or 3")
