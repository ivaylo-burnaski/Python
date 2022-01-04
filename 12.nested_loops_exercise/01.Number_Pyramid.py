number = int(input())
current_number = 0
numbers_are_finished = False
for row in range(1, number + 1):
    for column in range(1, row + 1):
        current_number += 1
        print(current_number, end=' ')
        if current_number == number:
            numbers_are_finished = True
            break
    if numbers_are_finished:
        break
    print()
