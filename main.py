from letters import alphabet
from art import logo


def caesar(start_text, shift_amount, cipher_direction):

    end_text = ''

    if cipher_direction == 'decode':
        shift_amount *= (-1)

    for char in start_text:
        if char not in alphabet:
            end_text += char
        else:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]

    print(f"Here's the {cipher_direction}d result: {end_text}\n")


print(logo)

should_continue = "yes"

while should_continue == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift %= 26

    caesar(text, shift, direction)

    should_continue = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    if should_continue == 'no':
        print("Goodbye!")
