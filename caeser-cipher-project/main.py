from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

restart = "y"

def cipher (text, shift):
    listed_text = list(text)
    for i in range (0,len(listed_text)):
        if listed_text[i] in alphabet:
            shifted_position=0
            alphabet_position = alphabet.index(listed_text[i])
            if direction == "encode":
                shifted_position = (alphabet_position+shift) % 26
            elif direction == "decode":
                shifted_position = (alphabet_position - shift) % 26
            else:
                print("Please write the correct 'encode' or 'decode' command to get system work properly")
                break
            listed_text[i] = alphabet[shifted_position]
    print(f"Your {direction}d cipher text is '{''.join(listed_text)}'\n")
    global restart
    restart = input("\nDo you want to restart? (type 'y' or 'n'):").lower()

while restart == "y":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cipher(text,shift)

print ("Goodbye 👋")
