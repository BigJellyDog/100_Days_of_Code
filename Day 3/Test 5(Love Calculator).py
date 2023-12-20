name1 = input("Write your Name: ")
name2 = input("Write your partners Name: ")

couple_name = name1+name2
couple_name = couple_name.lower()
x = couple_name.count("t")
x = couple_name.count("r") + x
x = couple_name.count("u") + x
x = couple_name.count("e") + x
y = couple_name.count("l")
y = couple_name.count("o") + y
y = couple_name.count("v") + y
y = couple_name.count("e") + y
score_string = str(x) + str(y)
score_value = int(score_string)
if score_value < 10 or score_value > 90:
    print(f"Your score is {score_value}, you go together like coke and mentos.")
elif 50 < score_value < 90:
    print(f"Your score is {score_value}.")
elif 40 < score_value < 50:
    print(f"Your score is {score_value}, you are alright together.")
else:
    print(f"Your score is {score_value}.")
