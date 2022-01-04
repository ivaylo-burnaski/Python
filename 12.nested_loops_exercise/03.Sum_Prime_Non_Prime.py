sum_of_prime_numbers = 0
sum_of_non_prime_numbers = 0
line = input()
while line != 'stop':
    number = int(line)
    if number < 0:
        print('Number is negative.')
        line = input()
        continue
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        sum_of_prime_numbers += number
    else:
        sum_of_non_prime_numbers += number
    line = input()
print(f'Sum of all prime numbers is: {sum_of_prime_numbers}')
print(f'Sum of all non prime numbers is: {sum_of_non_prime_numbers}')
