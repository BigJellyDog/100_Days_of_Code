line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure?: ")
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
cord1 = int(position[1]) - 1  # 3
cord2 = position[0]  # B
if cord2 == "B":
    cord2 = 1
elif cord2 == "A":
    cord2 = 0
else:
    cord2 = 2

map[cord1][cord2] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
