import pandas
import pyautogui


def clear(key):
    """
    Pressing the clear key for you
    insert the key name into the input as string
    """
    pyautogui.press(key)


data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

while True:
    word = input("Enter a word: ").upper()
    clear("F10")
    if word == "EXIT":
        break
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError as key_name:
        print(f"'{word}' This is not a letter, only letter please")
    else:
        print(output_list)
