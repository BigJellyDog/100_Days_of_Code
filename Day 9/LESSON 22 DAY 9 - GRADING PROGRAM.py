student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = student_scores

for student in student_grades:
    value = student_grades[student]
    if value in range(91, 101):
        student_grades[student] = "Outstanding"
    elif value in range(81, 91):
        student_grades[student] = "Exceeds Expectations"
    elif value in range(71, 81):
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"



print(student_grades)
# print(student_scores)