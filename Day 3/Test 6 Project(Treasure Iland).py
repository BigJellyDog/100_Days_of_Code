print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")
print('You wake up on a deserted beach, surrounded by palm trees and the sound of waves crashing against the shore.\n'
      'As you explore, you discover a tattered map in the sand that seems to lead to a hidden treasure on the '
      'mysterious \n'
      'Treasure Island. Excited, you decide to embark on a thrilling adventure to uncover the secrets of the island '
      'and\n'
      'claim the treasure for yourself.')
player_choice = input("As you follow the map, you reach a fork in the path. To the left, a dense jungle awaits,\n"
                      "and to the right, a rocky cliff overlooks the ocean. Which path will you choose? \n"
                      "type 'J' for Jungle or 'C' for Cliff: \n")
if player_choice == "J":
    print("You successfully navigate the jungle, discovering a waterfall with a hidden cave behind it.\nInside the "
          "cave, you find a stash of ancient artifacts and a clue pointing you towards an old pirate camp.")
    player_choice = input("Head to the Pirate Camp: Investigate the camp for clues, potentially encountering "
                          "unfriendly pirates. (Type: P): \n")
    if player_choice == "P":
        print("At the pirate camp, you find a hidden map leading to a buried treasure. However, you attract the \n"
              "attention of the pirates guarding it, leading to a confrontation.")
        print("Having obtained valuable information, you face another critical decision:")
        player_choice = input("Confront the Pirates (Type 'C'): \nEngage in a battle with the pirates to claim the "
                              "treasure for yourself. \n")
        if player_choice == "C":
            print("A fierce battle ensues, and with cunning tactics, you defeat the pirates. However, the noise \n"
                  "attracts the attention of a mysterious island guardian.\n")
elif player_choice == "C":
    print("As you climb the cliff, you spot a shipwreck below. Descending carefully, you find a chest of supplies \n"
          "from the wreck, including a rare compass pointing to the heart of the island.")
    player_choice = input("Explore the Mysterious Cave: Enter the dark cave, risking the unknown dangers within.\n"
                          "(Type M): \n")
    if player_choice == "M":
        print("Inside the cave, you discover a hidden passage leading to an underground chamber. Solve a puzzle to \n"
              "reveal the location of the treasure.")
        print("Having obtained valuable information, you face another critical decision:")
        player_choice = input("Continue Solving the Puzzle (Type 'S'): \nDedicate more time to decipher the remaining "
                              "clues, avoiding a direct confrontation.")
        if player_choice == "S":
            print("By solving the remaining puzzles, you uncover the exact location of the treasure without alerting \n"
                  "anyone. However, the route to the treasure is guarded by mystical traps.")

print("Regardless of your previous choices, you find yourself face-to-face with the island guardian, a mythical \n"
      "creature protecting the treasure. The final decision determines your fate:\n")
print("1.Fight the Guardian (Type 'F'):Engage in a challenging battle, risking everything for the "
      "treasure.\n2.Negotiate with"
      "the Guardian (Type 'N'): Attempt to communicate with the guardian, convincing it to let you have the "
      "treasure.\n3.Flee "
      "from the Guardian (Type 'E'): Make a run for it, hoping to escape the island without the treasure.")
player_choice = input("Type F N or E: \n\n")
if player_choice == "F":
    print("Victory!:\n"
          "After a fierce battle, you emerge victorious against the island guardian. The once ferocious creature now \n"
          "acknowledges your strength and determination. As you claim the legendary treasure, you notice the guardian \n"
          "fading away, its duty fulfilled. The treasure, infused with the guardian's magic, grants you not only \n"
          "immense wealth but also enhanced abilities. Legends of your triumph spread far and wide, and you become a "
          "revered figure among treasure hunters.\n\nAs you touch the treasure, you feel a surge of power coursing \n"
          "through you. It's not just gold and jewels - it's a source of ancient magic. You gain the ability to \n"
          "understand and manipulate elements, setting you apart from ordinary adventurers. The island guardian, \n"
          "now at peace, dissipates into a beam of light, leaving you with a sense of gratitude.")
elif player_choice == "N":
    print("Negotiation Success:\n"
          "Your diplomatic approach pays off, and you successfully convince the guardian to \n"
          "share a portion of the treasure. As a token of goodwill, the guardian imparts ancient \n"
          "knowledge about the island's mysteries. You leave with not only valuable riches but \n"
          "also a deep understanding of the island's secrets. The island guardian, now with a \n"
          "sense of trust in outsiders, watches over the remaining treasures, ensuring they are \n"
          "respected by future adventurers.\n\n"
          "The guardian, pleased with your respectful attitude, offers to accompany you on your \n"
          "future journeys. With the guardian as your ally, you become the guardian of the \n"
          "island's mystical legacy, working together to maintain a delicate balance between \n"
          "treasure hunters and the island's ancient magic.")
elif player_choice == "E":
    print("Escape:\n"
          "Choosing to escape without the treasure, you navigate the island's perils with skill and \n"
          "agility. The guardian, respecting your decision to leave the treasure untouched, allows \n"
          "you to depart without interference. As you sail away, the island's mysterious aura \n"
          "remains etched in your memory, and you become a storyteller, recounting your thrilling \n"
          "adventure to captivated audiences around the world. \n\n"
          "Realizing the consequences of your actions, you race against time to appease the \n"
          "angered island. Navigating through natural disasters requires wit, courage, and \n"
          "resourcefulness. As you escape with a portion of the treasure, the island, forever \n"
          "changed, serves as a cautionary tale for those who seek to exploit its mystical treasures")
