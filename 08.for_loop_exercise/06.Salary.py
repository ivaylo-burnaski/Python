n = int(input())
salary = int(input())
for i in range(1, n + 1):
    name_of_site = input()
    if name_of_site == 'Facebook':
        salary -= 150
    elif name_of_site == 'Instagram':
        salary -= 100
    elif name_of_site == 'Reddit':
        salary -= 50
    if salary <= 0:
        print('You have lost your salary.')
        break
if salary > 0:
    print(salary)