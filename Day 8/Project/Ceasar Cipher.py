alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def encrypt(plain_text, shift_amount):
    encrypted_word = ""
    for letter in plain_text:
        if letter not in alphabet:
            encrypted_word += letter
        else:
            i = alphabet.index(letter)
            encrypted_word += alphabet[(i + shift_amount) % 52]

    print(f"Here's the encoded result: {encrypted_word}")


def decrypt(encrypted_text, shift_amount):
    decrypted_word = ""
    for letter in encrypted_text:
        if letter not in alphabet:
            decrypted_word += letter
        else:
            i = alphabet.index(letter)
            decrypted_word += alphabet[(i - shift_amount) % 52]

    print(f"Here's the decoded result: {decrypted_word}")


coder = True
print('''
                                         _       _            
                                        (_)     | |              
  ___ __ _  ___  ___  __ _ _ __      ___ _ _ __ | |__   ___ _ __    
 / __/ _` |/ _ \/ __|/ _` | '__|    / __| | '_ \| '_ \ / _ \ '__|          
| (_| (_| |  __/\__ \ (_| | |      | (__| | |_) | | | |  __/ |       
 \___\__,_|\___||___/\__,_|_|       \___|_| .__/|_| |_|\___|_|   
                                        | | 
                                        |_| 
''')


while coder:

    direction = input("Type 'encode' to encrypt, type 'decode to decrypt: \n")

    if direction == "encode":
        encrypt(input("Type your message:\n"), int(input("Type the shift number: \n")))
        coder = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    elif direction == "decode":
        decrypt(input("Type your message:\n"), int(input("Type the shift number: \n")))
        coder = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    else:
        print("Please write 'encode' or 'decode'")
