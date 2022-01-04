kind_of_flowers = input()
count_of_flowers = int(input())
budget = int(input())
flowers_price = 0
if kind_of_flowers == 'Roses':
    flowers_price = count_of_flowers * 5
    if count_of_flowers > 80:
        flowers_price *= 0.9
elif kind_of_flowers == 'Dahlias':
    flowers_price = count_of_flowers * 3.80
    if count_of_flowers > 90:
        flowers_price *= 0.85
elif kind_of_flowers == 'Tulips':
    flowers_price = count_of_flowers * 2.80
    if count_of_flowers > 80:
        flowers_price *= 0.85
elif kind_of_flowers == 'Narcissus':
    flowers_price = count_of_flowers * 3
    if count_of_flowers < 120:
        flowers_price *= 1.15
elif kind_of_flowers == 'Gladiolus':
    flowers_price = count_of_flowers * 2.5
    if count_of_flowers < 80:
        flowers_price *= 1.20
if flowers_price <= budget:
    print(f'Hey, you have a great garden with {count_of_flowers} {kind_of_flowers} and {budget - flowers_price:.2f} leva left.')
else:
    print(f'Not enough money, you need {flowers_price - budget:.2f} leva more.')
