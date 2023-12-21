# Write your code below this line 👇
import math


def paint_calc(height, width, cover):
    number_of_cans = (height*width)/cover
    number_of_cans = math.ceil(number_of_cans)
    print(f"You'll need {number_of_cans} cans of paint.")


test_h = 3
test_w = 9
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
