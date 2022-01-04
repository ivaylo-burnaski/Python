days = int(input())
kind_of_residence = input()
satisfaction = input()
nights = days - 1
price_per_night = 0
if kind_of_residence == 'room for one person':
    price_per_night = 18.00
elif kind_of_residence == 'apartment':
    price_per_night = 25.00
elif kind_of_residence == 'president apartment':
    price_per_night = 35.00
total_price = nights * price_per_night
if kind_of_residence == 'apartment':
    if nights < 10:
        total_price *= 0.70
    elif 10 < nights < 15:
        total_price *= 0.65
    elif nights > 15:
        total_price *= 0.5
if kind_of_residence == 'president apartment':
    if nights < 10:
        total_price *= 0.90
    elif 10 < nights < 15:
        total_price *= 0.85
    elif nights > 15:
        total_price *= 0.8
if satisfaction == 'positive':
    total_price *= 1.25
elif satisfaction == 'negative':
    total_price *= 0.9
print(f'{total_price:.2f}')
