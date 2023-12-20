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

player_choice = int(input("Type 0 for rock, 1 for paper, and 2 for scissors: "))
computer_choice = random.randint(0, 2)
if player_choice > 2 or player_choice < 0:
    print("Not a valid choice :(")
else:
    print(list1[player_choice] + "\nComputer chose:\n" + list1[computer_choice])

if player_choice == 1 and computer_choice == 0:
    print("You win!")
elif player_choice == 2 and computer_choice == 1:
    print("You win!")
elif player_choice == 0 and computer_choice == 2:
    print("You win!")
elif player_choice == computer_choice:
    print("Draw")
else:
    print("You lose")
