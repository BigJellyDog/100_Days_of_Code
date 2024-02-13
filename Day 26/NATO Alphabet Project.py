"""NATO ALPHABET"""
import pandas

# Create a dict in this format: {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet = {code.letter: code.code for (let, code) in data.iterrows()}

user_input = ""
while user_input != "EXIT":
    user_input = str(input("Enter a word: ")).upper()
    if user_input == "EXIT":
        break
    # Create a list of the phonetic code words from a word that the user inputs.
    try:
        result = [word for n in user_input for letter, word in alphabet.items() if letter == n]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
    else:
        print(result)
