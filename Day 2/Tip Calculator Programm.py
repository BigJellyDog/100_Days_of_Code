print("Welcome to the tip calculator:")
total_bill = float(input("What was the total bill? $"))
percentage = int(input("What would you like to give? 10, 12, or 15? ")) / 100
people = int(input("How many people to split the bill? "))
tip = ((total_bill + (total_bill*percentage)) / people)
tip = round(tip, 2)
print(f"Each person should pay: ${tip}")
