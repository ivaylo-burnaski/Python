budget = float(input())
season = input()
destination = ''
kind_of_rest = ''
spend_money = 0
if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        kind_of_rest = 'Camp'
        spend_money = 0.3 * budget
    elif season == 'winter':
        kind_of_rest = 'Hotel'
        spend_money = 0.7 * budget
elif budget > 1000:
    destination = 'Europe'
    kind_of_rest = 'Hotel'
    spend_money = 0.9 * budget
else:
    destination = 'Balkans'
    if season == 'summer':
        kind_of_rest = 'Camp'
        spend_money = 0.4 * budget
    elif season == 'winter':
        kind_of_rest = 'Hotel'
        spend_money = 0.8 * budget
print(f"Somewhere in {destination}")
print(f"{kind_of_rest} - {spend_money:.2f}")
