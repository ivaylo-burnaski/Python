month = input()
spent_hours = int(input())
count_group_members = int(input())
day_time = input()
price_per_hour = 0
if month == 'march' or month == 'april' or month == 'may':
    if day_time == 'day':
        price_per_hour = 10.5
    else:
        price_per_hour = 8.4
elif month == 'june' or month == 'july' or month == 'august':
    if day_time == 'day':
        price_per_hour = 12.6
    else:
        price_per_hour = 10.2
if count_group_members >= 4:
    price_per_hour *= 0.9
if spent_hours >= 5:
    price_per_hour *= 0.5
total_visit_price = price_per_hour * spent_hours * count_group_members
print(f'Price per person for one hour: {price_per_hour:.2f}')
print(f'Total cost of the visit: {total_visit_price:.2f}')
