import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def number_input(s):
    """Asking for user input and returning it as a float number"""
    while True:

        number = input(s)
        try:
            number = int(number)
            break
        except ValueError:
            print("Please choose a number")
            continue
    return number


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for letter in start_text:
        if letter not in alphabet:
            end_text += letter
        elif cipher_direction == "decode":
            i = alphabet.index(letter)
            end_text += alphabet[(i + shift_amount) % 52]
        else:
            i = alphabet.index(letter)
            end_text += alphabet[(i - shift_amount) % 52]

    print(f"The {cipher_direction}d text is: {end_text}\n")


coder = True
print(art.art)
while coder:

    direction = input("Type 'encode' to encrypt, type 'decode to decrypt: ").lower()
    text = input("Type your message: ")
    shift = number_input("Type the shift number: ")
    # shift = int(input("Type the shift number: "))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    coder = input("Type 'yes' if you want to go again. Otherwise type 'no': \n")
    if coder == "no":
        print("Goodbye!")
        coder = False
    else:
        coder = True
