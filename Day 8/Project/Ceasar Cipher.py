import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


# def encrypt(plain_text, shift_amount):
#     encrypted_word = ""
#     for letter in plain_text:
#         if letter not in alphabet:
#             encrypted_word += letter
#         else:
#             i = alphabet.index(letter)
#             encrypted_word += alphabet[(i + shift_amount) % 52]
#
#     print(f"Here's the encoded result: {encrypted_word}")
#
#
# def decrypt(encrypted_text, shift_amount):
#     decrypted_word = ""
#     for letter in encrypted_text:
#         if letter not in alphabet:
#             decrypted_word += letter
#         else:
#             i = alphabet.index(letter)
#             decrypted_word += alphabet[(i - shift_amount) % 52]
#
#     print(f"Here's the decoded result: {decrypted_word}")


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

    direction = input("Type 'encode' to encrypt, type 'decode to decrypt: \n")
    text = input("Type your message: \n")
    shift = int(input("Type the shift number: \n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    coder = input("Type 'yes' if you want to go again. Otherwise type 'no': \n")
    if coder == "no":
        print("Goodbye!")
        coder = False
    else:
        coder = True

