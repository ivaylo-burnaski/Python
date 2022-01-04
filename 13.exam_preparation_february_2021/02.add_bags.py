luggage_price_up_to_20 = float(input())
luggage_weight = float(input())
days_to_trip = int(input())
luggage_count = int(input())
luggage_price = 0
if luggage_weight < 10:
    luggage_price += luggage_price_up_to_20 * 20 / 100
elif 10 <= luggage_weight <= 20:
    luggage_price += luggage_price_up_to_20 * 50 / 100
else:
    luggage_price += luggage_price_up_to_20
if days_to_trip > 30:
    luggage_price *= 1.1
elif 7 <= days_to_trip <= 30:
    luggage_price *= 1.15
elif days_to_trip < 7:
    luggage_price *= 1.4
print(f'The total price of bags is: {luggage_price * luggage_count:.2f} lv.')
