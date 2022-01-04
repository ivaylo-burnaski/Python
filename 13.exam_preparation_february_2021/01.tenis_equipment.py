from math import ceil, floor
tennis_rocket_price = float(input())
count_of_tennis_rockets = int(input())
count_of_sneakers = int(input())
sneakers_price = tennis_rocket_price / 6
current_sum = count_of_tennis_rockets * tennis_rocket_price + count_of_sneakers * sneakers_price
other_equipment = current_sum * 20 / 100
total_price = current_sum + other_equipment
print(f'Price to be paid by Djokovic {floor(total_price / 8)}')
print(f'Price to be paid by sponsors {ceil(total_price * 7 / 8)}')
