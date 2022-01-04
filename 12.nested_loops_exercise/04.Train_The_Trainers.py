count_of_jury = int(input())
sum_of_grades = 0
sum_of_presentation_grades = 0
presentation_count = 0
line = input()
while line != 'Finish':
    presentation_name = line
    presentation_count += 1
    sum_of_grades = 0
    for current_grade in range(count_of_jury):
        grade = float(input())
        sum_of_grades += grade
    average_grade = sum_of_grades / count_of_jury
    sum_of_presentation_grades += average_grade
    print(f'{presentation_name} - {average_grade:.2f}.')
    line = input()
average_presentation_grade = sum_of_presentation_grades / presentation_count
print(f"Student's final assessment is {average_presentation_grade:.2f}.")
