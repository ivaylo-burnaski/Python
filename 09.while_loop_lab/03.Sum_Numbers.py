number = int(input())
sum_of_numbers = 0
current_number = int(input())
sum_of_numbers += current_number
while sum_of_numbers < number:
    current_number = int(input())
    sum_of_numbers += current_number
print(sum_of_numbers)