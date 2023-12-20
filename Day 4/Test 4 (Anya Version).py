import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list1 = [rock, paper, scissors]

player_choice = 0

while player_choice != 69:

    player_choice = int(input("Type 0 for rock, 1 for paper, and 2 for scissors: "))
    computer_choice = 0

    if player_choice == 0:
        computer_choice = 2
    if player_choice == 1:
        computer_choice = 0
    if player_choice == 2:
        computer_choice = 1
    if player_choice == 69:
        break

    print(list1[player_choice]+"\nComputer chose:\n"+list1[computer_choice]+"\nYou WIN!\n")
