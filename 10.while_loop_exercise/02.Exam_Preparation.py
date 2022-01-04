number_of_bad_grades = int(input())
count_of_problems = 0
count_of_bad_grades = 0
sum_of_grades = 0
last_problem = ''
is_failed = True
while count_of_bad_grades < number_of_bad_grades:
    problem_name = input()
    if problem_name == 'Enough':
        is_failed = False
        break
    current_grade = int(input())
    if current_grade <= 4:
        count_of_bad_grades +=1
    count_of_problems += 1
    sum_of_grades += current_grade
    last_problem = problem_name
if is_failed:
    print(f'You need a break, {count_of_bad_grades} poor grades.')
else:
    print(f'Average score: {sum_of_grades / count_of_problems:.2f}')
    print(f'Number of problems: {count_of_problems}')
    print(f'Last problem: {last_problem}')
