number = int(input())
for current_number in range(1111, 10000):
    is_special = True
    for index, digit in enumerate(str(current_number)):
        current_digit = int(digit)
        if current_digit == 0 or number % current_digit != 0:
            is_special = False
            break
    if is_special:
        print(current_number, end=' ')
