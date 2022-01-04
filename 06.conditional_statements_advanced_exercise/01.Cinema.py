kind_of_projection = input()
rows = int(input())
columns = int(input())
count_of_seats = rows * columns
ticket_price = 0
if kind_of_projection == 'Premiere':
    ticket_price = 12.00
elif kind_of_projection == 'Normal':
    ticket_price = 7.50
elif kind_of_projection == 'Discount':
    ticket_price = 5.00
total_income = count_of_seats * ticket_price
print(f'{total_income:.2f} leva')