budget = int(input())
season = input()
count_of_fishermen = int(input())
ship_price = 0
if season == 'Spring':
    ship_price = 3000
elif season == 'Summer' or season == 'Autumn':
    ship_price = 4200
elif season == 'Winter':
    ship_price = 2600
if count_of_fishermen <= 6:
    ship_price *= 0.9
elif 7 <= count_of_fishermen <= 11:
    ship_price *= 0.85
elif count_of_fishermen >= 12:
    ship_price *= 0.75
if count_of_fishermen % 2 == 0 and season != 'Autumn':
    ship_price *= 0.95
if ship_price <= budget:
    print(f'Yes! You have {budget - ship_price:.2f} leva left.')
else:
    print(f'Not enough money! You need {ship_price - budget:.2f} leva.')
