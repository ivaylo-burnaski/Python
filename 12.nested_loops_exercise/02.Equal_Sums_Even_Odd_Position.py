start_number = int(input())
end_number = int(input())
for number in range(start_number, end_number + 1):
    odd_sum = 0
    even_sum = 0
    current_number = str(number)
    for index, digit in enumerate(current_number):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    if even_sum == odd_sum:
        print(current_number, end=' ')
