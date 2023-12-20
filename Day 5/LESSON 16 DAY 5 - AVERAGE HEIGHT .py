student_heights = [156, 178, 165, 171, 187]

total_height = 0
student_number = 0

for height in student_heights:
    total_height += height

for n in student_heights:
    student_number += 1

average_height = total_height // student_number
print(f"total height = {total_height}")
print(f"number of students = {student_number}")
print(f"average height = {average_height}")
