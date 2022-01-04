income = float(input())
average_evaluation = float(input())
min_salary = float(input())
success_scholarship = int(average_evaluation * 25)
social_scholarship = int(min_salary * 0.35)
if income > min_salary:
    if average_evaluation >= 5.50:
        print(f'You get a scholarship for excellent results {success_scholarship} BGN')
    else:
        print('You cannot get a scholarship!')
else:
    if average_evaluation <= 4.50:
        print('You cannot get a scholarship!')
    elif 4.50 < average_evaluation < 5.50:
        print(f'You get a Social scholarship {social_scholarship} BGN')
    else:
        if success_scholarship >= social_scholarship:
            print(f'You get a scholarship for excellent results {success_scholarship} BGN')
        else:
            print(f'You get a Social scholarship {social_scholarship} BGN')