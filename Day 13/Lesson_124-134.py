############DEBUGGING#####################

# Describe Problem
# def my_function():
#     for i in range(1, 20):
#         # The for loop can't reach 20 so the if statement will never be executed because the range module does not
#         # include 20 to fix it the range needs to be 1, 21
#         if i == 20:
#             print("You got it")
#
#
# my_function() # Fixed

# # Fixed
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer Fixed
# year = int(input("What's your year of birth? "))
# if 1994 >= year >= 1980:
#     print("You are a millennial.")
# elif year > 1994:
#     print("You are a Gen Z.")

# # Fixed the Errors
# age = int(input("How old are you? "))
# if age >= 18:
#     print(f"You can drive at age {age}.")

# # Fixed
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)


# Fixed

# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)
#
#
# mutate([1, 2, 3, 5, 8, 13])
