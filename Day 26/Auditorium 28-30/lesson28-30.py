"""Learning list comprehension"""

"""LESSON 28 DAY 26 - SQUARING NUMBERS"""
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n*n for n in numbers]

"""LESSON 29 DAY 26 - FILTERING EVEN NUMBERS"""
list_of_strings = ["9", "0", "32", "8", "2", "8", "64", "29", "42", "99"]
result1 = [int(n) for n in list_of_strings if int(n) % 2 == 0]

"""LESSON 30 DAY 26 - DATA OVERLAP"""
result2 = [int(n) for n in open("file1.txt") if n in open("file2.txt")]
print(result2)
