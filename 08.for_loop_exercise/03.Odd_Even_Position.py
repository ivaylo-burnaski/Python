import sys
n = int(input())
sum_of_odd = 0
min_of_odd = sys.maxsize
max_of_odd = -sys.maxsize
sum_of_even = 0
min_of_even = sys.maxsize
max_of_even = -sys.maxsize
for i in range(1, n + 1):
    number = float(input())
    if i % 2 == 0:
        sum_of_even += number
        if number > max_of_even:
            max_of_even = number
        if number < min_of_even:
            min_of_even = number
    else:
        sum_of_odd += number
        if number > max_of_odd:
            max_of_odd = number
        if number < min_of_odd:
            min_of_odd = number
print(f'OddSum={sum_of_odd:.2f},')
if min_of_odd == sys.maxsize:
    print('OddMin=No,')
else:
    print(f'OddMin={min_of_odd:.2f},')
if max_of_odd == -sys.maxsize:
    print('OddMax=No,')
else:
    print(f'OddMax={max_of_odd:.2f},')
print(f'EvenSum={sum_of_even:.2f},')
if min_of_even == sys.maxsize:
    print('EvenMin=No,')
else:
    print(f'EvenMin={min_of_even:.2f},')
if max_of_even == -sys.maxsize:
    print('EvenMax=No')
else:
    print(f'EvenMax={max_of_even:.2f}')
