import random
import word_list
import hangman_art

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

lives = 0
chosen_word = random.choice(word_list.word_list)
win_display = []
guessed_letters = []

# print(f"The solution is {chosen_word}")

display = []

for n in chosen_word:
    display.append("_")
print(hangman_art.hangman_logo[0])
while "_" in display:
    guess = ""
    while guess not in letters:
        if guess == chosen_word:
            for n in chosen_word:
                win_display.append(n)
            print("You guessed the full word! Good job!")
            print("You WIN!")
            print(*win_display)
            display.clear()
            break
        guess = input("Guess a letter or try to guess the full word: \n").lower()
    if guess in display:
        print("You already guessed that letter\n")

    if len(guess) > 1 and guess != chosen_word:
        print("You tried to guess the full word, but it's wrong :(")
        print(f"The word was {chosen_word}")
        print("You LOSE!")
        print(*display)
        print(hangman_art.hangman_pic[6])
        break

    def find_position(word, letter):
        return word.find(letter)

    letter_occurrence = chosen_word.count(guess)

    if guess in chosen_word and letter_occurrence > 1:
        positions = []
        for i, char in enumerate(chosen_word):
            if char == guess:
                positions.append(i)
        for n in positions:
            display[n] = guess
    if guess in chosen_word and letter_occurrence == 1 and len(guess) < 2:
        position = find_position(chosen_word, guess)
        display[position] = guess
    if guess not in chosen_word:
        lives += 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if guess not in guessed_letters:
            guessed_letters.append(guess)
            print("Guessed letters:", *guessed_letters)
        else:
            print("Guessed letters:", *guessed_letters)
            pass
    if lives == 6:
        print(f"Out of lives, you died. The word was {chosen_word}")
        print(hangman_art.hangman_pic[6])
        break
    print(f"You guessed the letter {guess}")
    print(*display)
    print(hangman_art.hangman_pic[lives])
else:
    print("You win!")
