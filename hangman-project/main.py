import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = word_list[random.randint(0,2)]

print(f'Pssst, the solution is {chosen_word}.')
display = []

for n in range (0, len(chosen_word)):
    display+= "_"

print ("".join(display))
lives = 6
while "_" in display and lives > 0:
    guess = input("Guess a letter: ").lower()

    n = 0
    for letter in chosen_word:
        if letter == guess:
            display[n] = guess
        elif lives >0:
            lives -= 1
            print(f"Sorry that letter isn't present in the word \nYou have {lives} of attempts left.")
        else:
            lives -= 1
            print ("game over you have exceeded your life")
        n+=1
    updated_display = "".join(display)
    print(updated_display)
