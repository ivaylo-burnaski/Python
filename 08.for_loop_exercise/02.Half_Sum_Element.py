import sys
n = int(input())
max_number = -sys.maxsize
sum_of_others = 0
for i in range(1, n + 1):
    number = int(input())
    if number > max_number:
        max_number = number
    sum_of_others += number
sum_of_others -= max_number
if max_number == sum_of_others:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    print('No')
    print(f'Diff = {abs(max_number - sum_of_others)}')
