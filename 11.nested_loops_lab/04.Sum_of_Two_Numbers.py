start_of_interval = int(input())
end_of_interval = int(input())
special_number = int(input())
combinations_counter = 0
is_found = False
for i in range(start_of_interval, end_of_interval + 1):
    for j in range(start_of_interval, end_of_interval + 1):
        combinations_counter += 1
        if i + j == special_number:
            is_found = True
            break
    if is_found:
        break
if is_found:
    print(f'Combination N:{combinations_counter} ({i} + {j} = {special_number})')
else:
    print(f'{combinations_counter} combinations - neither equals {special_number}')
