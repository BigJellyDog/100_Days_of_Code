"""Learning list and dictionary comprehension"""
import random
import pandas
# numbers_list = [1, 2, 3]
# new_list = [n + 1 for n in numbers_list]

# range_list = [n*2 for n in range(1, 5)]
# print(range_list)
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
#
# short_names = [name.upper() for name in names if len(name) > 5]
#
# print(short_names)

# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.items()}
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# students_scores = {student: random.randint(1, 100) for student in names}
# passed_students = {student: score for (student, score) in students_scores.items() if score > 60}

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# for (key, value) in student_data_frame.items():
#     print(value)

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)