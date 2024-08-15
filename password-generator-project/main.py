#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

new_password ="";
for l in range(0,nr_letters):
  new_password += letters[random.randint(0,26)]
for s in range (0,nr_symbols):
  new_password += symbols[random.randint(0,8)]
for i in range (0, nr_numbers):
  new_password += numbers[random.randint(0,9)]
print(new_password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# this :--
pwd = random.sample(list(new_password),len(new_password))
generated_pwd = "".join(pwd)
print (generated_pwd)

# or this :--
pwd_list = list(new_password)
random.shuffle(pwd_list)
generated_pwd = "".join(pwd_list)
print(generated_pwd)
