print("The Love Calculator is calculating your score...")
name1 = "John"
name2 = "Jane"
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
i = 0
name3 = str(name1.upper() + name2.upper())
letters1 = ['T', 'R', 'U', 'E']
letters2 = ['L', 'O', 'V', 'E']

for letter1 in letters1:
    if letter1 in name3:
        i += 10
for letter2 in letters2:
    if letter2 in name3:
        i += 1

if i < 10 or i > 90:
    print(f"Your score is {i}, you got together like coke")
elif 40 <= i <= 50:
    print(f"Your score is {i}, you are alright together.")
else:
    print(f"Your score is {i}.")
