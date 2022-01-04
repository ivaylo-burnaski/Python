name_of_student = input()
class_number = 1
sum_of_grades = 0
is_failed = False
while class_number <= 12:
    grade = float(input())
    if grade < 4.00:
        if is_failed:
            break
        is_failed = True
        continue
    class_number += 1
    sum_of_grades += grade
if class_number < 12:
    print(f'{name_of_student} has been excluded at {class_number} grade')
else:
    print(f'{name_of_student} graduated. Average grade: {sum_of_grades / (class_number -1):.2f}')


